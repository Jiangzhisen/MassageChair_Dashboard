# Generated by Django 4.2.2 on 2023-06-16 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("myapp", "0076_delete_branch_delete_customer_delete_employee_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Branch",
            fields=[
                (
                    "branchid",
                    models.CharField(max_length=45, primary_key=True, serialize=False),
                ),
                ("branchname", models.CharField(max_length=45)),
                ("branchaddress", models.CharField(max_length=45)),
                ("branchphone", models.CharField(max_length=45)),
                ("employeeid", models.CharField(max_length=45)),
                ("salesyear", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Customer",
            fields=[
                (
                    "customerid",
                    models.CharField(max_length=45, primary_key=True, serialize=False),
                ),
                ("customername", models.CharField(max_length=45)),
                ("customergender", models.CharField(max_length=45)),
                ("customerage", models.IntegerField()),
                ("customerprofession", models.CharField(max_length=45)),
                ("customerphone", models.CharField(max_length=45)),
                ("customeremail", models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name="Employee",
            fields=[
                (
                    "employeeid",
                    models.CharField(max_length=45, primary_key=True, serialize=False),
                ),
                ("employeename", models.CharField(max_length=45)),
                ("branchid", models.CharField(max_length=45)),
                ("employeeposition", models.CharField(max_length=45)),
                ("employeeentrydate", models.DateField()),
                ("employeephone", models.CharField(max_length=45)),
                ("employeegender", models.CharField(max_length=45)),
                ("employeeemail", models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name="Feedback",
            fields=[
                (
                    "feedbackid",
                    models.CharField(max_length=45, primary_key=True, serialize=False),
                ),
                ("customerid", models.CharField(max_length=45)),
                ("satisfaction", models.IntegerField()),
                ("employeeid", models.CharField(max_length=45)),
                ("orderid", models.CharField(max_length=45)),
                ("feedbackdate", models.DateField()),
                ("feedbacktype", models.CharField(max_length=45)),
                ("processstatus", models.CharField(max_length=45)),
                ("factor", models.CharField(max_length=45)),
                ("factor_price", models.IntegerField()),
                (
                    "factor_comfort",
                    models.DecimalField(decimal_places=2, max_digits=10),
                ),
            ],
        ),
        migrations.CreateModel(
            name="MassageChair",
            fields=[
                (
                    "massagerid",
                    models.CharField(max_length=45, primary_key=True, serialize=False),
                ),
                ("branchid", models.CharField(max_length=45)),
                ("status", models.CharField(max_length=45)),
                ("usagecount", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="MassageChairUsage",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("massagerid", models.CharField(max_length=45)),
                ("customerid", models.CharField(max_length=45)),
                ("totaltime", models.IntegerField()),
                ("starttime", models.DateTimeField()),
                ("endtime", models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name="Order",
            fields=[
                (
                    "orderid",
                    models.CharField(max_length=45, primary_key=True, serialize=False),
                ),
                ("employeeid", models.CharField(max_length=45)),
                ("customerid", models.CharField(max_length=45)),
                ("orderdate", models.DateField()),
                ("orderprice", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="OrderDetail",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("orderid", models.CharField(max_length=45)),
                ("productid", models.CharField(max_length=45)),
                ("modelid", models.CharField(max_length=45)),
                ("salesquantity", models.IntegerField()),
                ("salesamount", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "productid",
                    models.CharField(max_length=45, primary_key=True, serialize=False),
                ),
                ("modelid", models.CharField(max_length=45)),
                ("productiondate", models.DateField()),
                ("supplierid", models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name="ProductModel",
            fields=[
                (
                    "modelid",
                    models.CharField(max_length=45, primary_key=True, serialize=False),
                ),
                ("productname", models.CharField(max_length=45)),
                ("productprice", models.IntegerField()),
                ("inventory", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Purchase",
            fields=[
                (
                    "purchaseid",
                    models.CharField(max_length=45, primary_key=True, serialize=False),
                ),
                ("employeeid", models.CharField(max_length=45)),
                ("supplierid", models.CharField(max_length=45)),
                ("purchasedate", models.DateField()),
                ("purchaseprice", models.IntegerField()),
                ("purchasepayment", models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name="PurchaseDetail",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("purchaseid", models.CharField(max_length=45)),
                ("modelid", models.CharField(max_length=45)),
                ("purchasequantity", models.IntegerField()),
                ("purchaseamount", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="SalesActivity",
            fields=[
                (
                    "salesactid",
                    models.CharField(max_length=45, primary_key=True, serialize=False),
                ),
                ("salesstage", models.CharField(max_length=45)),
                ("salesacttype", models.CharField(max_length=45)),
                ("salesactremark", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="SalesOpportunity",
            fields=[
                (
                    "salesoppid",
                    models.CharField(max_length=45, primary_key=True, serialize=False),
                ),
                ("customerid", models.CharField(max_length=45)),
                ("salesactid", models.CharField(max_length=45)),
                ("employeeid", models.CharField(max_length=45)),
                ("salesoppexcd", models.DateField()),
                ("salesoppexsa", models.IntegerField()),
                ("status", models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name="Supplier",
            fields=[
                (
                    "supplierid",
                    models.CharField(max_length=45, primary_key=True, serialize=False),
                ),
                ("suppliername", models.CharField(max_length=45)),
                ("supplierphone", models.CharField(max_length=45)),
                ("supplieraddress", models.CharField(max_length=45)),
                ("contactperson", models.CharField(max_length=45)),
                ("supplieremail", models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "userid",
                    models.CharField(max_length=45, primary_key=True, serialize=False),
                ),
                ("userpassword", models.CharField(max_length=45)),
                ("employeeid", models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name="Visitors",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("branchid", models.CharField(max_length=45)),
                ("date", models.DateField()),
                ("visitorcount", models.IntegerField()),
            ],
        ),
    ]
