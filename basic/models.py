from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class StatusDatabase(models.Model):
    id = models.BigAutoField(primary_key=True)
    status = models.CharField(max_length=100)
    status_code = models.CharField(max_length=100, unique=True)
    status_description = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    creator = models.ForeignKey(
        "basic.UserDatabase", on_delete=models.SET_NULL, null=True, blank=True, related_name="creator_status_database"
    )
    company = models.ForeignKey(
        "basic.CompanyDatabase", on_delete=models.SET_NULL, null=True, blank=True, related_name="company_status_database"
    )
    
    def __str__(self):
        return self.status

    class Meta:
        verbose_name = "Status"
        verbose_name_plural = "Statuses"
        ordering = ["-created_at"]
        db_table = "status_database"
        
        
class StatusDatabaseUser(models.Model):
    id = models.BigAutoField(primary_key=True)
    status = models.CharField(max_length=100)
    status_code = models.CharField(max_length=100, unique=True)
    status_description = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey(
        "basic.UserDatabase", on_delete=models.SET_NULL, null=True, blank=True, related_name="creator_status_database_user"
    )
    company = models.ForeignKey(
        "basic.CompanyDatabase", on_delete=models.SET_NULL, null=True, blank=True, related_name="company_status_database_user"
    )
    
    def __str__(self):
        return self.status

    class Meta:
        verbose_name = "Status"
        verbose_name_plural = "Statuses"
        ordering = ["-created_at"]
        db_table = "status_database_user"
        

class BusinessArea(models.Model):
    id = models.BigAutoField(primary_key=True)
    business_area = models.CharField(max_length=100)
    business_area_code = models.CharField(max_length=100, unique=True)
    business_area_description = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey(
        "basic.UserDatabase", on_delete=models.SET_NULL, null=True, blank=True, related_name="business_area_creator"
    )
    company = models.ForeignKey(
        "basic.CompanyDatabase", on_delete=models.SET_NULL, null=True, blank=True, related_name="business_area_company"
    )
    
    def __str__(self):
        return self.business_area

    class Meta:
        verbose_name = "Business Area"
        verbose_name_plural = "Business Areas"
        ordering = ["-created_at"]
        db_table = "business_area"
        unique_together = ("business_area", "business_area_code")
        

class BusinessSector(models.Model):
    id = models.BigAutoField(primary_key=True)
    business_sector = models.CharField(max_length=100)
    business_sector_code = models.CharField(max_length=100, unique=True)
    business_sector_description = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    creator = models.ForeignKey(
        "basic.UserDatabase", on_delete=models.SET_NULL, null=True, blank=True, related_name="creator_business_sector"
    )
    company = models.ForeignKey(
        "basic.CompanyDatabase", on_delete=models.SET_NULL, null=True, blank=True, related_name="company_business_sector"
    )
    
    def __str__(self):
        return self.business_sector

    class Meta:
        verbose_name = "Business Sector"
        verbose_name_plural = "Business Sectors"
        ordering = ["-created_at"]
        db_table = "business_sector"
        unique_together = ("business_sector", "business_sector_code")


class CurrencyDatabase(models.Model):
    id = models.BigAutoField(primary_key=True)
    currency_name = models.CharField(max_length=100, unique=True)
    currency_code = models.CharField(max_length=100, unique=True)
    currency_symbol = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    creator = models.ForeignKey(
        "basic.UserDatabase", on_delete=models.SET_NULL, null=True, blank=True, related_name="creator_currency"
    )
    company = models.ForeignKey(
        "basic.CompanyDatabase", on_delete=models.SET_NULL, null=True, blank=True, related_name="company_currency"
    )
    
    def __str__(self):
        return self.currency_name

    class Meta:
        verbose_name = "Currency"
        verbose_name_plural = "Currencies"
        ordering = ["-created_at"]
        db_table = "currency_database"
        unique_together = ("currency_name", "currency_code")

