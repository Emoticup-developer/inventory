from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from django.db import models
from django.core.exceptions import ObjectDoesNotExist
from ams.logic import DATAHANDLER
from ams.models import AccessGroupDatabase, AccessGroupUserDatabase, ApprovalProcess, ApprovalStack, ApprovalStatusDatabase, ModelNameDatabase, SubscriptionModel, UserModelPermission
from django.db import transaction
from django.apps import apps


class CustomLoginView(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request):
        try:
            username = request.data.get("username")
            password = request.data.get("password")
            user = authenticate(username=username, password=password)
            if user is None:
                raise AuthenticationFailed("Invalid credentials")
            refresh = RefreshToken.for_user(user)
            return Response(
                {
                    "access": str(refresh.access_token),
                    "refresh": str(refresh),
                    "username": user.username,
                }
            )
        except Exception as ex:
            return Response(
                {"error": str(ex)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class ModelNameDatabaseView(APIView):

    def get(self, request, pk=None):
        pipe = DATAHANDLER(request, ModelNameDatabase).process(pk=pk)
        return pipe

    def post(self, request, pk=None):
        pipe = DATAHANDLER(request, ModelNameDatabase).process(pk=pk)
        return pipe

    def put(self, request, pk=None):
        pipe = DATAHANDLER(request, ModelNameDatabase).process(pk=pk)
        return pipe

    def delete(self, request, pk=None):
        pipe = DATAHANDLER(request, ModelNameDatabase).process(pk=pk)
        return pipe


class PipelineApprove(APIView):

    def get(self, request, pk=None):
        pipe = DATAHANDLER(
            request=request, class_name=ApprovalProcess, data_copy=request.data.copy()
        ).process(pk=pk)
        return pipe

    def post(self, request):
        try:
            data_copy = request.data.copy()
            instance = ApprovalProcess.objects.filter(pk=request.data["id"]).first()

            # Authorization check
            if (
                instance.recent_user is not None
                and request.user != instance.recent_user.user
            ):
                return Response(
                    {"error": "You are not authorized to approve this request"},
                    status=status.HTTP_401_UNAUTHORIZED,
                )

            if instance.status.code == "EXECUTED":
                return Response(
                    {"error": "This request is already executed"},
                    status=status.HTTP_401_UNAUTHORIZED,
                )

            if data_copy["is_approve"] == True or data_copy["is_approve"] == "true":
                if not instance.comments:
                    instance.comments = []
                instance.comments.append(
                    {
                        "user": request.user.username,
                        "comment": data_copy["comment"],
                        "is_approve": data_copy["is_approve"],
                    }
                )

                instance.recent_user = (
                    instance.recent_user.next_user
                    if instance.recent_user and instance.recent_user.next_user
                    else None
                )
                if instance.recent_user is None:
                    with transaction.atomic():
                        model_name = instance.model_name.model_code
                        app_label = instance.model_name.model_app
                        ModelClass = apps.get_model(app_label, model_name)
                        # here the request is ready to create
                        if instance.method == "POST":
                            self.upsert_model_instance(ModelClass, instance.payload)
                            status_code = ApprovalStatusDatabase.objects.filter(
                                code="EXECUTED"
                            ).first()

                            if status_code:
                                instance.status = status_code

                            instance.save()
                            return Response(
                                {"message": "The data has been saved!"},
                                status=status.HTTP_201_CREATED,
                            )

                        elif instance.method == "PUT" or instance.method == "PATCH":
                            self.upsert_model_instance(
                                ModelClass, instance.payload, instance.update_id
                            )

                            status_code = ApprovalStatusDatabase.objects.filter(
                                code="EXECUTED"
                            ).first()

                            if status_code:
                                instance.status = status_code

                            instance.save()
                            return Response(
                                {"message": "The data has been updated!"},
                                status=status.HTTP_201_CREATED,
                            )
                        elif instance.method == "DELETE":
                            model_obj = ModelClass.objects.filter(
                                pk=instance.update_id
                            ).first()
                            model_obj.delete()
                            status_code = ApprovalStatusDatabase.objects.filter(
                                code="EXECUTED"
                            ).first()

                            if status_code:
                                instance.status = status_code

                            instance.save()
                            return Response(
                                {"message": "The data has been deleted!"},
                                status=status.HTTP_201_CREATED,
                            )
                    return Response(
                        {"message": "Something went wrong"},
                        status=status.HTTP_201_CREATED,
                    )
                else:
                    status_code = ApprovalStatusDatabase.objects.filter(
                        code="PROCESSING"
                    ).first()

                    instance.recent_user = (
                        instance.recent_user.next_user
                        if instance.recent_user.next_user
                        else None
                    )
                    if status_code:
                        instance.status = status_code
                    instance.save()
                    return Response(
                        {"message": "data sent for next approval"},
                        status=status.HTTP_201_CREATED,
                    )
            else:
                instance.comments.append(
                    {
                        "user": request.user.username,
                        "comment": data_copy["comment"],
                        "is_approve": data_copy["is_approve"],
                    }
                )
                instance.save()
                return Response(
                    {"message": "Rejected by the approver "},
                    status=status.HTTP_201_CREATED,
                )
        except Exception as ex:
            return Response(
                {"error": str(ex)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def put(self, request, pk=None):

        pipe = DATAHANDLER(
            request=request, class_name=ApprovalProcess, data_copy=request.data.copy()
        ).process(pk=pk)
        return pipe

    def delete(self, request, pk=None):
        pipe = DATAHANDLER(
            request=request, class_name=ApprovalProcess, data_copy=request.data.copy()
        ).process(pk=pk)
        return pipe

    def upsert_model_instance(self, ModelClass, data: dict, instance_id=None):
        """
        Create or update a Django model instance.
        Handles JSONField, FileField, ImageField correctly.
        """

        # Get model field map
        model_fields = {
            field.name: field
            for field in ModelClass._meta.get_fields()
            if isinstance(field, models.Field)
        }

        if instance_id:
            try:
                instance = ModelClass.objects.get(id=instance_id)
            except ObjectDoesNotExist:
                raise ValueError(
                    f"{ModelClass.__name__} with id {instance_id} not found"
                )
        else:
            instance = ModelClass()

        for field_name, value in data.items():
            if field_name not in model_fields:
                continue  # ignore unknown fields safely

            field = model_fields[field_name]

            # 🔹 Handle FileField / ImageField
            if isinstance(field, (models.FileField, models.ImageField)):
                if isinstance(value, dict) and "stored_path" in value:
                    # Assign ONLY stored path
                    setattr(instance, field_name, value["stored_path"])
                continue

            # 🔹 Handle JSONField
            if isinstance(field, models.JSONField):
                setattr(instance, field_name, value)
                continue

            # 🔹 Normal fields (CharField, BooleanField, etc.)
            setattr(instance, field_name, value)

        instance.save()
        return instance


class AccessGroupDatabaseView(APIView):
    def get(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(
            request=request, class_name=AccessGroupDatabase, data_copy=data_copy
        )
        pipe_out = pipe.process(pk=pk)
        
        if isinstance(pipe_out, Response):
            return pipe_out

        instance = pipe.objects.all()
        serializer_class = pipe.MySerializerView(pipe.class_name)
        
        return Response(serializer_class(instance, many=True).data, status=200)
    
    def post(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(
            request=request, class_name=AccessGroupDatabase, data_copy=data_copy
        ).process(pk=pk)
        return pipe
    
    def put(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(
            request=request, class_name=AccessGroupDatabase, data_copy=data_copy
        ).process(pk=pk)
        return pipe
    
    def delete(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(
            request=request, class_name=AccessGroupDatabase, data_copy=data_copy
        ).process(pk=pk)
        return pipe




class AccessGroupUserDatabaseView(APIView):
    def get(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(
            request=request, class_name=AccessGroupUserDatabase, data_copy=data_copy
        ).process(pk=pk)
        return pipe
    
    def post(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(
            request=request, class_name=AccessGroupUserDatabase, data_copy=data_copy
        ).process(pk=pk)
        return pipe
    
    def put(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(
            request=request, class_name=AccessGroupUserDatabase, data_copy=data_copy
        ).process(pk=pk)
        return pipe
    
    def delete(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(
            request=request, class_name=AccessGroupUserDatabase, data_copy=data_copy
        ).process(pk=pk)
        return pipe
    
    
class UserModelPermissionView(APIView):
    def get(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(
            request=request, class_name=UserModelPermission, data_copy=data_copy
        ).process(pk=pk)
        return pipe
    
    def post(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(
            request=request, class_name=UserModelPermission, data_copy=data_copy
        ).process(pk=pk)
        return pipe
    
    def put(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(
            request=request, class_name=UserModelPermission, data_copy=data_copy
        ).process(pk=pk)
        return pipe
    
    def delete(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(
            request=request, class_name=UserModelPermission, data_copy=data_copy
        ).process(pk=pk)
        return pipe
    
    
class SubscriptionModelView(APIView):
    def get(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(
            request=request, class_name=SubscriptionModel, data_copy=data_copy
        ).process(pk=pk)
        return pipe
    
    def post(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(
            request=request, class_name=SubscriptionModel, data_copy=data_copy
        ).process(pk=pk)
        return pipe
    
    def put(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(
            request=request, class_name=SubscriptionModel, data_copy=data_copy
        ).process(pk=pk)
        return pipe
    
    def delete(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(
            request=request, class_name=SubscriptionModel, data_copy=data_copy
        ).process(pk=pk)
        return pipe 
    
    
class ApprovalStatusDatabaseView(APIView):
    def get(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(
            request=request, class_name=ApprovalStatusDatabase, data_copy=data_copy
        ).process(pk=pk)
        return pipe
    
    def post(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(
            request=request, class_name=ApprovalStatusDatabase, data_copy=data_copy
        ).process(pk=pk)
        return pipe
    
    def put(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(
            request=request, class_name=ApprovalStatusDatabase, data_copy=data_copy
        ).process(pk=pk)
        return pipe
    
    def delete(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(
            request=request, class_name=ApprovalStatusDatabase, data_copy=data_copy
        ).process(pk=pk)
        return pipe
    
class ApprovalStackView(APIView):
    def get(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(
            request=request, class_name=ApprovalStack, data_copy=data_copy
        ).process(pk=pk)
        return pipe
    
    def post(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(
            request=request, class_name=ApprovalStack, data_copy=data_copy
        ).process(pk=pk)
        return pipe
    
    def put(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(
            request=request, class_name=ApprovalStack, data_copy=data_copy
        ).process(pk=pk)
        return pipe
    
    def delete(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(
            request=request, class_name=ApprovalStack, data_copy=data_copy
        ).process(pk=pk)
        return pipe
    
    