from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from ams.logic import DATAHANDLER
from basic.models import TempModel, UserDatabase
# Create your views here.




class UserAccounts(APIView):
    def get(self, request,pk=None):
        pipe = DATAHANDLER(request, UserDatabase).process(pk=pk)
        return pipe
    
    def post(self, request,pk=None):
        pipe = DATAHANDLER(request, UserDatabase).process(pk=pk)
        return pipe
    
    def put(self, request,pk=None):
        pipe = DATAHANDLER(request, UserDatabase).process(pk=pk)
        return pipe
    
    def delete(self, request,pk=None):
        pipe = DATAHANDLER(request, UserDatabase).process(pk=pk)
        return pipe
    
    
class TempModels(APIView):
    def get(self, request,pk=None):
        pipe = DATAHANDLER(request, TempModel).process(pk=pk)
        return pipe
    
    def post(self, request,pk=None):
        pipe = DATAHANDLER(request, TempModel).process(pk=pk)
        return pipe
    
    def put(self, request,pk=None):
        pipe = DATAHANDLER(request, TempModel).process(pk=pk)
        return pipe
    
    def delete(self, request,pk=None):
        pipe = DATAHANDLER(request, TempModel).process(pk=pk)
        return pipe