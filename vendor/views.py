from django.shortcuts import render
from rest_framework.views import APIView
from ams.logic import DATAHANDLER
from basic.models import UserDatabase, UserTypeDatabase
from bloc.email_notification import send_custom_email
from bloc.helper import generate_password
from vendor.models import (
    KYCStatus,
    Quotation,
    Vendor,
    VendorDeclaration,
    VendorKYC,
    VendorMaterial,
    VendorType,
)
from rest_framework.response import Response
from django.db.models import Max

from django.db.models import Q
# Create your views here.


class VendorTypeView(APIView):
    def get(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(request=request, class_name=VendorType, data_copy=data_copy)
        pipe.can_read = True
        
        pipe_out = pipe.process(pk=pk)

        if isinstance(pipe_out, Response):
            return pipe_out

        instance = pipe_out
        print(instance)
        serializer_class = pipe.MySerializerView(pipe.class_name)

        return Response(serializer_class(instance, many=True).data, status=200)

    def post(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(request, VendorType, data_copy)
        pipe.can_create = True
        output = pipe.process(pk=pk)

        return output

    def put(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(request, VendorType, data_copy).process(pk=pk)
        return pipe

    def delete(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(request, VendorType, data_copy).process(pk=pk)
        return pipe


class VendorView(APIView):
    def get(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(request=request, class_name=Vendor, data_copy=data_copy)
        pipe_out = pipe.process(pk=pk)

        if isinstance(pipe_out, Response):
            return pipe_out

        instance = pipe_out

        serializer_class = pipe.MySerializerView(pipe.class_name)

        return Response(serializer_class(instance, many=True).data, status=200)

    def post(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(request, Vendor, data_copy, bloc="vendor_created").process(
            pk=pk
        )
        return pipe

    def put(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(request, Vendor, data_copy).process(pk=pk)
        return pipe

    def delete(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(request, Vendor, data_copy).process(pk=pk)
        return pipe


class VendorMaterialView(APIView):
    def get(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(
            request=request, class_name=VendorMaterial, data_copy=data_copy
        )
        pipe_out = pipe.process(pk=pk)

        if isinstance(pipe_out, Response):
            return pipe_out

        instance = pipe_out
        serializer_class = pipe.MySerializerView(pipe.class_name)

        return Response(serializer_class(instance, many=True).data, status=200)

    def post(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(request, VendorMaterial, data_copy).process(pk=pk)
        return pipe

    def put(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(request, VendorMaterial, data_copy).process(pk=pk)
        return pipe

    def delete(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(request, VendorMaterial, data_copy).process(pk=pk)
        return pipe


class VendorDeclarationView(APIView):
    def get(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(
            request=request, class_name=VendorDeclaration, data_copy=data_copy
        )
        pipe_out = pipe.process(pk=pk)

        if isinstance(pipe_out, Response):
            return pipe_out

        instance = pipe_out
        serializer_class = pipe.MySerializerView(pipe.class_name)

        return Response(serializer_class(instance, many=True).data, status=200)

    def post(self, request, pk=None):
        data_copy = request.data.copy()
        print("Data copy in put method:", data_copy)  # Debugging statement

        pipe = DATAHANDLER(request, VendorDeclaration, data_copy).process(pk=pk)
        return pipe

    def put(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(request, VendorDeclaration, data_copy).process(pk=pk)
        return pipe

    def delete(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(request, VendorDeclaration, data_copy).process(pk=pk)
        return pipe


class QuotationView(APIView):
    def get(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(request=request, class_name=Quotation, data_copy=data_copy)
        pipe.can_read = True
        pipe_out = pipe.process(pk=pk)

        if isinstance(pipe_out, Response):
            return pipe_out

        instance = pipe_out
        serializer_class = pipe.MySerializerView(pipe.class_name)

        return Response(serializer_class(instance, many=True).data, status=200)

    def post(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(request, Quotation, data_copy).process(pk=pk)
        return pipe

    def put(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(request, Quotation, data_copy).process(pk=pk)
        return pipe

    def delete(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(request, Quotation, data_copy).process(pk=pk)
        return pipe


class KYCStatusView(APIView):
    def get(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(request=request, class_name=KYCStatus, data_copy=data_copy)
        pipe_out = pipe.process(pk=pk)

        if isinstance(pipe_out, Response):
            return pipe_out

        instance = pipe_out
        serializer_class = pipe.MySerializerView(pipe.class_name)

        return Response(serializer_class(instance, many=True).data, status=200)

    def post(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(request, KYCStatus, data_copy).process(pk=pk)
        return pipe

    def put(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(request, KYCStatus, data_copy).process(pk=pk)
        return pipe

    def delete(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(request, KYCStatus, data_copy).process(pk=pk)
        return pipe


class VendorKYCView(APIView):
    def get(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(request=request, class_name=VendorKYC, data_copy=data_copy)
        pipe_out = pipe.process(pk=pk)

        if isinstance(pipe_out, Response):
            return pipe_out

        instance = pipe_out
        serializer_class = pipe.MySerializerView(pipe.class_name)

        return Response(serializer_class(instance, many=True).data, status=200)

    def post(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(request, VendorKYC, data_copy).process(pk=pk)
        return pipe

    def put(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(request, VendorKYC, data_copy).process(pk=pk)
        return pipe

    def delete(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(request, VendorKYC, data_copy).process(pk=pk)
        return pipe


class SendLinkToVendor(APIView):
    def post(self, request):
        partner = request.data.get("partner")
        representative = request.data.get("representative")
        email = request.data.get("email")
        password = generate_password(length=12, use_symbols=True)
        code = self.generate_vendor_code()
        print(code)
        user = UserDatabase.objects.create_user(
            username=str(partner).strip().lower(),
            password=password,
            email=email,
            user_code = code,
            user_type=UserTypeDatabase.objects.filter(type_code="VENDOR").first(),
            is_active=True,
        )
        if user:
            user.save()
        else:
            return Response({"message": "user not created"}, status=400)
        
        send_custom_email(
            to_email=[email],
            subject="Greetings from KCBPL Procurement Team ",
            template_name="vendor/form_link.html",
            context={
                "partner": partner,
                "username": user.username,
                "representative": representative,
                "email": email,
                "password": password,
                "link": request.build_absolute_uri("/login/"),
            },
        )
        return Response({"message": "email sent"}, status=200)





    def generate_vendor_code(self):
        last_user = (
            UserDatabase.objects
            .filter(user_type__type_code="VENDOR", user_code__startswith="VEN")
            .order_by("-user_code")
            .first()
        )

        if not last_user:
            return "VEN0001"

        last_code = last_user.user_code

        try:
            last_number = int(last_code.replace("VEN", ""))
        except ValueError:
            last_number = 0

        return f"VEN{last_number + 1:04d}"