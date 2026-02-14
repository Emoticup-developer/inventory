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
    
    creator = models.ForeignKey(
        "basic.UserDatabase", on_delete=models.SET_NULL, null=True, blank=True
    )
    company = models.ForeignKey(
        "basic.CompanyDatabase", on_delete=models.SET_NULL, null=True, blank=True
    )

    def __str__(self):
        return str(self.model_name) + str(self.model_code)


# group wise permission WHERE I CAN CREATED READ UPDATE DELETE
class AccessGroupDatabase(models.Model):
    id = models.BigAutoField(primary_key=True)

    ##group
    access_group_name = models.CharField(max_length=100, unique=True)
    access_group_code = models.CharField(max_length=100, unique=True)
    access_group_description = models.CharField(max_length=100)
    ##models
    # model = models.ForeignKey(
    #     "ModelNameDatabase", on_delete=models.SET_NULL, null=True, blank=True
    # )
    url = models.CharField(max_length=100, null=True, blank=True)
    ##access
    can_create = models.BooleanField(default=False)
    can_read = models.BooleanField(default=False)
    can_update = models.BooleanField(default=False)
    can_delete = models.BooleanField(default=False)
    ##timestamp
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    creator = models.ForeignKey(
        "basic.UserDatabase", on_delete=models.SET_NULL, null=True, blank=True
    )
    company = models.ForeignKey(
        "basic.CompanyDatabase", on_delete=models.SET_NULL, null=True, blank=True
    )

    def __str__(self):
        return self.access_group_name

    class Meta:
        verbose_name = "Access Group"
        verbose_name_plural = "Access Groups"
        ordering = ["-created_at"]
        db_table = "access_group_database"



