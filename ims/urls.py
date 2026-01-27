from django.urls import path
from .views import *

urlpatterns = [
    path("", ImsView.as_view(), name="ims"),
]
