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
        "basic.UserDatabase", on_delete=models.SET_NULL, null=True, blank=True, related_name="user_vendor_type"
    )
    company = models.ForeignKey(
        "basic.CompanyDatabase", on_delete=models.SET_NULL, null=True, blank=True, related_name="company_vendor_type"
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
        "VendorType",
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    contact_person = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=30, null=True, blank=True)
    mobile = models.CharField(max_length=30, null=True, blank=True)
    website = models.URLField(null=True, blank=True)

    billing_address = models.TextField(null=True, blank=True)
    shipping_address = models.TextField(null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    postal_code = models.CharField(max_length=20, null=True, blank=True)

    tax_id = models.CharField(max_length=50, null=True, blank=True)
    vat_number = models.CharField(max_length=50, null=True, blank=True)
    gst_number = models.CharField(max_length=50, null=True, blank=True)
    pan_number = models.CharField(max_length=50, null=True, blank=True)

    payment_terms = models.CharField(max_length=100, null=True, blank=True)
    credit_days = models.PositiveIntegerField(default=0)
    credit_limit = models.DecimalField(
        max_digits=14, decimal_places=2, default=0
    )
    currency = models.CharField(max_length=10, default="USD")

    bank_name = models.CharField(max_length=100, null=True, blank=True)
    bank_account_number = models.CharField(max_length=100, null=True, blank=True)
    bank_ifsc_swift = models.CharField(max_length=50, null=True, blank=True)
    bank_branch = models.CharField(max_length=100, null=True, blank=True)

    default_lead_time_days = models.PositiveIntegerField(default=0)
    minimum_order_value = models.DecimalField(
        max_digits=14, decimal_places=2, default=0
    )

    is_active = models.BooleanField(default=True)
    is_blacklisted = models.BooleanField(default=False)

    remarks = models.TextField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    creator = models.ForeignKey(
        "basic.UserDatabase", on_delete=models.SET_NULL, null=True, blank=True, related_name="user_vendor"
    )
    company = models.ForeignKey(
        "basic.CompanyDatabase", on_delete=models.SET_NULL, null=True, blank=True, related_name="company_vendor"
    )

    class Meta:
        db_table = "vendor"
        ordering = ["vendor_name"]

    def __str__(self):
        return f"{self.vendor_name} ({self.vendor_code})"




class VendorMaterial(models.Model):
    vendor = models.ForeignKey(
        "Vendor",
        on_delete=models.CASCADE,
        related_name="vendor_materials"
    )

    material = models.ForeignKey(
        "ims.Material",
        on_delete=models.CASCADE,
        related_name="vendor_materials"
    )

    purchase_uom = models.ForeignKey(
        "ims.UnitOfMeasure",
        on_delete=models.PROTECT
    )

    price = models.DecimalField(
        max_digits=14,
        decimal_places=4
    )

    minimum_order_quantity = models.DecimalField(
        max_digits=12,
        decimal_places=3,
        default=1
    )

    lead_time_days = models.PositiveIntegerField(default=0)

    tax_percentage = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=0
    )

    discount_percentage = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=0
    )

    is_preferred = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    valid_from = models.DateField(null=True, blank=True)
    valid_to = models.DateField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    creator = models.ForeignKey(
        "basic.UserDatabase", on_delete=models.SET_NULL, null=True, blank=True, related_name="user_vendor_material"
    )
    company = models.ForeignKey(
        "basic.CompanyDatabase", on_delete=models.SET_NULL, null=True, blank=True, related_name="company_vendor_material"
    )

    class Meta:
        db_table = "vendor_material"
        unique_together = ("vendor", "material", "purchase_uom")
        ordering = ["vendor", "material"]

    def __str__(self):
        return f"{self.vendor} → {self.material}"
