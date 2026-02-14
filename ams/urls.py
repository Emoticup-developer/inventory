from django.urls import path
from .views import *

urlpatterns = [
    path("login/", CustomLoginView.as_view(), name="login"),
    ##ModelNameDatabaseView
    path("model_name_database/", ModelNameDatabaseView.as_view(), name="model_name_database"),
    path("model_name_database/<pk>", ModelNameDatabaseView.as_view(), name="model_name_database"),
    ##PipelineApprove
    path("pipeline_approve/", PipelineApprove.as_view(), name="pipeline_approve"),
    path("pipeline_approve/<pk>", PipelineApprove.as_view(), name="pipeline_approve"),
    ##NavigationBoxView
    path("navigation_box/", NavigationBoxView.as_view(), name="navigation_box"),
    path("navigation_box/<pk>", NavigationBoxView.as_view(), name="navigation_box"),
    
]
