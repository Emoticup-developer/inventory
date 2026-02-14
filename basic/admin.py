from django.contrib import admin

from basic.models import CityDatabase, CompanyDatabase, CountryDatabase, LanguageDatabase, StateDatabase, StatusDatabase, StatusDatabaseUser, TempModel, UserDatabase, UserTypeDatabase
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import PositionDatabase, UserDatabase

# Register your models here.
admin.site.register(TempModel)
admin.site.register(StatusDatabase)
admin.site.register(StatusDatabaseUser)
admin.site.register(CountryDatabase)
admin.site.register(StateDatabase)
admin.site.register(CityDatabase)
admin.site.register(LanguageDatabase)
admin.site.register(CompanyDatabase)
admin.site.register(UserTypeDatabase)
admin.site.register(PositionDatabase)






@admin.register(UserDatabase)
class UserDatabaseAdmin(UserAdmin):
    model = UserDatabase

    fieldsets = UserAdmin.fieldsets + (
        ("Additional Info", {
            "fields": (
                "user_photo",
                "user_company",
                "user_type",
                "user_code",
                "status",
                "phone_number",
                "position",
                "manager"
            )
        }),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Additional Info", {
            "fields": (
                "user_photo",
                "user_company",
                "user_type",
                "user_code",
                "status",
                "phone_number",
                "email",
            )
        }),
    )

    list_display = (
        "username",
        "email",
        "user_code",
        "user_company",
        "is_staff",
        "is_active",
    )

    search_fields = ("username", "email", "user_code")
