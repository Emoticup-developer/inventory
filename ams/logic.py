from rest_framework import serializers
from django.db.models import Q, Model
from django.core.exceptions import FieldError
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.apps import apps
from basic.models import UserDatabase
from backend_inventory.settings import CORE_USER_CODE
from bloc.route import BLOC_FUNCTIONS
from django.core.files.storage import default_storage
from rest_framework.request import Request
from django.core.files.uploadedfile import UploadedFile
import uuid

from ams.models import (
    AccessGroupDatabase,
    AccessGroupUserDatabase,
    ApprovalProcess,
    ApprovalStack,
    ApprovalStatusDatabase,
    ModelNameDatabase,
    RowLevelPermission,
    SubTask,
    SubscriptionModel,
    UserModelPermission,
)
import uuid
from django.core.files.storage import default_storage
from django.core.files.uploadedfile import UploadedFile
from rest_framework.request import Request
from django.db import transaction
import uuid


def request_to_payload(request: Request, data_copy) -> dict:
    payload = {}

    # 1. Handle normal fields
    for key, value in data_copy.items():
        if key in request.FILES:
            continue  # files handled separately

        # boolean coercion
        if isinstance(value, str):
            if value.lower() == "true":
                value = True
            elif value.lower() == "false":
                value = False

        payload[key] = value

    # 2. Handle files (single + multiple)
    for key, files in request.FILES.lists():
        payload[key] = []

        for file in files:
            ext = file.name.rsplit(".", 1)[-1]
            filename = f"approval_uploads/{uuid.uuid4()}.{ext}"

            saved_path = default_storage.save(filename, file)

            payload[key].append(
                {
                    "type": "file",
                    "original_name": file.name,
                    "stored_path": saved_path,
                    "content_type": file.content_type,
                    "size": file.size,
                }
            )

        # flatten single file
        if len(payload[key]) == 1:
            payload[key] = payload[key][0]

    return payload


DJANGO_LOOKUPS = {
    "exact",
    "iexact",
    "contains",
    "icontains",
    "in",
    "gt",
    "gte",
    "lt",
    "lte",
    "startswith",
    "istartswith",
    "endswith",
    "iendswith",
    "range",
    "isnull",
}


def dynamic_queryset_filter(query_params, queryset, order_by=None):
    if not query_params:
        return queryset.order_by(order_by) if order_by else queryset

    model: Model = queryset.model
    valid_fields = {f.name for f in model._meta.fields}

    filters = {}

    for param, value in query_params.items():
        if not value:
            continue

        parts = param.split("__", 1)
        field = parts[0]
        lookup = parts[1] if len(parts) == 2 else "exact"

        if field not in valid_fields or lookup not in DJANGO_LOOKUPS:
            continue  # silently ignore invalid filters

        # Basic type coercion
        if value.lower() in {"true", "false"}:
            value = value.lower() == "true"

        filters[param] = value

    try:
        queryset = queryset.filter(**filters)
    except FieldError:
        pass  # fail silently or log

    if order_by:
        queryset = queryset.order_by(order_by)

    return queryset


def getDynamicSerializer(model_class):
    model_class = model_class

    class DynamicSerializer(serializers.ModelSerializer):
        class Meta:
            model = model_class
            fields = "__all__"

    return DynamicSerializer


def getDynamicSerializerView(model_class):
    model_class = model_class

    class DynamicSerializer(serializers.ModelSerializer):
        class Meta:
            model = model_class
            fields = "__all__"
            depth = 1

    return DynamicSerializer


