from basic.models import UserDatabase

from ims.models import (
    BagInventory,
    ConsumeAndScrap,
    Material,
    MaterialMovement,
    PO_Status,
    PurchaseOrder,
    PurchaseOrderItem,
    Stock,
    StorageLocation,
    Transaction,
    TransactionStatus,
)




def material_movement(context):
    try:
        model = context["model"]
        
        source = StorageLocation.objects.filter(location_code=model.source_code).first()
        
        destination = StorageLocation.objects.filter(
            location_code=model.destination_code
        ).first()
        
        material = Material.objects.filter(pk=model.material.pk).first()
        
        if not source or not destination or not material:
            print("Invalid source, destination, or material.")
            return
        
        source_stock = Stock.objects.filter(
            material=material, storage_location=source
        ).first()

        if not source_stock or source_stock.quantity < model.volume:
            print("Insufficient stock at source location.")
            return
        
        stock, created = Stock.objects.update_or_create(
            material=material,
            storage_location=destination,
            defaults={
                "base_uom": model.material.base_uom,
                "company": model.company,
                "creator": model.creator,
                "last_transaction": model,
            },
        )
        
        # IMPORTANT: increment quantity separately

        if (
            model.transaction_status
            and not model.transaction_status.status_code == "PENG"
            and model.transaction_status.status_code == "ACPT"
        ):
            stock.quantity = stock.quantity + model.volume
            stock.save(update_fields=["quantity"])
            # Decrement source stock
            source_stock.quantity = source_stock.quantity - model.volume
            source_stock.save(update_fields=["quantity"])
            
            model.transaction_status = TransactionStatus.objects.filter(
                status_code="CM"
            ).first()
            
            model.save(update_fields=["transaction_status"])
        else:
            print("Transaction is not in a valid state for processing.")
            
    except Exception as ex:
        model = context["model"]
        model.transaction_status = TransactionStatus.objects.filter(
            status_code="ER"
        ).first()
        model.save(update_fields=["transaction_status"])



from django.db import transaction
from django.db.models import F


def po_delivered(context):
    try:
        model = context["model"]

        if model.status.status_code != "DELIVERED":
            return

        with transaction.atomic():
            po_items = PurchaseOrderItem.objects.select_related("material").filter(
                purchase_order=model
            )

            for item in po_items:

                if not item.material:
                    continue
                
                mm = MaterialMovement.objects.filter(
                    movement_code="SL2V", company=model.company
                ).first()
                
                transactions = Transaction.objects.create(
                    movement=mm,
                    transaction_name=f"{model.po_number} - {item.material} - Returned",
                    description=f"{model.po_number} - {item.material} - Returned from {model.storage_location.location_code} ",
                    material=item.material,
                    source_code=model.vendor.vendor_code,
                    destination_code=model.storage_location.location_code,
                    units_of_measure=item.material.base_uom,
                    volume=item.received_quantity,
                    transaction_status=TransactionStatus.objects.get(status_code="CM"),
                    is_shipped=True,
                    created_by=model.creator,
                )
                stock, created = Stock.objects.update_or_create(
                    material=item.material,
                    storage_location=model.storage_location,
                    defaults={
                        "base_uom": item.material.base_uom,
                        "company": model.company,
                        "creator": model.creator,
                        "last_transaction": transactions,
                    },
                )
                
                # IMPORTANT: increment quantity separately
                data = Stock.objects.filter(pk=stock.pk).first()
                data.quantity = data.quantity + item.received_quantity
                data.save(update_fields=["quantity"])
                
    except Exception as ex:
        print(ex)


