from django.urls import path
from .views import *

urlpatterns = [
    ##StatusDatabaseView
    path("company_status/", StatusDatabaseView.as_view(), name="company_status"),
    path("company_status/<pk>", StatusDatabaseView.as_view(), name="company_status"),
    ##StatusDatabaseUserView
    path("user_status/", StatusDatabaseUserView.as_view(), name="user_status"),
    path("user_status/<pk>", StatusDatabaseUserView.as_view(), name="user_status"),
    ##CountryDatabaseView
    path("country/", CountryDatabaseView.as_view(), name="country"),
    path("country/<pk>", CountryDatabaseView.as_view(), name="country"),
    ##StateDatabaseView
    path("state/", StateDatabaseView.as_view(), name="state"),
    path("state/<pk>", StateDatabaseView.as_view(), name="state"),
    ##CityDatabaseView
    path("city/", CityDatabaseView.as_view(), name="city"),
    path("city/<pk>", CityDatabaseView.as_view(), name="city"),
    ##LanguageDatabaseView
    path("language/", LanguageDatabaseView.as_view(), name="language"),
    path("language/<pk>", LanguageDatabaseView.as_view(), name="language"),
    ##CompanyDatabaseView
    path("company/", CompanyDatabaseView.as_view(), name="company"),
    path("company/<pk>", CompanyDatabaseView.as_view(), name="company"),
    ##UserTypeDatabaseView
    path("user_type/", UserTypeDatabaseView.as_view(), name="user_type"),
    path("user_type/<pk>", UserTypeDatabaseView.as_view(), name="user_type"),
    ##UserDatabaseView
    path("user/", UserDatabaseView.as_view(), name="user"),
    path("user/<pk>", UserDatabaseView.as_view(), name="user"),
    ##CurrencyDatabaseView
    path("currency/", CurrencyDatabaseView.as_view(), name="currency"),
    path("currency/<pk>", CurrencyDatabaseView.as_view(), name="currency"),
    ##PositionDatabaseView
    path("position/", PositionDatabaseView.as_view(), name="position"),
    path("position/<pk>", PositionDatabaseView.as_view(), name="position"),
    ##BusinessAreaView
    path("business_area/", BusinessAreaView.as_view(), name="business_area"),
    path("business_area/<pk>", BusinessAreaView.as_view(), name="business_area"),
    
    ##BusinessSectorView
    path("business_sector/", BusinessSectorView.as_view(), name="business_sector"),
    path("business_sector/<pk>", BusinessSectorView.as_view(), name="business_sector"),
]
