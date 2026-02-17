from django.db import models

# Create your models here.


class VendorType(models.Model):
    name = models.CharField(max_length=100, unique=True)
    code = models.CharField(max_length=50, unique=True, db_index=True)
    short_name = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)

    # Behavior flags
    is_service_provider = models.BooleanField(default=False)
    is_material_supplier = models.BooleanField(default=True)
    requires_contract = models.BooleanField(default=False)

    # Control
    is_active = models.BooleanField(default=True)
    sort_order = models.PositiveIntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey(
        "basic.UserDatabase",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="user_vendor_type",
    )
    company = models.ForeignKey(
        "basic.CompanyDatabase",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="company_vendor_type",
    )

    class Meta:
        db_table = "vendor_type"
        ordering = ["sort_order", "name"]
        verbose_name = "Vendor Type"
        verbose_name_plural = "Vendor Types"

    def __str__(self):
        return f"{self.name} ({self.code})"


class Vendor(models.Model):
    vendor_name = models.CharField(max_length=150)
    vendor_code = models.CharField(max_length=50, unique=True, db_index=True)
    short_name = models.CharField(max_length=50)
    vendor_type = models.ForeignKey(
        "VendorType", on_delete=models.SET_NULL, null=True, blank=True
    )
    contact_person = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=30, null=True, blank=True)
    mobile = models.CharField(max_length=30, null=True, blank=True)
    website = models.URLField(null=True, blank=True)

    billing_address = models.TextField(null=True, blank=True)
    shipping_address = models.TextField(null=True, blank=True)
    country = models.ForeignKey(
        "basic.CountryDatabase", on_delete=models.SET_NULL, null=True, blank=True
    )
    state = models.ForeignKey(
        "basic.StateDatabase", on_delete=models.SET_NULL, null=True, blank=True
    )
    city = models.ForeignKey(
        "basic.CityDatabase", on_delete=models.SET_NULL, null=True, blank=True
    )
    
    postal_code = models.CharField(max_length=20, null=True, blank=True)

    currency = models.ForeignKey(
        "basic.CurrencyDatabase", on_delete=models.SET_NULL, null=True, blank=True
    )

    default_lead_time_days = models.PositiveIntegerField(default=0)
    minimum_order_value = models.DecimalField(
        max_digits=14, decimal_places=2, default=0
    )
    
    is_general = models.BooleanField(default=True,null=True,blank=True)
    is_active = models.BooleanField(default=True)
    is_blacklisted = models.BooleanField(default=False)
    is_approved_by_cfo = models.BooleanField(default=False)
    is_validated = models.BooleanField(default=False)

    remarks = models.TextField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    creator = models.ForeignKey(
        "basic.UserDatabase",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="user_vendor",
    )
    company = models.ForeignKey(
        "basic.CompanyDatabase",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="company_vendor",
    )

    class Meta:
        db_table = "vendor"
        ordering = ["vendor_name"]

    def __str__(self):
        return f"{self.vendor_name} ({self.vendor_code})"


class VendorDeclaration(models.Model):
    vendor = models.OneToOneField(Vendor, on_delete=models.CASCADE)
    declared_by_name = models.CharField(max_length=150)
    declared_by_designation = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    declaration_date = models.DateField()
    signature = models.FileField(upload_to="vendor/declarations/")
    accepted = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    company = models.ForeignKey(
        "basic.CompanyDatabase", on_delete=models.SET_NULL, null=True, blank=True
    )
    creator = models.ForeignKey(
        "basic.UserDatabase", on_delete=models.SET_NULL, null=True, blank=True
    )

    class Meta:
        db_table = "vendor_declaration"
        ordering = [
            "vendor",
        ]

    def __str__(self):
        return f"{self.vendor} - {self.declared_by_name}"


class Quotation(models.Model):
    vendor = models.ForeignKey(
        "Vendor", on_delete=models.CASCADE, related_name="vendor_quotations"
    )

    quotation_number = models.CharField(max_length=100,unique=True)
    quotation = models.FileField(upload_to="quotations/")
    date_of_quotation = models.DateField(auto_now_add=True)

    quantity = models.DecimalField(max_digits=12, decimal_places=3,blank=True,null=True)

    lead_time_days = models.PositiveIntegerField(default=0)
    is_validated = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    company = models.ForeignKey(
        "basic.CompanyDatabase", on_delete=models.SET_NULL, null=True, blank=True
    )
    creator = models.ForeignKey(
        "basic.UserDatabase", on_delete=models.SET_NULL, null=True, blank=True
    )

    class Meta:
        db_table = "vendor_quotation"
        ordering = [
            "vendor",
        ]

    def __str__(self):
        return f"{self.vendor} - {self.quotation_number}"