class DATAHANDLER:
    def __init__(
        self,
        request,
        class_name,
        data_copy=None,
        sub_task_uuid=None,
        extra_position=None,
        bloc=None,
    ):
        self.request = request
        self.method = request.method
        self.data = request.data
        self.data_copy = data_copy
        self.class_name = class_name
        self.can_create = False
        self.can_delete = False
        self.can_update = False
        self.can_read = False
        self.data_manager = self.data_management()
        self.approval_stack = self.check_model_author()
        self.rba = self.role_base_access()
        self.sub_task_handler = SUBTASKHANDLER(sub_task_uuid)
        self.field_names = {f.name for f in self.class_name._meta.fields}
        self.extra_position = extra_position if extra_position else []
        self.bloc = bloc if bloc else ""

    def role_base_access(self):
        model = ModelNameDatabase.objects.filter(
            model_name=self.class_name.__name__
        ).first()

        my_group = AccessGroupUserDatabase.objects.filter(
            user=self.request.user, model=model
        ).first()
        group = my_group

        if group is not None:
            m_rba = RowLevelPermission.objects.filter(
                group=group.access_group, user=self.request.user
            )
        else:
            m_rba = RowLevelPermission.objects.filter(user=self.request.user)
        return m_rba

    def check_model_author(self):
        if not self.request.user.is_authenticated:
            return Response(
                {"error": "Unauthorized request"}, status=status.HTTP_401_UNAUTHORIZED
            )

        else:
            model = ModelNameDatabase.objects.filter(
                model_name=self.class_name.__name__
            ).first()
            group_permission = AccessGroupUserDatabase.objects.filter(
                user=self.request.user, model=model
            )
            for item in group_permission:
                if item.access_group.can_create:
                    self.can_create = item.access_group.can_create
                if item.access_group.can_read:
                    self.can_read = item.access_group.can_read
                if item.access_group.can_update:
                    self.can_update = item.access_group.can_update
                if item.access_group.can_delete:
                    self.can_delete = item.access_group.can_delete

            user_level = UserModelPermission.objects.filter(
                user=self.request.user, model=model
            )
            for item in user_level:
                if item.can_create:
                    self.can_create = item.can_create
                if item.can_read:
                    self.can_read = item.can_read
                if item.can_update:
                    self.can_update = item.can_update
                if item.can_delete:
                    self.can_delete = item.can_delete

    def data_management(self):
        model = ModelNameDatabase.objects.filter(
            model_name=self.class_name.__name__
        ).first()

        data = SubscriptionModel.objects.filter(model=model).first()
        if data:
            group = AccessGroupDatabase.objects.filter(access_group_code=data.code).first()
        else:
            group = None
            
        if data and group:
            return data
        else:
            return None

    def process(self, pk=None):
        try:
            ##need to to remove once development is done
            self.can_create = True
            self.can_read = True
            self.can_delete = True
            self.can_update = True
            ## end of remove

            if self.method == "POST":
                if not self.can_create:
                    return Response(
                        {"error": "Permission denied"}, status=status.HTTP_403_FORBIDDEN
                    )
                return self.create()

            elif self.method == "GET":
                if not self.can_read:
                    return Response(
                        {"error": "Permission denied !"},
                        status=status.HTTP_403_FORBIDDEN,
                    )
                if pk:
                    return self.read(pk)
                return self.read()

            elif self.method == "PUT" or self.method == "PATCH":
                if not self.can_update:
                    return Response(
                        {"error": "Permission denied !"},
                        status=status.HTTP_403_FORBIDDEN,
                    )
                if pk:
                    return self.update(pk)
                else:
                    return Response(
                        {"error": "Invalid request"}, status=status.HTTP_400_BAD_REQUEST
                    )

            elif self.method == "DELETE":
                if not self.can_delete:
                    return Response(
                        {"error": "Permission denied !"},
                        status=status.HTTP_403_FORBIDDEN,
                    )
                if pk:
                    return self.delete(pk)
                else:
                    return Response(
                        {"error": "Invalid request"}, status=status.HTTP_400_BAD_REQUEST
                    )
            else:
                return Response(
                    {"error": "Invalid request"}, status=status.HTTP_400_BAD_REQUEST
                )

        except Exception as ex:
            return Response(
                {"error": str(ex)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def create(self):

        if self.data_manager is not None and self.data_manager.create:
            SerializerClass = self.MySerializer(self.class_name)
            serializer = SerializerClass(data=self.data_copy)

            if not serializer.is_valid():
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            model_object = self.add_model_to_create()
            model_object.save()
            return Response(
                {"message": "creation sent for approval"},
                status=status.HTTP_202_ACCEPTED,
            )
        else:
            SerializerClass = self.MySerializer(self.class_name)
            serializer = SerializerClass(data=self.data_copy)
            serializer.is_valid(raise_exception=True)
            model_out = serializer.save()

            if "creator" in self.field_names:
                model_out.creator = self.request.user

            if "company" in self.field_names:
                model_out.company = self.request.user.user_company

            model_out.save()
            self.sub_task_handler.bloc_run(self.bloc, {"model": model_out})
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    def add_model_to_create(self):
        stat = ApprovalStatusDatabase.objects.filter(code="NEW").first()
        current_approval = ApprovalStack.objects.filter(
            code=self.data_manager.code, is_first=True
        )
        if "creator" in self.field_names:
            self.data_copy["creator"] = (
                self.request.user.pk if self.request.user else None
            )

        if "company" in self.field_names:
            self.data_copy["company"] = (
                self.request.user.user_company.pk
                if self.request.user.user_company
                else None
            )

        model_object = ApprovalProcess.objects.create(
            model_name=self.data_manager.model,
            status=stat if stat else None,
            recent_user=current_approval.first() if current_approval else None,
            payload=request_to_payload(self.request, self.data_copy),
            company=self.request.user.user_company,
            code=self.data_manager.code,
            method=self.method,
            creator=self.request.user,
            sub_task_uuid=self.sub_task_handler.uuid_code,
            bloc=self.bloc,
        )

        return model_object

    def read(self, pk=None):
        SerializerClass = self.MySerializerView(self.class_name)
        field_names = {f.name for f in self.class_name._meta.fields}
        has_code = "code" in field_names

        if pk:
            qs = self.class_name.objects.filter(pk=pk)
            if has_code:
                codes = self.rba.values_list("code", flat=True)
                qs = qs.filter(code__in=codes)

            instance = qs.first()

            if not instance:
                return Response({"error": "Not found"}, status=404)

            return Response(SerializerClass(instance).data, status=200)

        queryset = dynamic_queryset_filter(
            self.request.query_params,
            self.class_name.objects.all(),
            order_by=self.request.query_params.get("order_by"),
        )
        if has_code and not (
            self.request.user.position
            and self.request.user.position.position_code
            in CORE_USER_CODE + self.extra_position
        ):
            codes = self.rba.values_list("code", flat=True)

            if "creator" in self.field_names:
                employees = UserDatabase.objects.filter(
                    Q(manager=self.request.user) | Q(manager__manager=self.request.user)
                )
                queryset = queryset.filter(creator__in=employees)

            queryset = queryset.filter(code__in=codes)

        return queryset

    def update(self, pk):
        codes = self.rba.values_list("code", flat=True)
        field_names = {f.name for f in self.class_name._meta.fields}
        has_code = "code" in field_names

        if has_code and not (
            self.request.user.position
            and self.request.user.position.position_code
            in CORE_USER_CODE + self.extra_position
        ):
            instance = self.class_name.objects.filter(pk=pk, code__in=codes).first()
        else:
            instance = self.class_name.objects.filter(pk=pk).first()

        if not instance:
            return Response({"error": "Not found"}, status=404)

        if self.data_manager is not None and self.data_manager.update:
            SerializerClass = self.MySerializer(self.class_name)
            serializer = SerializerClass(instance, data=self.data_copy, partial=True)

            if not serializer.is_valid():
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            model_object = self.add_model_update_pipe(instance)
            model_object.save()
            return Response(
                {"message": "update sent for approval"}, status=status.HTTP_202_ACCEPTED
            )
        else:
            SerializerClass = self.MySerializer(self.class_name)
            serializer = SerializerClass(instance, data=self.data_copy, partial=True)
            serializer.is_valid(raise_exception=True)
            model_saved = serializer.save()
            self.sub_task_handler.bloc_run(self.bloc, {"model": model_saved})
            return Response(serializer.data, status=status.HTTP_200_OK)

    def add_model_update_pipe(self, instance):
        stat = ApprovalStatusDatabase.objects.filter(code="NEW").first()
        current_approval = ApprovalStack.objects.filter(
            code=self.data_manager.code, is_first=True
        )
        model_object = ApprovalProcess.objects.create(
            model_name=self.data_manager.model,
            recent_user=current_approval.first() if current_approval else None,
            payload=request_to_payload(self.request, self.data_copy),
            status=stat if stat else None,
            company=self.request.user.user_company,
            code=self.data_manager.code,
            method=self.method,
            update_id=instance.pk,
            creator=self.request.user,
            sub_task_uuid=self.sub_task_handler.uuid_code,
            bloc=self.bloc,
        )

        return model_object

    def delete(self, pk):
        codes = self.rba.values_list("code", flat=True)
        field_names = {f.name for f in self.class_name._meta.fields}
        has_code = "code" in field_names

        if has_code and not (
            self.request.user.position
            and self.request.user.position.position_code
            in CORE_USER_CODE + self.extra_position
        ):
            instance = self.class_name.objects.filter(pk=pk, code__in=codes).first()
        else:
            instance = self.class_name.objects.filter(pk=pk).first()
        if not instance:
            return Response({"error": "Not found"}, status=404)
        if self.data_manager is not None and self.data_manager.can_delete:
            self.delete_model_pipe(instance)
            return Response({"message": "delete request sent for approval"}, status=status.HTTP_202_ACCEPTED)
        else:
            self.sub_task_handler.bloc_run(self.bloc, {"model": instance})
            instance.delete()
            return Response(
                {"message": "Data has been deleted ! "}, status=status.HTTP_200_OK
            )

    def delete_model_pipe(self, instance):
        stat = ApprovalStatusDatabase.objects.filter(code="NEW").first()
        current_approval = ApprovalStack.objects.filter(
            code=self.data_manager.code, is_first=True
        )
        model_object = ApprovalProcess.objects.create(
            model_name=self.data_manager.model,
            status=stat if stat else None,
            recent_user=current_approval.first() if current_approval else None,
            payload=request_to_payload(self.request, self.data_copy),
            company=self.request.user.user_company,
            code=self.data_manager.code,
            method=self.method,
            update_id=instance.pk,
            creator=self.request.user,
            sub_task_uuid=self.sub_task_handler.uuid_code,
            bloc=self.bloc,
        )
        model_object.save()

    def MySerializer(self, model_class):
        return getDynamicSerializer(model_class)

    def MySerializerView(self, model_class):
        return getDynamicSerializerView(model_class)

    def save_to_shadow(self):
        payload = request_to_payload(self.request)

        with transaction.atomic():
            obj = ApprovalProcess.objects.create(
                model_name=ModelNameDatabase.objects.get(
                    model_name=self.class_name.__name__
                ),
                payload=payload,
                code=str(uuid.uuid4()),  #
            )

        return obj


class SUBTASKHANDLER:
    def __init__(self, uuid_code):
        self.uuid_code = uuid_code
        self.instances = self.get_sub_task()

    def get_sub_task(self):
        if self.uuid_code is not None:
            return SubTask.objects.filter(sub_task_uuid=self.uuid_code)
        else:
            return []

    def execute(self):
        for item in self.instances:
            if item.is_executed:
                continue

            try:
                if item.method == "POST":
                    model_class = self.instancesToClass(item)
                    SerializerClass = self.MySerializer(model_class)

                    serializer = SerializerClass(data=item.payload, partial=True)
                    serializer.is_valid(raise_exception=True)
                    serializer.save()

                elif item.method == "PUT" or item.method == "PATCH":
                    model_class = self.instancesToClass(item)
                    SerializerClass = self.MySerializer(model_class)
                    instance = model_class.objects.filter(pk=item.instance_id).first()
                    serializer = SerializerClass(
                        instance, data=item.payload, partial=True
                    )
                    serializer.is_valid(raise_exception=True)
                    serializer.save()

                elif item.method == "DELETE":
                    model_class = self.instancesToClass(item)
                    instance = model_class.objects.filter(pk=item.instance_id).first()
                    instance.delete()

                item.is_executed = True
                item.save()

            except Exception as ex:
                print(ex)

    def MySerializer(self, model_class):
        return getDynamicSerializer(model_class)

    def instancesToClass(self, instance):
        my_model = apps.get_model(instance.model.model_name, instance.model.model_app)
        return my_model

    def bloc_run(self, bloc, args=None):
        bloc_code = bloc
        if len(str(bloc)) < 1:
            return Response(
                {"error": "no Bloc found "}, status=status.HTTP_404_NOT_FOUND
            )

        my_function = BLOC_FUNCTIONS[bloc_code]
        if my_function is None:
            print("bloc function not found")
            return Response(
                {"error": "no Bloc function found "}, status=status.HTTP_404_NOT_FOUND
            )

        my_function(args)
