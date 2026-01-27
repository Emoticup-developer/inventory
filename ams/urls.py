from django.urls import path
from .views import *

urlpatterns = [
    path("login/", CustomLoginView.as_view(), name="login"),
    ##ModelNameDatabaseView
    path("model_name_database/", ModelNameDatabaseView.as_view(), name="model_name_database"),
    path("model_name_database/<pk>", ModelNameDatabaseView.as_view(), name="model_name_database"),
    
]
