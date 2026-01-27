from django.urls import path
from .views import *

urlpatterns = [
    path("user_accounts/", UserAccounts.as_view(), name="user_accounts"),
    
    
    ##TempModels
    path("temp_models/", TempModels.as_view(), name="temp_models"),
    path("temp_models/<pk>", TempModels.as_view(), name="temp_models"),
]
