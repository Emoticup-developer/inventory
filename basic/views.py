from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import make_password

from ams.logic import DATAHANDLER
from basic.models import BusinessArea, BusinessSector, CityDatabase, CompanyDatabase, CountryDatabase, CurrencyDatabase, LanguageDatabase, PositionDatabase, StateDatabase, StatusDatabase, StatusDatabaseUser, TempModel, UserDatabase, UserTypeDatabase

# Create your views here.

class StatusDatabaseView(APIView):
    def get(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(
            request=request, class_name=StatusDatabase, data_copy=data_copy
        )
        pipe_out = pipe.process(pk=pk)
        
        if isinstance(pipe_out, Response):
            return pipe_out
        
        instance = pipe_out
        serializer_class = pipe.MySerializerView(pipe.class_name)
        
        return Response(serializer_class(instance, many=True).data, status=200)

    def post(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(request, StatusDatabase, data_copy).process(pk=pk)
        return pipe
    
    def put(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(request, StatusDatabase, data_copy).process(pk=pk)
        return pipe
    
    def delete(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(request, StatusDatabase, data_copy).process(pk=pk)
        return pipe


class StatusDatabaseUserView(APIView):
    def get(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(
            request=request, class_name=StatusDatabaseUser, data_copy=data_copy
        )
        pipe_out = pipe.process(pk=pk)
        
        if isinstance(pipe_out, Response):
            return pipe_out
        
        instance = pipe_out
        serializer_class = pipe.MySerializerView(pipe.class_name)
        
        return Response(serializer_class(instance, many=True).data, status=200)
    
    def post(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(request, StatusDatabaseUser, data_copy).process(pk=pk)
        return pipe
    
    def put(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(request, StatusDatabaseUser, data_copy).process(pk=pk)
        return pipe
    
    def delete(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(request, StatusDatabaseUser, data_copy).process(pk=pk)
        return pipe


class CurrencyDatabaseView(APIView):
    def get(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(
            request=request, class_name=CurrencyDatabase, data_copy=data_copy
        )
        pipe_out = pipe.process(pk=pk)
        
        if isinstance(pipe_out, Response):
            return pipe_out
        
        instance = pipe_out
        serializer_class = pipe.MySerializerView(pipe.class_name)
        
        return Response(serializer_class(instance, many=True).data, status=200)
    
    def post(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(request, CurrencyDatabase, data_copy).process(pk=pk)
        return pipe
    
    def put(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(request, CurrencyDatabase, data_copy).process(pk=pk)
        return pipe
    
    def delete(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(request, CurrencyDatabase, data_copy).process(pk=pk)
        return pipe

class CountryDatabaseView(APIView):
    def get(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(
            request=request, class_name=CountryDatabase, data_copy=data_copy
        )
        pipe_out = pipe.process(pk=pk)
        
        if isinstance(pipe_out, Response):
            return pipe_out
        
        instance = pipe_out
        serializer_class = pipe.MySerializerView(pipe.class_name)
        
        return Response(serializer_class(instance, many=True).data, status=200)
    

    
    def post(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(request, CountryDatabase, data_copy).process(pk=pk)
        return pipe
    
    def put(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(request, CountryDatabase, data_copy).process(pk=pk)
        return pipe
    
    def delete(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(request, CountryDatabase, data_copy).process(pk=pk)
        return pipe



class StateDatabaseView(APIView):
    def get(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(
            request=request, class_name=StateDatabase, data_copy=data_copy
        )
        pipe_out = pipe.process(pk=pk)
        
        if isinstance(pipe_out, Response):
            return pipe_out
        
        instance = pipe_out
        serializer_class = pipe.MySerializerView(pipe.class_name)
        
        return Response(serializer_class(instance, many=True).data, status=200)
    
    def post(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(request, StateDatabase, data_copy).process(pk=pk)
        return pipe
    
    def put(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(request, StateDatabase, data_copy).process(pk=pk)
        return pipe
    
    def delete(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(request, StateDatabase, data_copy).process(pk=pk)
        return pipe
    

class CityDatabaseView(APIView):
    def get(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(
            request=request, class_name=CityDatabase, data_copy=data_copy
        )
        pipe_out = pipe.process(pk=pk)
        
        if isinstance(pipe_out, Response):
            return pipe_out
        
        instance = pipe_out
        serializer_class = pipe.MySerializerView(pipe.class_name)
        
        return Response(serializer_class(instance, many=True).data, status=200)
    
    def post(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(request, CityDatabase, data_copy).process(pk=pk)
        return pipe
    
    def put(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(request, CityDatabase, data_copy).process(pk=pk)
        return pipe
    
    def delete(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(request, CityDatabase, data_copy).process(pk=pk)
        return pipe
    
    
    
class LanguageDatabaseView(APIView):
    def get(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(
            request=request, class_name=LanguageDatabase, data_copy=data_copy
        )
        pipe_out = pipe.process(pk=pk)
        
        if isinstance(pipe_out, Response):
            return pipe_out
        
        instance = pipe_out
        serializer_class = pipe.MySerializerView(pipe.class_name)
        
        return Response(serializer_class(instance, many=True).data, status=200)
    
    
    def post(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(request, LanguageDatabase, data_copy).process(pk=pk)
        return pipe
    
    def put(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(request, LanguageDatabase, data_copy).process(pk=pk)
        return pipe
    
    def delete(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(request, LanguageDatabase, data_copy).process(pk=pk)
        return pipe
    
class CompanyDatabaseView(APIView):
    
    def get(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(
            request=request, class_name=CompanyDatabase, data_copy=data_copy
        )
        pipe_out = pipe.process(pk=pk)
        
        if isinstance(pipe_out, Response):
            return pipe_out
        
        instance = pipe_out
        serializer_class = pipe.MySerializerView(pipe.class_name)
        
        return Response(serializer_class(instance, many=True).data, status=200)
    
    def post(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(request, CompanyDatabase, data_copy).process(pk=pk)
        return pipe
    
    def put(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(request, CompanyDatabase, data_copy).process(pk=pk)
        return pipe
    
    def delete(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(request, CompanyDatabase, data_copy).process(pk=pk)
        return pipe
    
    
    
class UserTypeDatabaseView(APIView):
    def get(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(
            request=request, class_name=UserTypeDatabase, data_copy=data_copy
        )
        pipe_out = pipe.process(pk=pk)
        
        if isinstance(pipe_out, Response):
            return pipe_out
        
        instance = pipe_out
        serializer_class = pipe.MySerializerView(pipe.class_name)
        
        return Response(serializer_class(instance, many=True).data, status=200)
    
    def post(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(request, UserTypeDatabase, data_copy).process(pk=pk)
        return pipe
    
    def put(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(request, UserTypeDatabase, data_copy).process(pk=pk)
        return pipe
    
    def delete(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(request, UserTypeDatabase, data_copy).process(pk=pk)
        return pipe
    
class UserDatabaseView(APIView):
    def get(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(
            request=request, class_name=UserDatabase, data_copy=data_copy
        )
        pipe_out = pipe.process(pk=pk)
        
        if isinstance(pipe_out, Response):
            return pipe_out
        
        instance = pipe_out
        serializer_class = pipe.MySerializerView(pipe.class_name)
        
        return Response(serializer_class(instance, many=True).data, status=200)
    
    def post(self, request, pk=None):
        data_copy = request.data.copy()
        
        if "password" in data_copy.keys():
            data_copy["password"] = make_password(str(data_copy["password"]).strip())
            
        pipe = DATAHANDLER(request, UserDatabase, data_copy)
        pipe_out = pipe.process(pk=pk)
        return pipe_out
    
    def put(self, request, pk=None):
        data_copy = request.data.copy()
        
        if "password" in data_copy.keys():
            data_copy["password"] = make_password(str(data_copy["password"]).strip())
        
        pipe = DATAHANDLER(request, UserDatabase, data_copy).process(pk=pk)
        return pipe

    def delete(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(request, UserDatabase, data_copy).process(pk=pk)
        return pipe
    
class PositionDatabaseView(APIView):
    def get(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(
            request=request, class_name=PositionDatabase, data_copy=data_copy
        )
        pipe_out = pipe.process(pk=pk)
        
        if isinstance(pipe_out, Response):
            return pipe_out
        
        instance = pipe_out
        serializer_class = pipe.MySerializerView(pipe.class_name)
        
        return Response(serializer_class(instance, many=True).data, status=200)
    
    def post(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(request, PositionDatabase, data_copy).process(pk=pk)
        return pipe
    
    def put(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(request, PositionDatabase, data_copy).process(pk=pk)
        return pipe
    
    def delete(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(request, PositionDatabase, data_copy).process(pk=pk)
        return pipe
    
class BusinessAreaView(APIView):
    def get(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(
            request=request, class_name=BusinessArea, data_copy=data_copy
        )
        pipe_out = pipe.process(pk=pk)
        
        if isinstance(pipe_out, Response):
            return pipe_out
        
        instance = pipe_out
        serializer_class = pipe.MySerializerView(pipe.class_name)
        
        return Response(serializer_class(instance, many=True).data, status=200)
    
    def post(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(request, BusinessArea, data_copy).process(pk=pk)
        return pipe
    
    
    def put(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(request, BusinessArea, data_copy).process(pk=pk)
        return pipe
    
    
    def delete(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(request, BusinessArea, data_copy).process(pk=pk)
        return pipe
    
    
class BusinessSectorView(APIView):
    def get(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(
            request=request, class_name=BusinessSector, data_copy=data_copy
        )
        pipe_out = pipe.process(pk=pk)
        
        if isinstance(pipe_out, Response):
            return pipe_out
        
        instance = pipe_out
        serializer_class = pipe.MySerializerView(pipe.class_name)
        
        return Response(serializer_class(instance, many=True).data, status=200)
    
    def post(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(request, BusinessSector, data_copy).process(pk=pk)
        return pipe
    
    
    def put(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(request, BusinessSector, data_copy).process(pk=pk)
        return pipe
    
    
    def delete(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(request, BusinessSector, data_copy).process(pk=pk)
        return pipe