class VendorMaterial(models.Model):
    vendor = models.ForeignKey(
        "Vendor", on_delete=models.CASCADE, related_name="vendor_materials"
    )

    material = models.ForeignKey(
        "ims.Material", on_delete=models.CASCADE, related_name="vendor_materials"
    )

    purchase_uom = models.ForeignKey("ims.UnitOfMeasure", on_delete=models.PROTECT)

    price = models.DecimalField(max_digits=14, decimal_places=4)

    minimum_order_quantity = models.DecimalField(
        max_digits=12, decimal_places=3, default=1
    )

    lead_time_days = models.PositiveIntegerField(default=0)

    tax_percentage = models.DecimalField(max_digits=5, decimal_places=2, default=0)

    discount_percentage = models.DecimalField(max_digits=5, decimal_places=2, default=0)

    is_preferred = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    valid_from = models.DateField(null=True, blank=True)
    valid_to = models.DateField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    creator = models.ForeignKey(
        "basic.UserDatabase",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="user_vendor_material",
    )
    company = models.ForeignKey(
        "basic.CompanyDatabase",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="company_vendor_material",
    )

    class Meta:
        db_table = "vendor_material"
        unique_together = ("vendor", "material", "purchase_uom")
        ordering = ["vendor", "material"]

    def __str__(self):
        return f"{self.vendor} → {self.material}"


class KYCStatus(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    creator = models.ForeignKey(
        "basic.UserDatabase",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="user_kyc_status",
    )
    company = models.ForeignKey(
        "basic.CompanyDatabase",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="company_kyc_status",
    )

    class Meta:
        db_table = "kyc_status"
        ordering = ["name"]

    def __str__(self):
        return self.name


class VendorKYC(models.Model):
    vendor = models.OneToOneField(
        "vendor.Vendor", on_delete=models.CASCADE, related_name="kyc"
    )
    payment_terms = models.CharField(max_length=100, null=True, blank=True)
    credit_days = models.PositiveIntegerField(default=0)
    credit_limit = models.DecimalField(max_digits=14, decimal_places=2, default=0)
    # Basic identity
    legal_name = models.CharField(max_length=200)
    trade_name = models.CharField(max_length=200, null=True, blank=True)
    vendor_type = models.ForeignKey(
        "vendor.VendorType", on_delete=models.SET_NULL, null=True, blank=True
    )
    registration_number = models.CharField(max_length=100)
    incorporation_date = models.DateField(null=True, blank=True)
    country_of_registration = models.ForeignKey(
        "basic.CountryDatabase", on_delete=models.SET_NULL, null=True, blank=True
    )

    # Tax details
    tax_id = models.CharField(max_length=100)
    tax_certificate = models.FileField(
        upload_to="vendor_kyc/tax/", null=True, blank=True
    )
    is_msme = models.BooleanField(default=False)
    msme_certificate = models.FileField(
        upload_to="vendor_kyc/msme/", null=True, blank=True
    )

    # Banking details
    bank_name = models.CharField(max_length=150)
    account_holder_name = models.CharField(max_length=150)
    account_number = models.CharField(max_length=50)
    ifsc_swift_code = models.CharField(max_length=20)
    bank_branch = models.CharField(max_length=100, null=True, blank=True)
    bank_proof = models.FileField(upload_to="vendor_kyc/bank/", null=True, blank=True)

    # Address & contact
    registered_address = models.TextField()
    operational_address = models.TextField(null=True, blank=True)
    official_email = models.EmailField()
    phone_number = models.CharField(max_length=20)

    # Authorized signatory
    signatory_name = models.CharField(max_length=150)
    signatory_designation = models.CharField(max_length=100)
    signatory_email = models.EmailField()
    signatory_phone = models.CharField(max_length=20)

    # Compliance & risk
    nda_signed = models.BooleanField(default=False)
    contract_signed = models.BooleanField(default=False)
    is_blacklisted = models.BooleanField(default=False)
    risk_rating = models.CharField(max_length=20, null=True, blank=True)

    kyc_status = models.ForeignKey(
        "KYCStatus", on_delete=models.SET_NULL, null=True, blank=True
    )
    approved_at = models.DateTimeField(null=True, blank=True)
    approved_by = models.ForeignKey(
        "basic.UserDatabase",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="approved_vendor_kyc",
    )
    tax_id = models.CharField(max_length=50, null=True, blank=True)
    vat_number = models.CharField(max_length=50, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    creator = models.ForeignKey(
        "basic.UserDatabase",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="creator_vendor_kyc",
    )
    company = models.ForeignKey(
        "basic.CompanyDatabase",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="company_vendor_kyc",
    )

    class Meta:
        db_table = "vendor_kyc"
        verbose_name = "Vendor KYC"
        verbose_name_plural = "Vendor KYCs"

    def __str__(self):
        return f"KYC - {self.legal_name}"
