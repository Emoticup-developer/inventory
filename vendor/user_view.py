from rest_framework import serializers
from ams.logic import DATAHANDLER
from basic.models import UserDatabase
from vendor.models import Vendor, VendorType
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
        pipe = DATAHANDLER(request=request, class_name=Vendor, data_copy=data_copy)
        pipe_out = pipe.process(pk=pk)
        
        if isinstance(pipe_out, Response):
            return pipe_out
        
        instance = pipe_out.filter(vendor = Vendor.objects.filter(vendor_code = request.user.username).first())
        
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
        pipe.can_create = True
        pipe_out = pipe.process(pk=pk)
        
        if isinstance(pipe_out, Response):
            return pipe_out
        
        instance = pipe_out.filter(username = request.user.username)
        
        serializer_class = pipe.MySerializerView(pipe.class_name)
        
        return Response(serializer_class(instance, many=True).data, status=200)