def po_returned(context):
    try:
        model = context["model"]

        if model.status.status_code != "RETURNED":
            return

        with transaction.atomic():
            po_items = PurchaseOrderItem.objects.select_related("material").filter(
                purchase_order=model
            )

            for item in po_items:

                if not item.material:
                    continue

                mm = MaterialMovement.objects.filter(
                    movement_code="SL2V", company=model.company
                ).first()

                transactions = Transaction.objects.create(
                    movement=mm,
                    transaction_name=f"{model.po_number} - {item.material} - Returned",
                    description=f"{model.po_number} - {item.material} - Returned from {model.storage_location.location_code} to {model.vendor.vendor_code}",
                    material=item.material,
                    source_code=model.storage_location.location_code,
                    destination_code=model.vendor.vendor_code,
                    units_of_measure=item.material.base_uom,
                    volume=item.received_quantity,
                    transaction_status=TransactionStatus.objects.get(status_code="CM"),
                    is_shipped=True,
                    created_by=model.creator,
                )

                stock, created = Stock.objects.update_or_create(
                    material=item.material,
                    storage_location=model.storage_location,
                    defaults={
                        "base_uom": item.material.base_uom,
                        "company": model.company,
                        "creator": model.creator,
                        "last_transaction": transactions,
                    },
                )

                # IMPORTANT: decrement quantity separately
                data = Stock.objects.filter(pk=stock.pk).first()
                data.quantity = max(data.quantity - item.received_quantity, 0)
                data.save(update_fields=["quantity"])

    except Exception as ex:
        print(ex)
        
        
def material_movement_tech(context):
    try:
        model = context["model"]
        source = StorageLocation.objects.filter(location_code=model.source_code).first()
        destination = UserDatabase.objects.filter(
            user_code=model.destination_code
        ).first()

        material = Material.objects.filter(pk=model.material.pk).first()

        if not source or not destination or not material:
            return

        source_stock = Stock.objects.filter(
            material=material, storage_location=source
        ).first()

        if not source_stock or source_stock.quantity < model.volume:
            print("Insufficient stock at source location.")
            return

        stock, created = BagInventory.objects.update_or_create(
            material=material,
            user=destination,
            defaults={
                "uom": model.material.base_uom,
                "company": model.company,
                "creator": model.creator,
                "related_transaction": model,
            },
        )

        if (
            model.transaction_status
            and not model.transaction_status.status_code == "PENG"
            and model.transaction_status.status_code == "ACPT"
        ):
            # IMPORTANT: increment quantity separately
            stock.volume = stock.volume + model.volume
            stock.save(update_fields=["volume"])

            # Decrement source stock
            source_stock.quantity = source_stock.quantity - model.volume
            source_stock.save(update_fields=["quantity"])

            model.transaction_status = TransactionStatus.objects.filter(
                status_code="CM"
            ).first()
            model.save(update_fields=["transaction_status"])
        else:
            print("Transaction is not in a valid state for processing.")
    except Exception as ex:
        model = context["model"]
        model.transaction_status = TransactionStatus.objects.filter(
            status_code="ER"
        ).first()
        model.save(update_fields=["transaction_status"])
        print(ex)

def material_movement_tech_tech(context):
    try:
        model = context["model"]
        source = UserDatabase.objects.filter(user_code=model.source_code).first()
        destination = UserDatabase.objects.filter(
            user_code=model.destination_code
        ).first()

        material = Material.objects.filter(pk=model.material.pk).first()

        if not source or not destination or not material:
            return

        source_stock = BagInventory.objects.filter(
            material=material, user=source
        ).first()

        if not source_stock or source_stock.volume < model.volume:
            print("Insufficient stock at source location.")
            return

        stock, created = BagInventory.objects.update_or_create(
            material=material,
            user=destination,
            defaults={
                "uom": model.material.base_uom,
                "company": model.company,
                "creator": model.creator,
                "related_transaction": model,
            },
        )

        if (
            model.transaction_status
            and not model.transaction_status.status_code == "PENG"
            and model.transaction_status.status_code == "ACPT"
        ):
            # IMPORTANT: increment quantity separately
            stock.volume = stock.volume + model.volume
            stock.save(update_fields=["volume"])

            # Decrement source stock
            source_stock.volume = source_stock.volume - model.volume
            source_stock.save(update_fields=["volume"])

            model.transaction_status = TransactionStatus.objects.filter(
                status_code="CM"
            ).first()
            model.save(update_fields=["transaction_status"])
        else:
            print("Transaction is not in a valid state for processing.")

    except Exception as ex:
        model = context["model"]
        model.transaction_status = TransactionStatus.objects.filter(
            status_code="ER"
        ).first()
        model.save(update_fields=["transaction_status"])
        print(ex)


