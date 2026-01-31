from django.contrib import admin

from ams.models import (
    AccessGroupDatabase,
    AccessGroupUserDatabase,
    ApprovalProcess,
    ApprovalStack,
    ApprovalStatusDatabase,
    ModelNameDatabase,
    RowLevelPermission,
    SubscriptionModel,
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
admin.site.register(SubscriptionModel)
admin.site.register(RowLevelPermission)
