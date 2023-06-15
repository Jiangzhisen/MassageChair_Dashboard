from django.db import models

# Create your models here.

#分店資料表
class Branch(models.Model):
    branchid = models.CharField(max_length=45, primary_key=True)
    branchname = models.CharField(max_length=45)
    branchaddress = models.CharField(max_length=45)
    branchphone = models.CharField(max_length=45)
    employeeid = models.CharField(max_length=45)
    salesyear = models.IntegerField()

#分店訪客量資料表
class Visitors(models.Model):
    branchid = models.CharField(max_length=45)
    date = models.DateField()
    visitorcount = models.IntegerField()

#客戶資料表
class Customer(models.Model):
    customerid = models.CharField(max_length=45, primary_key=True)
    customername = models.CharField(max_length=45)
    customergender = models.CharField(max_length=45)
    customerage = models.IntegerField()
    customerprofession = models.CharField(max_length=45)
    customerphone = models.CharField(max_length=45)
    customeremail = models.CharField(max_length=45)

#員工資料表
class Employee(models.Model):
    employeeid = models.CharField(max_length=45, primary_key=True)
    employeename = models.CharField(max_length=45)
    branchid = models.CharField(max_length=45)
    employeeposition = models.CharField(max_length=45)
    employeeentrydate = models.DateField()
    employeephone = models.CharField(max_length=45)
    employeegender = models.CharField(max_length=45)
    employeeemail = models.CharField(max_length=45)

#帳號密碼資料表
class User(models.Model):
    userid = models.CharField(max_length=45, primary_key=True)
    userpassword = models.CharField(max_length=45)
    employeeid = models.CharField(max_length=45)

#意見回饋資料表
class Feedback(models.Model):
    feedbackid = models.CharField(max_length=45, primary_key=True)
    customerid = models.CharField(max_length=45)
    satisfaction = models.IntegerField()
    employeeid = models.CharField(max_length=45)
    orderid = models.CharField(max_length=45)
    feedbackdate = models.DateField()
    feedbacktype = models.CharField(max_length=45)
    processstatus = models.CharField(max_length=45)
    factor = models.CharField(max_length=45)
    factor_price = models.IntegerField()
    factor_comfort = models.DecimalField(max_digits=10, decimal_places=2)

#公共按摩椅資料表
class MassageChair(models.Model):
    massagerid = models.CharField(max_length=45, primary_key=True)
    branchid = models.CharField(max_length=45)
    status = models.CharField(max_length=45)
    usagecount = models.IntegerField()

#公共按摩椅使用狀態按摩椅
class MassageChairUsage(models.Model):
    massagerid = models.CharField(max_length=45)
    customerid = models.CharField(max_length=45)
    totaltime = models.IntegerField()
    starttime = models.DateTimeField()
    endtime = models.DateTimeField()

#訂單資料表
class Order(models.Model):
    orderid = models.CharField(max_length=45, primary_key=True)
    employeeid = models.CharField(max_length=45)
    customerid = models.CharField(max_length=45)
    orderdate = models.DateField()
    orderprice = models.IntegerField()

#訂單詳細資料表
class OrderDetail(models.Model):
    orderid = models.CharField(max_length=45)
    productid = models.CharField(max_length=45)
    modelid = models.CharField(max_length=45)
    salesquantity = models.IntegerField()
    salesamount = models.IntegerField()
    # class Meta:
    #     constraints = [
    #         models.UniqueConstraint(fields=['orderid', 'productid'], name='unique_order_detail')
    #     ]

#產品型號資料表
class ProductModel(models.Model):
    modelid = models.CharField(max_length=45, primary_key=True)
    productname = models.CharField(max_length=45)
    productprice = models.IntegerField()
    inventory = models.IntegerField()

#產品資料表
class Product(models.Model):
    productid = models.CharField(max_length=45, primary_key=True)
    modelid = models.CharField(max_length=45)
    productiondate = models.DateField()
    supplierid = models.CharField(max_length=45)

#進貨資料表
class Purchase(models.Model):
    purchaseid = models.CharField(max_length=45, primary_key=True)
    employeeid = models.CharField(max_length=45)
    supplierid = models.CharField(max_length=45)
    purchasedate = models.DateField()
    purchaseprice = models.IntegerField()
    purchasepayment = models.CharField(max_length=45)

#進貨詳細資料表
class PurchaseDetail(models.Model):
    purchaseid = models.CharField(max_length=45)
    modelid = models.CharField(max_length=45)
    purchasequantity = models.IntegerField()
    purchaseamount = models.IntegerField()
    # class Meta:
    #     constraints = [
    #         models.UniqueConstraint(fields=['purchaseid', 'modelid'], name='unique_purchase_detail')
    #     ]

#銷售活動資料表
class SalesActivity(models.Model):
    salesactid = models.CharField(max_length=45, primary_key=True)
    salesstage = models.CharField(max_length=45)
    salesacttype = models.CharField(max_length=45)
    salesactremark = models.CharField(max_length=100)

#銷售機會資料表
class SalesOpportunity(models.Model):
    salesoppid = models.CharField(max_length=45, primary_key=True)
    customerid = models.CharField(max_length=45)
    salesactid = models.CharField(max_length=45)
    employeeid = models.CharField(max_length=45)
    salesoppexcd = models.DateField()
    salesoppexsa = models.IntegerField()
    status = models.CharField(max_length=45)

#供應商資料表
class Supplier(models.Model):
    supplierid = models.CharField(max_length=45, primary_key=True)
    suppliername = models.CharField(max_length=45)
    supplierphone = models.CharField(max_length=45)
    supplieraddress = models.CharField(max_length=45)
    contactperson = models.CharField(max_length=45)
    supplieremail = models.CharField(max_length=45)