def material_movement_tech_sl(context):
    try:
        model = context["model"]
        destination = StorageLocation.objects.filter(
            location_code=model.destination_code
        ).first()
        source = UserDatabase.objects.filter(user_code=model.source_code).first()

        material = Material.objects.filter(pk=model.material.pk).first()

        if not source or not destination or not material:
            print("Invalid source, destination, or material.")
            return

        source_stock = BagInventory.objects.filter(
            material=material, user=source
        ).first()

        if not source_stock or source_stock.volume < model.volume:
            print("Insufficient stock at source location.")
            return

        stock, created = BagInventory.objects.update_or_create(
            material=material,
            user=destination,
            defaults={
                "uom": model.material.base_uom,
                "company": model.company,
                "creator": model.creator,
                "related_transaction": model,
            },
        )

        if (
            model.transaction_status
            and not model.transaction_status.status_code == "PENG"
            and model.transaction_status.status_code == "ACPT"
        ):
            # IMPORTANT: increment quantity separately
            stock.volume = stock.volume + model.volume
            stock.save(update_fields=["volume"])

            # Decrement source stock
            source_stock.volume = source_stock.volume - model.volume
            source_stock.save(update_fields=["volume"])

            model.transaction_status = TransactionStatus.objects.filter(
                status_code="CM"
            ).first()
            model.save(update_fields=["transaction_status"])
        else:
            print("Transaction is not in a valid state for processing.")

    except Exception as ex:
        model = context["model"]
        model.transaction_status = TransactionStatus.objects.filter(
            status_code="ER"
        ).first()
        model.save(update_fields=["transaction_status"])





def SLToScrapOrConsume(context):
    model = context["model"]
    
    storage_location = StorageLocation.objects.filter(
        location_code=model.source_code
    ).first()

    material = Material.objects.filter(pk=model.material.pk).first()
    
    stock = Stock.objects.filter(material=material, storage_location=storage_location).first()
    if not storage_location or not material:
        print("Invalid source, destination, or material.")
        return

    stock_data , created = ConsumeAndScrap.objects.update_or_create(
        material=material,
        transaction=model,
        volume=model.volume,
        created_at=model.created_at,
        company=model.company,
        creator=model.creator,
    )
    stock.quantity = stock.quantity - model.volume
    stock.save(update_fields=["quantity"])
    
    model.transaction_status = TransactionStatus.objects.filter(
        status_code="CM"
    ).first()
    
    model.save(update_fields=["transaction_status"])
    



