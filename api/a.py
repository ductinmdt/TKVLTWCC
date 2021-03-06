# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class CoreAddress(models.Model):
    username = models.CharField(unique=True, max_length=150)
    default_address = models.CharField(db_column='Default Address', max_length=45, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    shippingaddress = models.CharField(db_column='ShippingAddress', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'core_address'


class CoreAnhpham(models.Model):
    name = models.CharField(max_length=160)

    class Meta:
        managed = False
        db_table = 'core_anhpham'


class CoreBrand(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    brandname = models.CharField(db_column='BrandName', max_length=200)  # Field name made lowercase.
    branddes = models.CharField(db_column='BrandDes', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    img = models.CharField(db_column='IMG', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'core_brand'


class CoreCart(models.Model):
    cartid = models.AutoField(db_column='CartID', primary_key=True)  # Field name made lowercase.
    username = models.CharField(max_length=150)
    carttotal = models.FloatField(db_column='CartTotal')  # Field name made lowercase.
    cartnum = models.CharField(db_column='Cartnum', max_length=45, blank=True, null=True)  # Field name made lowercase.
    typecart = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'core_cart'


class CoreCartdetails(models.Model):
    deltailsid = models.AutoField(db_column='DeltailsID', primary_key=True)  # Field name made lowercase.
    quantity = models.IntegerField()
    price = models.FloatField(db_column='Price')  # Field name made lowercase.
    username = models.CharField(max_length=200)
    productname = models.CharField(db_column='ProductName', max_length=200)  # Field name made lowercase.
    img = models.CharField(db_column='IMG', max_length=200)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'core_cartdetails'


class CoreOrderdetails(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    orderid = models.IntegerField(db_column='OrderID')  # Field name made lowercase.
    quantity = models.IntegerField(db_column='Quantity')  # Field name made lowercase.
    price = models.FloatField(db_column='Price')  # Field name made lowercase.
    productname = models.CharField(db_column='ProductName', max_length=200)  # Field name made lowercase.
    img = models.CharField(db_column='IMG', max_length=200)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'core_orderdetails'


class CoreOrders(models.Model):
    orderid = models.AutoField(db_column='OrderID', primary_key=True)  # Field name made lowercase.
    orderaddress = models.CharField(db_column='OrderAddress', max_length=500, blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(max_length=200)
    orderdate = models.DateField(db_column='OrderDate')  # Field name made lowercase.
    orderstatus = models.CharField(db_column='OrderStatus', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'core_orders'


class CoreProduct(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    productcode = models.CharField(db_column='ProductCode', max_length=200, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=200)  # Field name made lowercase.
    price = models.FloatField(db_column='Price')  # Field name made lowercase.
    img = models.CharField(db_column='IMG', max_length=200)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    stock = models.IntegerField(db_column='Stock')  # Field name made lowercase.
    createdate = models.DateField(db_column='CreateDate')  # Field name made lowercase.
    brandname = models.ForeignKey(CoreBrand, models.DO_NOTHING, db_column='BrandName')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'core_product'


class CoreProfile(models.Model):
    username = models.CharField(max_length=200)
    img = models.CharField(db_column='IMG', max_length=200)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'core_profile'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Feedback(models.Model):
    topic = models.CharField(max_length=200)
    title = models.CharField(max_length=200, blank=True, null=True)
    name = models.CharField(max_length=45, blank=True, null=True)
    email = models.CharField(db_column='Email', max_length=45, blank=True, null=True)  # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=45, blank=True, null=True)  # Field name made lowercase.
    des = models.CharField(db_column='Des', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'feedback'
