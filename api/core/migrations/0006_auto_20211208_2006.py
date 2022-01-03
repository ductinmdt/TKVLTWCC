# Generated by Django 3.1.4 on 2021-12-08 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_address_brand_cart_cartdetails_orderdetails_orders_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartdetails',
            name='productname',
            field=models.CharField(db_column='ProductName', max_length=200),
        ),
        migrations.AlterField(
            model_name='orders',
            name='orderdate',
            field=models.DateField(blank=True, db_column='OrderDate', default='2021-12-08'),
        ),
        migrations.AlterField(
            model_name='product',
            name='createdate',
            field=models.DateField(db_column='CreateDate', default='2021-12-08'),
        ),
    ]
