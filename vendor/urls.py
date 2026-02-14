from django.urls import path
from .views import *
from .user_view import VendorAccount,VendorQuotation

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
]
