from django.urls import path
from .views import *

urlpatterns = [
    path("", ImsView.as_view(), name="ims"),
    ##UnitsView
    path("units/", UnitsView.as_view(), name="units"),
    path("units/<pk>", UnitsView.as_view(), name="units"),
    ##UnitOfMeasureView
    path("unit_of_measure/", UnitOfMeasureView.as_view(), name="unit_of_measure"),
    path("unit_of_measure/<pk>", UnitOfMeasureView.as_view(), name="unit_of_measure"),
    ##MaterialGroupView
    path("material_group/", MaterialGroupView.as_view(), name="material_group"),
    path("material_group/<pk>", MaterialGroupView.as_view(), name="material_group"),
    ##MaterialCategoryView
    path(
        "material_category/", MaterialCategoryView.as_view(), name="material_category"
    ),
    path(
        "material_category/<pk>",
        MaterialCategoryView.as_view(),
        name="material_category",
    ),
    ##MaterialTypeView
    path("material_type/", MaterialTypeView.as_view(), name="material_type"),
    path("material_type/<pk>", MaterialTypeView.as_view(), name="material_type"),
    ##MaterialView
    path("material/", MaterialView.as_view(), name="material"),
    path("material/<pk>", MaterialView.as_view(), name="material"),
    ##PlantTypeView
    path("plant_type/", PlantTypeView.as_view(), name="plant_type"),
    path("plant_type/<pk>", PlantTypeView.as_view(), name="plant_type"),
    ##PlantView
    path("plant/", PlantView.as_view(), name="plant"),
    path("plant/<pk>", PlantView.as_view(), name="plant"),
    ##WarehouseTypeView
    path("warehouse_type/", WarehouseTypeView.as_view(), name="warehouse_type"),
    path("warehouse_type/<pk>", WarehouseTypeView.as_view(), name="warehouse_type"),
    ##WarehouseView
    path("warehouse/", WarehouseView.as_view(), name="warehouse"),
    path("warehouse/<pk>", WarehouseView.as_view(), name="warehouse"),
    ##StorageLocationTypeView
    path(
        "storage_location_type/",
        StorageLocationTypeView.as_view(),
        name="storage_location_type",
    ),
    path(
        "storage_location_type/<pk>",
        StorageLocationTypeView.as_view(),
        name="storage_location_type",
    ),
    ##StorageLocationView
    path("storage_location/", StorageLocationView.as_view(), name="storage_location"),
    path(
        "storage_location/<pk>", StorageLocationView.as_view(), name="storage_location"
    ),
    ##MaterialMovementView
    path(
        "material_movement/", MaterialMovementView.as_view(), name="material_movement"
    ),
    path(
        "material_movement/<pk>",
        MaterialMovementView.as_view(),
        name="material_movement",
    ),
    ##TransactionStatusView
    path(
        "transaction_status/",
        TransactionStatusView.as_view(),
        name="transaction_status",
    ),
    path(
        "transaction_status/<pk>",
        TransactionStatusView.as_view(),
        name="transaction_status",
    ),
    ##TransactionView
    path("transaction/", TransactionView.as_view(), name="transaction"),
    path("transaction/<pk>", TransactionView.as_view(), name="transaction"),
    ##MaterialReportView
    path("material_report/", MaterialReportView.as_view(), name="material_report"),
    path("material_report/<pk>", MaterialReportView.as_view(), name="material_report"),
    ##PO_StatusView
    path("po_status/", PO_StatusView.as_view(), name="po_status"),
    path("po_status/<pk>", PO_StatusView.as_view(), name="po_status"),
    ##PurchaseOrderView
    path("purchase_order/", PurchaseOrderView.as_view(), name="purchase_order"),
    path("purchase_order/<pk>", PurchaseOrderView.as_view(), name="purchase_order"),
    ##PurchaseOrderItemView
    path(
        "purchase_order_item/",
        PurchaseOrderItemView.as_view(),
        name="purchase_order_item",
    ),
    path(
        "purchase_order_item/<pk>",
        PurchaseOrderItemView.as_view(),
        name="purchase_order_item",
    )
]
