# Generated by Django 3.1.4 on 2021-11-24 13:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('brandid', models.CharField(db_column='BrandID', max_length=200, primary_key=True, serialize=False)),
                ('branddes', models.CharField(blank=True, db_column='BrandDes', max_length=2000, null=True)),
                ('img', models.CharField(blank=True, db_column='IMG', max_length=200, null=True)),
            ],
            options={
                'db_table': 'brand',
            },
        ),
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('customerid', models.CharField(db_column='ID', max_length=200, primary_key=True, serialize=False)),
                ('email', models.CharField(blank=True, db_column='Email', max_length=200, null=True)),
                ('password', models.CharField(blank=True, db_column='Password', max_length=200, null=True)),
                ('fullname', models.CharField(blank=True, db_column='FullName', max_length=200, null=True)),
                ('billingaddress', models.CharField(blank=True, db_column='BillingAddress', max_length=500, null=True)),
                ('shippingaddress', models.CharField(blank=True, db_column='ShippingAddress', max_length=500, null=True)),
                ('phone', models.CharField(blank=True, db_column='Phone', max_length=200, null=True)),
            ],
            options={
                'db_table': 'customers',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('productid', models.CharField(db_column='ID', max_length=200, primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='Name', max_length=200)),
                ('price', models.FloatField(db_column='Price')),
                ('img', models.CharField(db_column='IMG', max_length=200)),
                ('description', models.CharField(blank=True, db_column='Description', max_length=500, null=True)),
                ('stock', models.IntegerField(db_column='Stock')),
                ('createdate', models.DateField(db_column='CreateDate')),
                ('brandid', models.ForeignKey(db_column='BrandID', on_delete=django.db.models.deletion.DO_NOTHING, to='core.brand')),
            ],
            options={
                'db_table': 'product',
            },
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('orderid', models.CharField(db_column='OrderID', max_length=200, primary_key=True, serialize=False)),
                ('orderaddress', models.CharField(db_column='OrderAddress', max_length=500)),
                ('customeremail', models.CharField(blank=True, db_column='CustomerEmail', max_length=200, null=True)),
                ('orderdate', models.DateField(db_column='OrderDate')),
                ('orderstatus', models.CharField(db_column='OrderStatus', max_length=200)),
                ('customerid', models.ForeignKey(db_column='CustomerID', on_delete=django.db.models.deletion.DO_NOTHING, to='core.customers')),
            ],
            options={
                'db_table': 'orders',
            },
        ),
        migrations.CreateModel(
            name='Orderdetails',
            fields=[
                ('detailsid', models.IntegerField(db_column='ID', primary_key=True, serialize=False)),
                ('price', models.FloatField(blank=True, db_column='Price', null=True)),
                ('quantity', models.IntegerField(blank=True, db_column='Quantity', null=True)),
                ('orderid', models.ForeignKey(blank=True, db_column='OrderID', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.orders')),
                ('productid', models.ForeignKey(blank=True, db_column='ProductID', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.product')),
            ],
            options={
                'db_table': 'orderdetails',
            },
        ),
    ]
