from rest_framework import serializers
from django.db.models import Q, Model
from django.core.exceptions import FieldError
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


from django.core.files.storage import default_storage
from rest_framework.request import Request
from django.core.files.uploadedfile import UploadedFile
import uuid

from ams.models import AccessGroupDatabase, AccessGroupUserDatabase, ApprovalProcess, ApprovalStack, ModelNameDatabase
import uuid
from django.core.files.storage import default_storage
from django.core.files.uploadedfile import UploadedFile
from rest_framework.request import Request
from django.db import transaction
import uuid


def request_to_payload(request: Request) -> dict:
    payload = {}

    # 1. Handle normal fields
    for key, value in request.data.items():
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
    def __init__(self, request, class_name):
        self.request = request
        self.method = request.method
        self.data = request.data
        self.class_name = class_name
        self.approval_stack = self.check_model_author()
        

    def check_model_author(self):
        if not self.request.user.is_authenticated:
            return Response(
                {"error": "Unauthorized"}, status=status.HTTP_401_UNAUTHORIZED
            )
        else:
            
            model = ModelNameDatabase.objects.filter(
                model_name=self.class_name.__name__
            ).first()
            group = AccessGroupDatabase.objects.filter(model=model)
            permission = AccessGroupUserDatabase.objects.filter(
                access_group=group, user=self.request.user
            )
        
    # def permission_check(self):
    #     if not self.approval_stack:
    #         return Response(
    #             {"error": "Unauthorized"}, status=status.HTTP_401_UNAUTHORIZED
    #         )
    #     else:
    #         return True

    def process(self, pk=None):
        try:
            if self.method == "POST":
                return self.create()
            elif self.method == "GET":
                if pk:
                    return self.read(pk)
                return self.read()
            elif self.method == "PUT" or self.method == "PATCH":
                if pk:
                    return self.update(pk)
                else:
                    return Response(
                        {"error": "Invalid request"}, status=status.HTTP_400_BAD_REQUEST
                    )
            elif self.method == "DELETE":
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
        SerializerClass = self.MySerializer(self.class_name)
        serializer = SerializerClass(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)

    def read(self, pk=None):
        SerializerClass = self.MySerializerView(self.class_name)

        if pk:
            instance = self.class_name.objects.filter(pk=pk).first()
            if not instance:
                return Response({"error": "Not found"}, status=404)
            return Response(SerializerClass(instance).data)

        queryset = dynamic_queryset_filter(
            self.request.query_params,
            self.class_name.objects.all(),
            order_by=self.request.query_params.get("order_by"),
        )

        return Response(SerializerClass(queryset, many=True).data)

    def update(self, pk):
        instance = self.class_name.objects.filter(pk=pk).first()
        if not instance:
            return Response({"error": "Not found"}, status=404)

        SerializerClass = self.MySerializer(self.class_name)
        serializer = SerializerClass(instance, data=self.request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=200)

    def delete(self, pk):
        instance = self.class_name.objects.filter(pk=pk).first()
        if not instance:
            return Response({"error": "Not found"}, status=404)
        instance.delete()
        return Response({"message": "Deleted"}, status=204)

    def MySerializer(self, model_class):
        return getDynamicSerializer(model_class)

    def MySerializerView(self, model_class):
        return getDynamicSerializerView(model_class)

    def save_to_shadow(self):
        payload = request_to_payload(self.request)

        print("PAYLOAD >>>", payload)

        with transaction.atomic():
            obj = ApprovalProcess.objects.create(
                model_name=ModelNameDatabase.objects.get(
                    model_name=self.class_name.__name__
                ),
                payload=payload,
                code=str(uuid.uuid4()),  # IMPORTANT
            )

        return obj