class CountryDatabase(models.Model):
    id = models.BigAutoField(primary_key=True)
    country_name = models.CharField(max_length=100, unique=True)
    country_code = models.CharField(max_length=100, unique=True)
    country_mobile = models.CharField(max_length=100)
    country_logo = models.ImageField(upload_to="country_logos/", blank=True, null=True, default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    creator = models.ForeignKey(
        "basic.UserDatabase", on_delete=models.SET_NULL, null=True, blank=True, related_name="creator_country"
    )
    company = models.ForeignKey(
        "basic.CompanyDatabase", on_delete=models.SET_NULL, null=True, blank=True, related_name="company_country"
    )

    def __str__(self):
        return self.country_name
    
    class Meta:
        verbose_name = "Country"
        verbose_name_plural = "Countries"
        ordering = ["-created_at"]
        db_table = "country_database"
        
        
class StateDatabase(models.Model):
    id = models.BigAutoField(primary_key=True)
    state_name = models.CharField(max_length=100, unique=True)
    state_code = models.CharField(max_length=100, unique=True)
    state_country = models.ForeignKey("CountryDatabase", on_delete=models.SET_NULL, null=True, blank=True)
    state_logo = models.ImageField(upload_to="state_logos/", blank=True, null=True, default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey(
        "basic.UserDatabase", on_delete=models.SET_NULL, null=True, blank=True, related_name="creator_state"
    )
    company = models.ForeignKey(
        "basic.CompanyDatabase", on_delete=models.SET_NULL, null=True, blank=True, related_name="company_state"
    )

    def __str__(self):
        return self.state_name
    
    class Meta:
        verbose_name = "State"
        verbose_name_plural = "States"
        ordering = ["-created_at"]
        db_table = "state_database"
        

class CityDatabase(models.Model):
    id = models.BigAutoField(primary_key=True)
    city_name = models.CharField(max_length=100, unique=True)
    city_code = models.CharField(max_length=100, unique=True)
    city_state = models.ForeignKey("StateDatabase", on_delete=models.SET_NULL, null=True, blank=True)
    city_logo = models.ImageField(upload_to="city_logos/", blank=True, null=True, default=None)
    pin_code = models.CharField(max_length=100, null=True, blank=True)       
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    creator = models.ForeignKey(
        "basic.UserDatabase", on_delete=models.SET_NULL, null=True, blank=True, related_name="creator_city_db"
    )
    company = models.ForeignKey(
        "basic.CompanyDatabase", on_delete=models.SET_NULL, null=True, blank=True, related_name="company_city_db"
    )

    def __str__(self):
        return self.city_name
    
    class Meta:
        verbose_name = "City"
        verbose_name_plural = "Cities"
        ordering = ["-created_at"]
        db_table = "city_database"
        
        
class LanguageDatabase(models.Model):
    id = models.BigAutoField(primary_key=True)
    language_name = models.CharField(max_length=100, unique=True)
    language_code = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey(
        "basic.UserDatabase", on_delete=models.SET_NULL, null=True, blank=True, related_name="creator_lang"
    )
    company = models.ForeignKey(
        "basic.CompanyDatabase", on_delete=models.SET_NULL, null=True, blank=True, related_name="company_lang"
    )

    def __str__(self):
        return self.language_name
    
    class Meta:
        verbose_name = "Language"
        verbose_name_plural = "Languages"
        ordering = ["-created_at"]
        db_table = "language_database"




class CompanyDatabase(models.Model):
    id = models.BigAutoField(primary_key=True)
    organization_id = models.CharField(max_length=100,blank=True, null=True,unique=True)
    company_name = models.CharField(max_length=100, unique=True)
    company_code = models.CharField(max_length=100, unique=True)
    company_description = models.CharField(max_length=100,blank=True, null=True)
    parent_company = models.ForeignKey(
        "self",
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )
    company_logo = models.ImageField(upload_to="company_logos/", blank=True, null=True, default=None)
    company_admin = models.ForeignKey(
        "basic.UserDatabase",
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    currency = models.ForeignKey("CurrencyDatabase", on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.ForeignKey("StatusDatabase", on_delete=models.SET_NULL, null=True, blank=True)
    country = models.ForeignKey("CountryDatabase", on_delete=models.SET_NULL, null=True, blank=True)
    state = models.ForeignKey("StateDatabase", on_delete=models.SET_NULL, null=True, blank=True)
    city = models.ForeignKey("CityDatabase", on_delete=models.SET_NULL, null=True, blank=True)
    language = models.ForeignKey("LanguageDatabase", on_delete=models.SET_NULL, null=True, blank=True)
    business_area = models.ForeignKey("BusinessArea", on_delete=models.SET_NULL, null=True, blank=True) 
    business_sector = models.ForeignKey("BusinessSector", on_delete=models.SET_NULL, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.company_name
    
    
    class Meta:
        verbose_name = "Company"
        verbose_name_plural = "Companies"
        ordering = ["-created_at"]
        db_table = "company_database"
        unique_together = ("company_name", "company_code","organization_id","parent_company",)

class UserTypeDatabase(models.Model):
    id = models.BigAutoField(primary_key=True)
    type = models.CharField(max_length=100)
    type_code = models.CharField(max_length=100, unique=True)
    type_description = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.type
    
    
    class Meta:
        verbose_name = "User Type"
        verbose_name_plural = "User Types"
        ordering = ["-created_at"]
        db_table = "user_type_database"
        unique_together = ("type", "type_code")

class PositionDatabase(models.Model):
    id = models.BigAutoField(primary_key=True)
    position = models.CharField(max_length=100)
    position_code = models.CharField(max_length=100, unique=True)
    position_description = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.position
    
    
    class Meta:
        verbose_name = "Position"
        verbose_name_plural = "Positions"
        ordering = ["-created_at"]
        db_table = "position_database"
        unique_together = ("position", "position_code")


class UserDatabase(AbstractUser):
    user_photo = models.ImageField(
        upload_to="employee_photos/", blank=True, null=True, default=None
    )
    user_company = models.ForeignKey("CompanyDatabase", on_delete=models.SET_NULL, null=True, blank=True)
    user_type = models.ForeignKey("UserTypeDatabase", on_delete=models.SET_NULL, null=True, blank=True)
    user_code = models.CharField(max_length=100, unique=True)
    position = models.ForeignKey("PositionDatabase", on_delete=models.SET_NULL, null=True, blank=True)
    email = models.EmailField(unique=True)
    status = models.ForeignKey("StatusDatabaseUser", on_delete=models.SET_NULL, null=True, blank=True)
    phone_number = models.CharField(max_length=100, null=True, blank=True)
    
    last_login_ip = models.GenericIPAddressField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    device_id = models.CharField(max_length=255, null=True, blank=True)
    emergency_contact = models.CharField(max_length=255, null=True, blank=True)
    relationship_emergency_contact = models.CharField(max_length=255, null=True, blank=True)
    remarks = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.user_code)
    
    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
        ordering = ["-created_at"]
        db_table = "user_database"
        unique_together = ("username", "email")



class TempModel(models.Model):
    id = models.BigAutoField(primary_key=True)
    image = models.ImageField(upload_to="temp/", blank=True, null=True, default=None)
    file = models.FileField(upload_to="temp/", blank=True, null=True, default=None)
    test = models.CharField(max_length=100)
    boolean = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    class Meta:
        verbose_name = "Temp"
        verbose_name_plural = "Temps"
        ordering = ["-created_at"]
        db_table = "temp_model"
