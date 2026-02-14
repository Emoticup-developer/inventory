from django.shortcuts import render
from rest_framework.views import APIView
from ams.logic import DATAHANDLER
from vendor.models import KYCStatus, Quotation, Vendor, VendorDeclaration, VendorKYC, VendorMaterial, VendorType
from rest_framework.response import Response
# Create your views here.


class VendorTypeView(APIView):
    def get(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(
            request=request, class_name=VendorType, data_copy=data_copy
        )
        pipe_out = pipe.process(pk=pk)
        
        if isinstance(pipe_out, Response):
            return pipe_out
        
        instance = pipe_out
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
        pipe = DATAHANDLER(
            request=request, class_name=Vendor, data_copy=data_copy
        )
        pipe_out = pipe.process(pk=pk)
        
        if isinstance(pipe_out, Response):
            return pipe_out
        
        instance = pipe_out
        
        serializer_class = pipe.MySerializerView(pipe.class_name)
        
        return Response(serializer_class(instance, many=True).data, status=200)

    def post(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(request, Vendor, data_copy,bloc="vendor_created").process(pk=pk)
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
        pipe = DATAHANDLER(
            request=request, class_name=Quotation, data_copy=data_copy
        )
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
        pipe = DATAHANDLER(
            request=request, class_name=KYCStatus, data_copy=data_copy
        )
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
        pipe = DATAHANDLER(
            request=request, class_name=VendorKYC, data_copy=data_copy
        )
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
    
    