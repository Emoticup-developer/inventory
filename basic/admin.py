from django.contrib import admin

from basic.models import CityDatabase, CompanyDatabase, CountryDatabase, LanguageDatabase, StateDatabase, StatusDatabase, StatusDatabaseUser, TempModel, UserDatabase, UserTypeDatabase

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
admin.site.register(UserDatabase)
