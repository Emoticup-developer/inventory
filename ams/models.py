from django.db import models


## ALL MODEL REGISED HERE
class ModelNameDatabase(models.Model):
    id = models.BigAutoField(primary_key=True)
    model_name = models.CharField(max_length=100, unique=True)
    model_code = models.CharField(max_length=100, unique=True)
    model_app = models.CharField(max_length=100)
    model_description = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.model_name) + str(self.model_code)


# group wise permission WHERE I CAN CREATED READ UPDATE DELETE
class AccessGroupDatabase(models.Model):

    id = models.BigAutoField(primary_key=True)
    ##company
    company = models.ForeignKey(
        "basic.CompanyDatabase", on_delete=models.SET_NULL, null=True, blank=True
    )

    ##group
    access_group_name = models.CharField(max_length=100, unique=True)
    access_group_code = models.CharField(max_length=100, unique=True)
    access_group_description = models.CharField(max_length=100)
    ##models
    model = models.ForeignKey(
        "ModelNameDatabase", on_delete=models.SET_NULL, null=True, blank=True
    )
    url = models.CharField(max_length=100, null=True, blank=True)
    ##access
    can_create = models.BooleanField(default=False)
    can_read = models.BooleanField(default=False)
    can_update = models.BooleanField(default=False)
    can_delete = models.BooleanField(default=False)
    ##timestamp
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.access_group_name

    class Meta:
        verbose_name = "Access Group"
        verbose_name_plural = "Access Groups"
        ordering = ["-created_at"]
        db_table = "access_group_database"


## WHERE I CAN CREATED READ UPDATE DELETE TO USER
class AccessGroupUserDatabase(models.Model):
    id = models.BigAutoField(primary_key=True)
    access_group = models.ForeignKey(
        "AccessGroupDatabase", on_delete=models.CASCADE, null=False, blank=False
    )
    user = models.ForeignKey(
        "basic.UserDatabase", on_delete=models.SET_NULL, null=True, blank=True
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.user) + " - " + str(self.access_group)

    class Meta:
        verbose_name = "Access Group User"
        verbose_name_plural = "Access Group Users"
        ordering = ["-created_at"]
        unique_together = ("access_group", "user")
        db_table = "access_group_user_database"


##direct give permision to user WHERE I CAN CREATED READ UPDATE DELETE FOR USER ADN MODEL
class UserModelPermission(models.Model):
    user = models.ForeignKey(
        "basic.UserDatabase", on_delete=models.SET_NULL, null=True, blank=True
    )

    model = models.ForeignKey(ModelNameDatabase, on_delete=models.CASCADE)

    can_create = models.BooleanField(null=True)
    can_read = models.BooleanField(null=True)
    can_update = models.BooleanField(null=True)
    can_delete = models.BooleanField(null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user) + " - " + str(self.model)

    class Meta:
        unique_together = ("user", "model")
        db_table = "user_model_permission"
        ordering = ["-created_at"]


class SubscriptionModel(models.Model):
    id = models.BigAutoField(primary_key=True)
    model = models.ForeignKey(
        "ModelNameDatabase", on_delete=models.SET_NULL, null=True, blank=True
    )
    create = models.BooleanField(default=False)
    can_delete = models.BooleanField(default=False)
    update = models.BooleanField(default=False)
    code = models.CharField(max_length=100, unique=False, blank=True, null=True)
    company = models.ForeignKey(
        "basic.CompanyDatabase", on_delete=models.SET_NULL, null=True, blank=True
    )
    ##timestamp
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return (
            str(self.model)
            + " - "
            + str(self.create)
            + " - "
            + str(self.can_delete)
            + " - "
            + str(self.update)
        )

    class Meta:
        verbose_name = "Subscription Model"
        verbose_name_plural = "Subscription Models"
        ordering = ["-created_at"]
        db_table = "subscription_model"
        unique_together = ("model",)


## MASTER DATA OF STATUS OF APPROVAL
class ApprovalStatusDatabase(models.Model):
    id = models.BigAutoField(primary_key=True)
    status = models.CharField(max_length=100, unique=True)
    code = models.CharField(max_length=100, unique=True)
    ##timestamp
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.status

    class Meta:
        verbose_name = "Approval Status"
        verbose_name_plural = "Approval Statuses"
        ordering = ["-created_at"]
        db_table = "approval_status_database"


## LEVEL OF APPROVAL WHERE STRCUTURE IS DEFINED WHO AFTET WHO
class ApprovalStack(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(
        "basic.UserDatabase", on_delete=models.SET_NULL, null=True, blank=True
    )
    is_first = models.BooleanField(default=False)
    next_user = models.ForeignKey(
        "self", on_delete=models.SET_NULL, null=True, blank=True
    )
    code = models.CharField(max_length=100, unique=False)
    ##timestamp
    comments = models.JSONField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.code

    class Meta:
        verbose_name = "Approval Stack"
        verbose_name_plural = "Approval Stacks"
        ordering = ["-created_at"]
        db_table = "approval_stack"


## BASE WHERE DATA IS STORED FOR APPROVAL
class ApprovalProcess(models.Model):
    id = models.BigAutoField(primary_key=True)
    ##model related
    model_name = models.ForeignKey(
        "ModelNameDatabase", on_delete=models.SET_NULL, null=True, blank=True
    )
    data = models.BinaryField(blank=True, null=True)
    payload = models.JSONField(blank=True, null=True)

    ##status
    status = models.ForeignKey(
        "ApprovalStatusDatabase", on_delete=models.SET_NULL, null=True, blank=True
    )
    ##company
    company = models.ForeignKey(
        "basic.CompanyDatabase", on_delete=models.SET_NULL, null=True, blank=True
    )
    recent_user = models.ForeignKey(
        ApprovalStack, on_delete=models.SET_NULL, null=True, blank=True
    )
    update_id = models.CharField(blank=True,null=True,max_length=100)
    code = models.CharField(max_length=100, unique=False)
    method = models.TextField(blank=False , null = False , default = "POST")
    comments = models.JSONField(blank=True, null=True)

    ##timestamp
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.code) + " - " + str(self.model_name)

    class Meta:
        verbose_name = "Approval Process"
        verbose_name_plural = "Approval Processes"
        ordering = ["-created_at"]
        db_table = "approval_process"
