from django.db import models
import uuid

class Units(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    base_quantity = models.DecimalField(max_digits=10, decimal_places=2)
    short_name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Units"
        verbose_name_plural = "Units"
        ordering = ["-created_at"]
        db_table = "units"
        unique_together = ("name", "code", "short_name")


class UnitOfMeasure(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    is_base_unit = models.BooleanField(default=False)
    category = models.ForeignKey(
        Units, on_delete=models.SET_NULL, null=True, blank=True
    )
    short_name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "UOM"
        verbose_name_plural = "UOMs"
        ordering = ["-created_at"]
        db_table = "uom"
        unique_together = ("name", "code", "short_name")


# Create your models here.
class MaterialGroup(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    short_name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Material Group"
        verbose_name_plural = "Material Groups"
        ordering = ["-created_at"]
        db_table = "material_group"
        unique_together = ("name", "code", "short_name")


class MaterialCategory(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    short_name = models.CharField(max_length=100)
    material_group = models.ForeignKey(
        "MaterialGroup", on_delete=models.SET_NULL, null=True, blank=True
    )
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Material Category"
        verbose_name_plural = "Material Categories"
        ordering = ["-created_at"]
        db_table = "material_category"
        unique_together = ("name", "code", "short_name")


class MaterialType(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    short_name = models.CharField(max_length=100)
    material_category = models.ForeignKey(
        "MaterialCategory", on_delete=models.SET_NULL, null=True, blank=True
    )
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Material Type"
        verbose_name_plural = "Material Types"
        ordering = ["-created_at"]
        db_table = "material_type"
        unique_together = ("name", "code", "short_name")


    class Material(models.Model):
        material_name = models.CharField(max_length=100)
        code = models.CharField(max_length=100)
        is_active = models.BooleanField(default=True)
        base_uom = models.ForeignKey(
            "UnitOfMeasure",
            on_delete=models.SET_NULL,
            null=True,
            blank=True,
            related_name="materials",
        )
        purchase_uom = models.ForeignKey(
            "UnitOfMeasure",
            on_delete=models.SET_NULL,
            null=True,
            blank=True,
            related_name="purchase_materials",
        )
        issue_uom = models.ForeignKey(
            "UnitOfMeasure",
            on_delete=models.SET_NULL,
            null=True,
            blank=True,
            related_name="issue_materials", 
        )
        weight = models.DecimalField(max_digits=10, decimal_places=2)
        volume = models.DecimalField(max_digits=10, decimal_places=2)

        short_name = models.CharField(max_length=100)
        material_type = models.ForeignKey(
            "MaterialType", on_delete=models.SET_NULL, null=True, blank=True
        )
        description = models.TextField(null=True, blank=True)
        
        ## settings
        re_order_level = models.DecimalField(max_digits=10, decimal_places=2)
        re_order_quantity = models.DecimalField(max_digits=10, decimal_places=2)
        
        ##expiry
        has_expiry = models.BooleanField(default=False)
        shelf_life = models.DecimalField(max_digits=10, decimal_places=2)
        
        qr_code = models.CharField(max_length=100, null=True, blank=True,unique=True)
        
        ##vendor details
        vendor = models.ForeignKey(
            "vendor.Vendor", on_delete=models.SET_NULL, null=True, blank=True,related_name="materials"
        )
        
        
        movement = models.JSONField(
            null=True, blank=True, default=list
        )
        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)

        def __str__(self):
            return self.material_name

        class Meta:
            verbose_name = "Material"
            verbose_name_plural = "Materials"
            ordering = ["-created_at"]
            db_table = "material"
            unique_together = ("material_name", "code", "short_name")

class PlantType(models.Model):
    name = models.CharField(max_length=100, unique=True)
    code = models.CharField(max_length=50, unique=True, db_index=True)
    short_name = models.CharField(max_length=50, null=True, blank=True)

    # Behavior flags: define what this plant type can do
    is_manufacturing = models.BooleanField(default=False)
    is_distribution = models.BooleanField(default=False)
    is_service = models.BooleanField(default=False)

    description = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    # Optional sorting for display in dropdowns/admin
    sort_order = models.PositiveIntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "plant_type"
        ordering = ["sort_order", "name"]

    def __str__(self):
        return f"{self.name} ({self.code})"


class Plant(models.Model):
    plant_name = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    company = models.ForeignKey(
        "basic.CompanyDatabase", on_delete=models.SET_NULL, null=True, blank=True   
    )
    plant_type = models.ForeignKey(
        "PlantType", on_delete=models.SET_NULL, null=True, blank=True
    )
    short_name = models.CharField(max_length=100)
    description = models.TextField( null=True, blank=True)
    is_operational = models.BooleanField(default=True)
    
    currency = models.ForeignKey(
        "basic.CurrencyDatabase", on_delete=models.SET_NULL, null=True, blank=True
    )
    ##address
    country = models.ForeignKey(
        "basic.CountryDatabase", on_delete=models.SET_NULL, null=True, blank=True
    )
    state = models.ForeignKey(
        "basic.StateDatabase", on_delete=models.SET_NULL, null=True, blank=True
    )
    city = models.ForeignKey(
        "basic.CityDatabase", on_delete=models.SET_NULL, null=True, blank=True
    )
    address_line1 = models.TextField(null=True, blank=True)
    address_line2 = models.TextField(null=True, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.plant_name

    class Meta:
        verbose_name = "Plant"
        verbose_name_plural = "Plants"
        ordering = ["-created_at"]
        db_table = "plant"
        unique_together = ("plant_name", "code", "short_name")
        
        
class WarehouseType(models.Model):
    name = models.CharField(max_length=100, unique=True)
    code = models.CharField(max_length=50, unique=True, db_index=True)

    is_raw_material = models.BooleanField(default=False)
    is_finished_goods = models.BooleanField(default=False)
    is_spare_parts = models.BooleanField(default=False)
    is_transit = models.BooleanField(default=False)

    description = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    sort_order = models.PositiveIntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "warehouse_type"
        ordering = ["sort_order", "name"]

    def __str__(self):
        return f"{self.name} ({self.code})"



class Warehouse(models.Model):
    warehouse_name = models.CharField(max_length=150)
    warehouse_code = models.CharField(max_length=50, unique=True, db_index=True)
    short_name = models.CharField(max_length=50, null=True, blank=True)

    plant = models.ForeignKey(
        "Plant",
        on_delete=models.PROTECT,
        related_name="warehouses"
    )

    warehouse_type = models.ForeignKey(
        "WarehouseType",
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    is_active = models.BooleanField(default=True)

    address_line1 = models.TextField(null=True, blank=True)
    address_line2 = models.TextField(null=True, blank=True)
    
    country = models.ForeignKey(
        "basic.CountryDatabase", on_delete=models.SET_NULL, null=True, blank=True
    )
    state = models.ForeignKey(
        "basic.StateDatabase", on_delete=models.SET_NULL, null=True, blank=True
    )
    city = models.ForeignKey(
        "basic.CityDatabase", on_delete=models.SET_NULL, null=True, blank=True
    )

    max_capacity = models.DecimalField(
        max_digits=12, decimal_places=3, null=True, blank=True
    )  # optional for capacity planning

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "warehouse"
        ordering = ["warehouse_name"]
        unique_together = ("warehouse_name", "warehouse_code", "short_name")

    def __str__(self):
        return f"{self.warehouse_name} ({self.warehouse_code})"




class StorageLocationType(models.Model):
    name = models.CharField(max_length=100, unique=True)
    code = models.CharField(max_length=50, unique=True, db_index=True)

    is_open = models.BooleanField(default=False)
    is_rack = models.BooleanField(default=False)
    is_cold_storage = models.BooleanField(default=False)
    is_hazardous = models.BooleanField(default=False)
    is_quarantine = models.BooleanField(default=False)

    description = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    sort_order = models.PositiveIntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "storage_location_type"
        ordering = ["sort_order", "name"]
        unique_together = ("name", "code")

    def __str__(self):
        return f"{self.name} ({self.code})"


class StorageLocation(models.Model):
    location_name = models.CharField(max_length=150)
    location_code = models.CharField(max_length=50)
    short_name = models.CharField(max_length=50, null=True, blank=True)

    warehouse = models.ForeignKey(
        "Warehouse",
        on_delete=models.PROTECT,
        related_name="storage_locations"
    )

    storage_type = models.ForeignKey(
        "StorageLocationType",
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    is_active = models.BooleanField(default=True)

    # Physical characteristics
    max_capacity = models.DecimalField(
        max_digits=12,
        decimal_places=3,
        null=True,
        blank=True
    )

    is_blocked = models.BooleanField(default=False)
    is_pickable = models.BooleanField(default=True)

    remarks = models.TextField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "storage_location"
        unique_together = ("warehouse", "location_code")
        ordering = ["location_name"]
        unique_together = ("location_name", "location_code", "short_name")

    def __str__(self):
        return f"{self.location_name} ({self.location_code})"



class MaterialMovement(models.Model):
    movement_name = models.CharField(max_length=100, unique=True)

    movement_code = models.CharField(max_length=50, unique=True, db_index=True)
    
    ##this indicate where materal from and to like it might wrehouse or store wherehouse as soem code and storeage 
    source_code = models.CharField(max_length=50, null=True, blank=True)
    destination_code = models.CharField(max_length=50, null=True, blank=True)
    
    description = models.TextField(null=True, blank=True)
    sort_order = models.PositiveIntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "material_movement"
        ordering = ["sort_order", "movement_name"]
        unique_together = ("movement_name", "movement_code")
        

    def __str__(self):
        return f"{self.movement_name} ({self.movement_code})"


class TransactionStatus(models.Model):
    status_name = models.CharField(max_length=100, unique=True)
    status_code = models.CharField(max_length=50, unique=True, db_index=True)
    description = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    sort_order = models.PositiveIntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "transaction_status"
        ordering = ["sort_order", "status_name"]
        unique_together = ("status_name", "status_code")

    def __str__(self):
        return f"{self.status_name} ({self.status_code})"




class Transaction(models.Model):
    transaction_code = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    transaction_name = models.CharField(max_length=100, unique=True)
    description = models.TextField(null=True, blank=True)
    
    movement = models.ForeignKey(
        "MaterialMovement",
        on_delete=models.PROTECT,  # PROTECT makes more sense
        null=False,
        blank=False
    )
    
    material = models.ForeignKey(
        "Material",
        on_delete=models.PROTECT,
        null=False,
        blank=False
    )
    
    source_code = models.CharField(max_length=20)
    destination_code = models.CharField(max_length=20)
    
    units_of_measure = models.ForeignKey(
        "UnitOfMeasure",
        on_delete=models.PROTECT,
        null=False,
        blank=False
    )
    volume = models.DecimalField(max_digits=14, decimal_places=3)
    
    created_by = models.ForeignKey(
        "basic.UserDatabase",
        on_delete=models.PROTECT
    )
    
    is_shipped = models.BooleanField(default=False)
    
    transaction_status = models.ForeignKey(
        "TransactionStatus",
        on_delete=models.PROTECT
    )
    
    history = models.JSONField(default=list, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "transaction"
        unique_together = ("transaction_name",)

    def __str__(self):
        return f"{self.transaction_name} ({self.transaction_code})"
    
    
    
class MaterialReport(models.Model):
    material = models.ForeignKey(
        "Material",
        on_delete=models.PROTECT
    )
    location_code = models.CharField(max_length=10)
    units_of_measure = models.ForeignKey(
        "UnitOfMeasure",
        on_delete=models.PROTECT
    )
    volume = models.DecimalField(max_digits=14, decimal_places=3)
    related_transaction = models.ForeignKey(
        "Transaction",
        on_delete=models.PROTECT
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "material_report"
        unique_together = ("material", "location_code", "units_of_measure")