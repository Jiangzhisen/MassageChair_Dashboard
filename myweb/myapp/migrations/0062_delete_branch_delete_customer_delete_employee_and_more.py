# Generated by Django 4.2.2 on 2023-06-15 06:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0061_initial"),
    ]

    operations = [
        migrations.DeleteModel(name="Branch",),
        migrations.DeleteModel(name="Customer",),
        migrations.DeleteModel(name="Employee",),
        migrations.DeleteModel(name="Feedback",),
        migrations.DeleteModel(name="MassageChair",),
        migrations.DeleteModel(name="MassageChairUsage",),
        migrations.DeleteModel(name="Order",),
        migrations.DeleteModel(name="OrderDetail",),
        migrations.DeleteModel(name="Product",),
        migrations.DeleteModel(name="ProductModel",),
        migrations.DeleteModel(name="Purchase",),
        migrations.DeleteModel(name="PurchaseDetail",),
        migrations.DeleteModel(name="SalesActivity",),
        migrations.DeleteModel(name="SalesOpportunity",),
        migrations.DeleteModel(name="Supplier",),
        migrations.DeleteModel(name="User",),
        migrations.DeleteModel(name="Visitors",),
    ]
