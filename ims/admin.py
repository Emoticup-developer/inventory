from django.contrib import admin

from ims.models import (
    BagInventory,
    ConsumeAndScrap,
    Material,
    MaterialCategory,
    MaterialGroup,
    MaterialMovement,
    MaterialType,
    PO_Status,
    Plant,
    PlantType,
    PurchaseOrder,
    PurchaseOrderItem,
    Stock,
    StorageLocation,
    StorageLocationType,
    Transaction,
    TransactionStatus,
    UnitOfMeasure,
    Units,
    Warehouse,
    WarehouseType,
)

# Register your models here.
admin.site.register(Units)
admin.site.register(UnitOfMeasure)
admin.site.register(MaterialGroup)
admin.site.register(MaterialCategory)
admin.site.register(MaterialType)
admin.site.register(Material)
admin.site.register(PlantType)
admin.site.register(Plant)
admin.site.register(WarehouseType)
admin.site.register(Warehouse)
admin.site.register(StorageLocationType)
admin.site.register(StorageLocation)
admin.site.register(MaterialMovement)
admin.site.register(TransactionStatus)
admin.site.register(Transaction)
admin.site.register(PO_Status)
admin.site.register(PurchaseOrder)
admin.site.register(PurchaseOrderItem)
admin.site.register(Stock)
admin.site.register(BagInventory)
admin.site.register(ConsumeAndScrap)