class RowLevelPermission(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(
        "AccessGroupDatabase", on_delete=models.SET_NULL, null=True, blank=True
    )
    user = models.ForeignKey(
        "basic.UserDatabase", on_delete=models.SET_NULL, null=True, blank=True,related_name="user_row_permission"
    )
    #Code where associated model code is stored for row level permission
    code = models.CharField(max_length=100, unique=False)
    
    creator = models.ForeignKey(
        "basic.UserDatabase", on_delete=models.SET_NULL, null=True, blank=True
    )
    company = models.ForeignKey(
        "basic.CompanyDatabase", on_delete=models.SET_NULL, null=True, blank=True
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.group)
    
    
    class Meta:
        verbose_name = "Row Level Permission"
        verbose_name_plural = "Row Level Permissions"
        ordering = ["-created_at"]
        db_table = "row_level_permission"
        unique_together = ("group", "code")



## WHERE I CAN CREATED READ UPDATE DELETE TO USER
class AccessGroupUserDatabase(models.Model):
    id = models.BigAutoField(primary_key=True)
    access_group = models.ForeignKey(
        "AccessGroupDatabase", on_delete=models.CASCADE, null=False, blank=False
    )
    user = models.ForeignKey(
        "basic.UserDatabase", on_delete=models.SET_NULL, null=True, blank=True
    )
    model = models.ForeignKey(
        "ModelNameDatabase", on_delete=models.SET_NULL, null=True, blank=True
    )
    ## here code is related field where selected models particular code only accesible to user
    code = models.CharField(max_length=100, unique=False, null=True, blank=True)
    
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    creator = models.ForeignKey(
        "basic.UserDatabase", on_delete=models.SET_NULL, null=True, blank=True, related_name="creator"
    )
    company = models.ForeignKey(
        "basic.CompanyDatabase", on_delete=models.SET_NULL, null=True, blank=True ,related_name="company"
    )

    def __str__(self):
        return str(self.user) + "--- has access ---" + str(self.model.model_name) + "--- in ---" + str(self.access_group)

    class Meta:
        verbose_name = "Access Group User"
        verbose_name_plural = "Access Group Users"
        ordering = ["-created_at"]
        unique_together = ("access_group", "user","model")
        db_table = "access_group_user_database"


##direct give permision to user WHERE I CAN CREATED READ UPDATE DELETE FOR USER ADN MODEL
class UserModelPermission(models.Model):
    user = models.ForeignKey(
        "basic.UserDatabase", on_delete=models.SET_NULL, null=True, blank=True ,related_name="user"
    )

    model = models.ForeignKey(ModelNameDatabase, on_delete=models.CASCADE)
    code = models.CharField(max_length=100, unique=True, null=True, blank=True)
    
    
    can_create = models.BooleanField(null=True)
    can_read = models.BooleanField(null=True)
    can_update = models.BooleanField(null=True)
    can_delete = models.BooleanField(null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    
    creator = models.ForeignKey(
        "basic.UserDatabase", on_delete=models.SET_NULL, null=True, blank=True, related_name="creator_user"
    )
    company = models.ForeignKey(
        "basic.CompanyDatabase", on_delete=models.SET_NULL, null=True, blank=True, related_name="company_user"
    )

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

    ##timestamp
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    creator = models.ForeignKey(
        "basic.UserDatabase", on_delete=models.SET_NULL, null=True, blank=True, related_name="creator_sub"
    )
    company = models.ForeignKey(
        "basic.CompanyDatabase", on_delete=models.SET_NULL, null=True, blank=True, related_name="company_sub"
    )

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
        verbose_name = "Subscription"
        verbose_name_plural = "Subscriptions"
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
    
    creator = models.ForeignKey(
        "basic.UserDatabase", on_delete=models.SET_NULL, null=True, blank=True, related_name="creator_ap_status"
    )
    company = models.ForeignKey(
        "basic.CompanyDatabase", on_delete=models.SET_NULL, null=True, blank=True, related_name="company_ap_status"
    )

    def __str__(self):
        return self.status

    class Meta:
        verbose_name = "StatusApproval"
        verbose_name_plural = "StatusApproval"
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
    
    creator = models.ForeignKey(
        "basic.UserDatabase", on_delete=models.SET_NULL, null=True, blank=True, related_name="creator_ap_stack"
    )
    company = models.ForeignKey(
        "basic.CompanyDatabase", on_delete=models.SET_NULL, null=True, blank=True, related_name="company_ap_stack"
    )

    def __str__(self):
        return self.code

    class Meta:
        verbose_name = "Linked_List_Approver"
        verbose_name_plural = "Linked_List_Approver"
        ordering = ["-created_at"]
        db_table = "approval_stack"

##SUB ttask model 
class SubTask(models.Model):
    model = models.ForeignKey(
        "ModelNameDatabase", on_delete=models.SET_NULL, null=True, blank=True
    )
    payload = models.JSONField(null=True, blank=True)
    sub_task_uuid = models.UUIDField(editable=True, unique=False,null=True,blank=True)
    method = models.CharField(max_length=100, unique=False, blank=True, null=True)
    instance_id = models.CharField(max_length=100, unique=False, blank=True, null=True)
    ##timestamp
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_executed = models.BooleanField(default=False)
    creator = models.ForeignKey(
        "basic.UserDatabase", on_delete=models.SET_NULL, null=True, blank=True, related_name="creator_sub_task"
    )
    company = models.ForeignKey(
        "basic.CompanyDatabase", on_delete=models.SET_NULL, null=True, blank=True, related_name="company_sub_task"
    )

    def __str__(self):
        return str(self.sub_task_uuid) + " ---> " + str(self.model)

    class Meta:
        verbose_name = "SubTask"
        verbose_name_plural = "SubTask"
        ordering = ["-created_at"]
        db_table = "sub_task"

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
    sub_task_uuid = models.UUIDField(editable=True, unique=True,null=True,blank=True)
    ##timestamp
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    ##it help to identify the fucntion
    bloc = models.TextField(null=True, blank=True)

    creator = models.ForeignKey(
        "basic.UserDatabase", on_delete=models.SET_NULL, null=True, blank=True, related_name="creator_ap_process"
    )
    company = models.ForeignKey(
        "basic.CompanyDatabase", on_delete=models.SET_NULL, null=True, blank=True, related_name="company_ap_process"
    )
    
    def __str__(self):
        return str(self.code) + " - " + str(self.model_name)

    class Meta:
        verbose_name = "Shadow_model"
        verbose_name_plural = "Shadow_model"
        unique_together = ("model_name", "code","method","update_id","id")
        ordering = ["-created_at"]
        db_table = "approval_process"



class NavigationBox(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100, unique=False)
    path = models.CharField(max_length=100, unique=False)
    ##timestamp
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey(
        "basic.UserDatabase", on_delete=models.SET_NULL, null=True, blank=True, related_name="creator_navigation_box"
    )
    company = models.ForeignKey(
        "basic.CompanyDatabase", on_delete=models.SET_NULL, null=True, blank=True, related_name="company_navigation_box"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Navigation Box"
        verbose_name_plural = "Navigation Boxes"
        ordering = ["-created_at"]
        db_table = "navigation_box"