def update_transaction_status(context):
    model = context["model"]

    if model.transaction_status and model.transaction_status.status_code == "RLBK":
        
        model.transaction_status = TransactionStatus.objects.filter(
            status_code="CN"
        ).first()

        movement = model.movement and model.movement.status_code

        if movement == "TECH2SL":
            source = BagInventory.objects.filter(
                user=UserDatabase.objects.filter(user_code=model.source_code).first(),
                material=model.material,
            ).first()
            stock = Stock.objects.filter(
                material=model.material,
                storage_location=StorageLocation.objects.filter(
                    location_code=model.destination_code
                ).first(),
            ).first()
            source.volume = source.volume + model.volume
            source.save(update_fields=["volume"])

            stock.quantity = stock.quantity - model.volume
            stock.save(update_fields=["quantity"])
            model.save(update_fields=["transaction_status"])

        elif movement == "TECH2TECH":
            source = BagInventory.objects.filter(
                user=UserDatabase.objects.filter(user_code=model.source_code).first(),
                material=model.material,
            ).first()
            destination = BagInventory.objects.filter(
                user=UserDatabase.objects.filter(
                    user_code=model.destination_code
                ).first(),
                material=model.material,
            ).first()
            source.volume = source.volume + model.volume
            source.save(update_fields=["volume"])

            destination.volume = destination.volume - model.volume
            destination.save(update_fields=["volume"])
            model.save(update_fields=["transaction_status"])

        elif movement == "SL2TECH":
            source = Stock.objects.filter(
                material=model.material,
                storage_location=StorageLocation.objects.filter(
                    location_code=model.source_code
                ).first(),
            ).first()

            destination = BagInventory.objects.filter(
                user=UserDatabase.objects.filter(
                    user_code=model.destination_code
                ).first(),
                material=model.material,
            ).first()

            source.quantity = source.quantity + model.volume
            source.save(update_fields=["quantity"])

            destination.volume = destination.volume - model.volume
            destination.save(update_fields=["volume"])

            model.save(update_fields=["transaction_status"])

        elif movement == "S2S" or movement == "S2VL" or movement == "VL2SL":
            source = Stock.objects.filter(
                material=model.material,
                storage_location=StorageLocation.objects.filter(
                    location_code=model.source_code
                ).first(),
            ).first()

            destination = Stock.objects.filter(
                material=model.material,
                storage_location=StorageLocation.objects.filter(
                    location_code=model.destination_code
                ).first(),
            ).first()

            source.quantity = source.quantity + model.volume
            source.save(update_fields=["quantity"])

            destination.quantity = destination.quantity - model.volume
            destination.save(update_fields=["quantity"])

            model.save(update_fields=["transaction_status"])
            
        elif movement == "S2CONS" or movement == "S2SCRP":
            source = Stock.objects.filter(
                last_transaction__transaction_code=model.transaction_code
            ).first()

            destination = ConsumeAndScrap.objects.filter(
                transaction__transaction_code=model.transaction_code
            ).first()

            source.quantity = source.quantity + model.volume
            source.save(update_fields=["quantity"])

            destination.volume = destination.volume - model.volume
            destination.save(update_fields=["volume"])
            destination.is_scrap = True if movement == "S2SCRP" else False

            model.save(update_fields=["transaction_status"])
            
        elif movement == "CONS2S" or movement == "SCRP2S":
            source = ConsumeAndScrap.objects.filter(
                transaction__transaction_code=model.transaction_code
            ).first()

            destination = Stock.objects.filter(
                last_transaction__transaction_code=model.transaction_code
            ).first()

            source.volume = source.volume + model.volume
            source.save(update_fields=["volume"])
            source.is_scrap = True 
            source.transaction = model
            
            
            destination.quantity = destination.quantity - model.volume
            destination.save(update_fields=["quantity"])
            destination.last_transaction = model
            

            model.save(update_fields=["transaction_status"])
        elif movement == "SL2V":
            source = Stock.objects.filter(
                transaction__transaction_code=model.transaction_code
            ).first()
            po = PurchaseOrder.objects.filter(
                storage_location=source.storage_location
            ).first()

            source.quantity = source.quantity - model.volume
            source.save(update_fields=["quantity"])
            po.is_released = False
            po.save(update_fields=["is_released"])
            po.status = PO_Status.objects.filter(
                status_code="RTN"
            ).first()
            po.save(update_fields=["status"])
            
        elif movement == "V2SL":
            source = Stock.objects.filter(
                transaction__transaction_code=model.transaction_code
            ).first()
            po = PurchaseOrder.objects.filter(
                storage_location=source.storage_location
            ).first()

            source.quantity = source.quantity + model.volume
            source.save(update_fields=["quantity"])
            po.is_released = False
            
            po.save(update_fields=["is_released"])
            po.status = PO_Status.objects.filter(
                status_code="RTN"
            ).first()
            
            po.save(update_fields=["status"])
