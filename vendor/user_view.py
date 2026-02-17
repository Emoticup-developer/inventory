from rest_framework import serializers
from ams.logic import DATAHANDLER
from ims.models import PurchaseOrder, Transaction
from basic.models import UserDatabase
from vendor.models import Quotation, Vendor, VendorDeclaration, VendorKYC, VendorMaterial, VendorType
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.contrib.auth.hashers import make_password


class VendorAccount(APIView):
    
    def get(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(
            request=request, class_name=UserDatabase, data_copy=data_copy
        )
        pipe.can_read = True
        
        pipe_out = pipe.process(pk=pk)
        
        if isinstance(pipe_out, Response):
            return pipe_out
        
        instance = pipe_out.filter(username = request.user.username)
        
        serializer_class = pipe.MySerializerView(pipe.class_name)
        
        return Response(serializer_class(instance, many=True).data, status=200)
    
    def put(self, request, pk=None):
        data_copy = request.data.copy()
        if "new_password" in data_copy.keys():
            old_password = data_copy["old_password"]
            user = UserDatabase.objects.filter(username = request.user.username).first()
            if not user.check_password(old_password):
                return Response({"error": "Old password is not correct"}, status=status.HTTP_400_BAD_REQUEST)
            
            data_copy["password"] = make_password(str(data_copy["new_password"]).strip())
            
        pipe = DATAHANDLER(request, UserDatabase, data_copy)
        pipe.can_update = True
        pipe_out = pipe.process(pk=pk)
        return pipe_out
    
    


class VendorQuotation(APIView):
    def get(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(request=request, class_name=Quotation, data_copy=data_copy)
        pipe_out = pipe.process(pk=pk)
        
        if isinstance(pipe_out, Response):
            return pipe_out
        
        instance = pipe_out.filter(vendor = Vendor.objects.filter(vendor_code = request.user.username).first())
        
        serializer_class = pipe.MySerializerView(pipe.class_name)
        
        return Response(serializer_class(instance, many=True).data, status=200)
    
    
    def put(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(request=request, class_name=Quotation, data_copy=data_copy)
        pipe_out = pipe.process(pk=pk)
        
        if isinstance(pipe_out, Response):
            return pipe_out
        
        instance = pipe_out.filter(username = request.user.username)
        
        serializer_class = pipe.MySerializerView(pipe.class_name)
        
        return Response(serializer_class(instance, many=True).data, status=200)
    
    
    def post(self, request, pk=None):
        data_copy = request.data.copy()
        if "quotation_number" not in data_copy.keys():
            id = Quotation.objects.order_by("-created_at").first()
            if id is None:
                data_copy["quotation_number"] = "1"
            else:
                data_copy["quotation_number"] = f"Q{id.id +1}"
            
        if "vendor" not in data_copy.keys():
            vendor = Vendor.objects.filter(vendor_code = request.user.username).first()   
            if vendor is None:
                return Response({"error": "Vendor not found"}, status=status.HTTP_400_BAD_REQUEST)
            
            data_copy["vendor"] =  vendor.pk
        
        pipe = DATAHANDLER(request=request, class_name=Quotation, data_copy=data_copy)
        pipe.can_create = True
        pipe_out = pipe.process(pk=pk)
        
        if isinstance(pipe_out, Response):
            return pipe_out
        
        instance = pipe_out.filter(username = request.user.username)
        
        serializer_class = pipe.MySerializerView(pipe.class_name)
        
        return Response(serializer_class(instance, many=True).data, status=200)
    
class VendorAccountData(APIView):
    def get(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(request=request, class_name=Vendor, data_copy=data_copy)
        pipe_out = pipe.process(pk=pk)
        
        if isinstance(pipe_out, Response):
            return pipe_out
        
        instance = pipe_out.filter(vendor_code = request.user.username)
        
        serializer_class = pipe.MySerializerView(pipe.class_name)
        
        return Response(serializer_class(instance, many=True).data, status=200)
    
        
    def put(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(request=request, class_name=Vendor, data_copy=data_copy)
        pipe_out = pipe.process(pk=pk)
        
        if isinstance(pipe_out, Response):
            return pipe_out
        
        instance = pipe_out.filter(username = request.user.username)
        
        serializer_class = pipe.MySerializerView(pipe.class_name)
        
        return Response(serializer_class(instance, many=True).data, status=200)
    
        
    def post(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(request=request, class_name=Vendor, data_copy=data_copy)
        pipe_out = pipe.process(pk=pk)
        
        if isinstance(pipe_out, Response):
            return pipe_out
        
        instance = pipe_out.filter(username = request.user.username)
        
        serializer_class = pipe.MySerializerView(pipe.class_name)
        
        return Response(serializer_class(instance, many=True).data, status=200)
    
        
    def delete(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(request=request, class_name=Vendor, data_copy=data_copy)
        pipe_out = pipe.process(pk=pk)
        
        if isinstance(pipe_out, Response):
            return pipe_out
        
        instance = pipe_out.filter(username = request.user.username)
        
        serializer_class = pipe.MySerializerView(pipe.class_name)
        
        return Response(serializer_class(instance, many=True).data, status=200)


class VendorDeclarationVendor(APIView):
    def get(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(request=request, class_name=VendorDeclaration, data_copy=data_copy)
        pipe_out = pipe.process(pk=pk)
        
        if isinstance(pipe_out, Response):
            return pipe_out
        
        instance = pipe_out.filter(vendor = Vendor.objects.filter(vendor_code = request.user.username).first())
        
        serializer_class = pipe.MySerializerView(pipe.class_name)
        
        return Response(serializer_class(instance, many=True).data, status=200)
    
    
    def post(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(request=request, class_name=VendorDeclaration, data_copy=data_copy)
        pipe_out = pipe.process(pk=pk)
        
        if isinstance(pipe_out, Response):
            return pipe_out
        
        instance = pipe_out.filter(vendor = Vendor.objects.filter(vendor_code = request.user.username).first())
        
        serializer_class = pipe.MySerializerView(pipe.class_name)
        
        return Response(serializer_class(instance, many=True).data, status=200)
    
    
    
    def put(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(request=request, class_name=VendorDeclaration, data_copy=data_copy)
        pipe_out = pipe.process(pk=pk)
        
        if isinstance(pipe_out, Response):
            return pipe_out
        
        instance = pipe_out.filter(vendor = Vendor.objects.filter(vendor_code = request.user.username).first())
        
        serializer_class = pipe.MySerializerView(pipe.class_name)
        
        return Response(serializer_class(instance, many=True).data, status=200)
    
    
    def delete(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(request=request, class_name=VendorDeclaration, data_copy=data_copy)
        pipe_out = pipe.process(pk=pk)
        
        if isinstance(pipe_out, Response):
            return pipe_out
        
        instance = pipe_out.filter(vendor = Vendor.objects.filter(vendor_code = request.user.username).first())
        
        serializer_class = pipe.MySerializerView(pipe.class_name)
        
        return Response(serializer_class(instance, many=True).data, status=200)
    
    
class VendorKYCVendor(APIView):
    def get(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(request=request, class_name=VendorKYC, data_copy=data_copy)
        pipe_out = pipe.process(pk=pk)
        
        if isinstance(pipe_out, Response):
            return pipe_out
        
        instance = pipe_out.filter(vendor = Vendor.objects.filter(vendor_code = request.user.username).first())
        
        serializer_class = pipe.MySerializerView(pipe.class_name)
        
        return Response(serializer_class(instance, many=True).data, status=200)
    
    
class VendorMaterialVendor(APIView):
    def get(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(request=request, class_name=VendorMaterial, data_copy=data_copy)
        pipe_out = pipe.process(pk=pk)
        
        if isinstance(pipe_out, Response):
            return pipe_out
        
        instance = pipe_out.filter(vendor = Vendor.objects.filter(vendor_code = request.user.username).first())
        
        serializer_class = pipe.MySerializerView(pipe.class_name)
        
        return Response(serializer_class(instance, many=True).data, status=200)
    
    
class TransactionVendor(APIView):
    def get(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(request=request, class_name=Transaction, data_copy=data_copy)
        pipe_out = pipe.process(pk=pk)
        
        if isinstance(pipe_out, Response):
            return pipe_out
        
        instance = pipe_out.filter(viewer = request.user)
        
        serializer_class = pipe.MySerializerView(pipe.class_name)
        
        return Response(serializer_class(instance, many=True).data, status=200)
    
    
    
class PurchaseOrderVendor(APIView):
    def get(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(request=request, class_name=PurchaseOrder, data_copy=data_copy)
        pipe_out = pipe.process(pk=pk)
        
        if isinstance(pipe_out, Response):
            return pipe_out
        
        instance = pipe_out.filter(viewer = request.user)
        
        serializer_class = pipe.MySerializerView(pipe.class_name)
        
        return Response(serializer_class(instance, many=True).data, status=200)