from django.contrib import admin

from vendor.models import KYCStatus, Quotation, Vendor, VendorDeclaration, VendorKYC, VendorMaterial, VendorType

# Register your models here.
admin.site.register(VendorType)
admin.site.register(Vendor)
admin.site.register(VendorDeclaration)
admin.site.register(Quotation)
admin.site.register(VendorMaterial)
admin.site.register(KYCStatus)
admin.site.register(VendorKYC)

