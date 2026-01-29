from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from ams.logic import DATAHANDLER
from basic.models import CityDatabase, CompanyDatabase, CountryDatabase, CurrencyDatabase, LanguageDatabase, StateDatabase, StatusDatabase, StatusDatabaseUser, TempModel, UserDatabase, UserTypeDatabase

# Create your views here.

class StatusDatabaseView(APIView):
    def get(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(request= request, class_name=StatusDatabase,data_copy= data_copy).process(pk=pk)
        return pipe

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
        pipe = DATAHANDLER(request= request, class_name=StatusDatabaseUser,data_copy= data_copy).process(pk=pk)
        return pipe
    
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
        pipe = DATAHANDLER(request= request, class_name=CurrencyDatabase,data_copy= data_copy).process(pk=pk)
        return pipe
    
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
        pipe = DATAHANDLER(request= request, class_name=CountryDatabase,data_copy= data_copy).process(pk=pk)
        return pipe
    
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
        pipe = DATAHANDLER(request= request, class_name=StateDatabase,data_copy= data_copy).process(pk=pk)
        return pipe
    
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
        pipe = DATAHANDLER(request= request, class_name=CityDatabase,data_copy= data_copy).process(pk=pk)
        return pipe
    
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
        pipe = DATAHANDLER(request= request, class_name=LanguageDatabase,data_copy= data_copy).process(pk=pk)
        return pipe
    
    
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
        pipe = DATAHANDLER(request= request, class_name=CompanyDatabase,data_copy= data_copy).process(pk=pk)
        return pipe
    
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
        pipe = DATAHANDLER(request= request, class_name=UserTypeDatabase,data_copy= data_copy).process(pk=pk)
        return pipe
    
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
        pipe = DATAHANDLER(request= request, class_name=UserDatabase,data_copy= data_copy).process(pk=pk)
        return pipe
    
    def post(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(request, UserDatabase, data_copy).process(pk=pk)
        return pipe
    
    def put(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(request, UserDatabase, data_copy).process(pk=pk)
        return pipe
    
    def delete(self, request, pk=None):
        data_copy = request.data.copy()
        pipe = DATAHANDLER(request, UserDatabase, data_copy).process(pk=pk)
        return pipe
    
    