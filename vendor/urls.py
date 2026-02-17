from django.urls import path
from .views import *
from .user_view import PurchaseOrderVendor, TransactionVendor, VendorAccount, VendorAccountData, VendorDeclarationVendor, VendorKYCVendor, VendorMaterialVendor,VendorQuotation

urlpatterns = [
    ##VendorTypeView
    path("vendor_type/", VendorTypeView.as_view(), name="vendor_type"),
    path("vendor_type/<pk>", VendorTypeView.as_view(), name="vendor_type"),
    ##VendorView
    path("vendor/", VendorView.as_view(), name="vendor"),
    path("vendor/<pk>", VendorView.as_view(), name="vendor"),
    ##VendorMaterialView
    path("vendor_material/", VendorMaterialView.as_view(), name="vendor_material"),
    path("vendor_material/<pk>", VendorMaterialView.as_view(), name="vendor_material"),
    ##VendorDeclarationView
    path("vendor_declaration/", VendorDeclarationView.as_view(), name="vendor_declaration"),
    path("vendor_declaration/<pk>", VendorDeclarationView.as_view(), name="vendor_declaration"),
    ##QuotationView
    path("quotation/", QuotationView.as_view(), name="quotation"),
    path("quotation/<pk>", QuotationView.as_view(), name="quotation"),
    ##KYCStatusView
    path("kyc_status/", KYCStatusView.as_view(), name="kyc_status"),
    path("kyc_status/<pk>", KYCStatusView.as_view(), name="kyc_status"),
    ##VendorKYCView
    path("vendor_kyc/", VendorKYCView.as_view(), name="vendor_kyc"),
    path("vendor_kyc/<pk>", VendorKYCView.as_view(), name="vendor_kyc"),
    
    
    ##Here only add vendor app related api
    ##VendorAccount
    path("vendor_account/", VendorAccount.as_view(), name="vendor_account"),
    path("vendor_account/<pk>", VendorAccount.as_view(), name="vendor_account"),
    ##VendorQuotation
    path("vendor_quotation/", VendorQuotation.as_view(), name="vendor_quotation"),
    path("vendor_quotation/<pk>", VendorQuotation.as_view(), name="vendor_quotation"),
    ##VendorAccountData
    path("vendor_account_data/", VendorAccountData.as_view(), name="vendor_account_data"),
    path("vendor_account_data/<pk>", VendorAccountData.as_view(), name="vendor_account_data"),
    ##VendorDeclarationVendor
    path("vendor_declaration_vendor/", VendorDeclarationVendor.as_view(), name="vendor_declaration_vendor"),
    path("vendor_declaration_vendor/<pk>", VendorDeclarationVendor.as_view(), name="vendor_declaration_vendor"),
    ##VendorKYCVendor
    path("vendor_kyc_vendor/", VendorKYCVendor.as_view(), name="vendor_kyc_vendor"),
    path("vendor_kyc_vendor/<pk>", VendorKYCVendor.as_view(), name="vendor_kyc_vendor"),
    ##VendorMaterialVendor
    path("vendor_material_vendor/", VendorMaterialVendor.as_view(), name="vendor_material_vendor"),
    path("vendor_material_vendor/<pk>", VendorMaterialVendor.as_view(), name="vendor_material_vendor"),
    #TransactionVendor
    path("transaction_vendor/", TransactionVendor.as_view(), name="transaction_vendor"),
    path("transaction_vendor/<pk>", TransactionVendor.as_view(), name="transaction_vendor"),
    ##PurchaseOrderVendor
    path("purchase_order_vendor/", PurchaseOrderVendor.as_view(), name="purchase_order_vendor"),
    path("purchase_order_vendor/<pk>", PurchaseOrderVendor.as_view(), name="purchase_order_vendor"),
]
