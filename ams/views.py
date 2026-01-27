from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate

from ams.logic import DATAHANDLER
from ams.models import ModelNameDatabase



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

    def get(self, request,pk=None):
        pipe = DATAHANDLER(request, ModelNameDatabase).process(pk=pk)
        return pipe
    
    def post(self, request,pk=None):
        pipe = DATAHANDLER(request, ModelNameDatabase).process(pk=pk)
        return pipe
    
    def put(self, request,pk=None):
        pipe = DATAHANDLER(request, ModelNameDatabase).process(pk=pk)
        return pipe
    
    def delete(self, request,pk=None):
        pipe = DATAHANDLER(request, ModelNameDatabase).process(pk=pk)
        return pipe