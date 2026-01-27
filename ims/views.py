from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Create your views here.


class ImsView(APIView):
    def get(self, request):
        return Response({"status": "success"}, status=status.HTTP_200_OK)