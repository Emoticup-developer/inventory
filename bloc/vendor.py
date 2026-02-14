from basic.models import UserDatabase, UserTypeDatabase


def VendorCreated(context):
    model = context["model"]
    user = UserDatabase.objects.create_user(
        email=model.email,
        password=str(model.vendor_code).strip(),
        username=str(model.vendor_code).strip(),
        user_company = model.company,
        user_type = UserTypeDatabase.objects.filter(type_code="VENDOR").first(),
        user_code = str(model.vendor_code).strip(),
        is_active = True,
        first_name = model.vendor_name  ,
        last_name = model.short_name ,
        phone_number = model.phone,
    )
    model.is_active = True
    model.is_blacklisted = False
    model.is_approved_by_cfo = True
    model.is_validated = True
    model.save()
    user.save()
    
