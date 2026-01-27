from django.contrib import admin

from ams.models import (
    AccessGroupDatabase,
    AccessGroupUserDatabase,
    ApprovalProcess,
    ApprovalStack,
    ApprovalStatusDatabase,
    ModelNameDatabase,
    UserModelPermission,
)

# Register your models here.
admin.site.register(ModelNameDatabase)
admin.site.register(ApprovalProcess)
admin.site.register(AccessGroupDatabase)
admin.site.register(UserModelPermission)
admin.site.register(AccessGroupUserDatabase)
admin.site.register(ApprovalStatusDatabase)
admin.site.register(ApprovalStack)
