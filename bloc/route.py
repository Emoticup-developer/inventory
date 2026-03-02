from .vendor import *
from .movement import (
    material_movement,
    material_movement_tech,
    material_movement_tech_sl,
    material_movement_tech_tech,
    po_delivered,
    update_transaction_status,
)


BLOC_FUNCTIONS = {
    "vendor_created": VendorCreated,
    "material_movement": material_movement,
    "po_delivered": po_delivered,
    "material_movement_sl_tech": material_movement_tech,
    "material_movement_tech_tech": material_movement_tech_tech,
    "material_movement_tech_sl": material_movement_tech_sl,
    "update_transaction_status":update_transaction_status
}
