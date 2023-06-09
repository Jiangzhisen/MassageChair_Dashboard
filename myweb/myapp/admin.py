from django.contrib import admin
from myapp.models import Branch, Customer, Employee, Feedback, MassageChair, MassageChairUsage, Order, OrderDetail, ProductModel, Product, Purchase, PurchaseDetail, SalesActivity, SalesOpportunity, Supplier, Visitors

# Register your models here.

class Branchadmin(admin.ModelAdmin):
    list_display = ('branchid', 'branchname', 'branchaddress', 'branchphone', 'employeeid')

class Customeradmin(admin.ModelAdmin):
    list_display = ('customerid', 'customername', 'customergender', 'customerage', 'customerprofession', 'customerphone', 'customeremail')

class Employeeadmin(admin.ModelAdmin):
    list_display = ('employeeid', 'employeename', 'branchid', 'employeeposition', 'employeeentrydate', 'employeephone', 'employeegender', 'employeeemail')

class Feedbackadmin(admin.ModelAdmin):
    list_display = ('feedbackid', 'customerid', 'satisfaction', 'employeeid', 'orderid', 'feedbackdate', 'feedbacktype', 'processstatus')

class MassageChairadmin(admin.ModelAdmin):
    list_display = ('massagerid', 'branchid', 'status', 'usagecount')

class MassageChairUsageadmin(admin.ModelAdmin):
    list_display = ('massagerid', 'customerid', 'totaltime', 'starttime', 'endtime')

class Orderadmin(admin.ModelAdmin):
    list_display = ('orderid', 'employeeid', 'customerid', 'orderdate', 'orderprice')

class OrderDetailadmin(admin.ModelAdmin):
    list_display = ('orderid', 'productid', 'modelid', 'salesquantity', 'salesamount')

class ProductModeladmin(admin.ModelAdmin):
    list_display = ('modelid', 'productname', 'productprice', 'inventory')

class Productadmin(admin.ModelAdmin):
    list_display = ('productid', 'modelid', 'productiondate', 'supplierid')

class Purchaseadmin(admin.ModelAdmin):
    list_display = ('purchaseid', 'employeeid', 'supplierid', 'purchasedate', 'purchaseprice', 'purchasepayment')

class PurchaseDetailadmin(admin.ModelAdmin):
    list_display = ('purchaseid', 'modelid', 'purchasequantity', 'purchaseamount')

class SalesActivityadmin(admin.ModelAdmin):
    list_display = ('salesactid', 'salesstage', 'salesacttype', 'salesactremark')

class SalesOpportunityadmin(admin.ModelAdmin):
    list_display = ('salesoppid', 'customerid', 'salesactid', 'employeeid', 'salesoppexcd', 'salesoppexsa')

class Supplieradmin(admin.ModelAdmin):
    list_display = ('supplierid', 'suppliername', 'supplierphone', 'supplieraddress', 'contactperson', 'supplieremail')

class Visitorsadmin(admin.ModelAdmin):
    list_display = ('branchid', 'date', 'visitorcount')


admin.site.register(Branch, Branchadmin)
admin.site.register(Customer, Customeradmin)
admin.site.register(Employee, Employeeadmin)
admin.site.register(Feedback, Feedbackadmin)
admin.site.register(MassageChair, MassageChairadmin)
admin.site.register(MassageChairUsage, MassageChairUsageadmin)
admin.site.register(Order, Orderadmin)
admin.site.register(OrderDetail, OrderDetailadmin)
admin.site.register(ProductModel, ProductModeladmin)
admin.site.register(Product, Productadmin)
admin.site.register(Purchase, Purchaseadmin)
admin.site.register(PurchaseDetail, PurchaseDetailadmin)
admin.site.register(SalesActivity, SalesActivityadmin)
admin.site.register(SalesOpportunity, SalesOpportunityadmin)
admin.site.register(Supplier, Supplieradmin)
admin.site.register(Visitors, Visitorsadmin)



