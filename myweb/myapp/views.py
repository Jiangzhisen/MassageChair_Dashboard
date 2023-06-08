from django.shortcuts import render
from .models import Branch, Customer, Employee, Feedback, MassageChair, MassageChairUsage, Order, OrderDetail, ProductModel, Product, Purchase, PurchaseDetail, SalesActivity, SalesOpportunity, Supplier, Visitors
from datetime import datetime, date
import random

# Create your views here.

#營運儀表板頁面
def index(request):
    orders = Order.objects.all()
    dates = []
    monthSales_quantity = []
    monthSales_amount = []
    totalamount = 0
    totalquantity = 0
    totalVisitor = 0
    currentMonth = ""
    currentQuatity = 0
    currentAmount = 0

    for order in orders:
        date = order.orderdate
        date_str = date.strftime("%m")
        if date_str != currentMonth:
            monthSales_quantity.append(currentQuatity)
            monthSales_amount.append(currentAmount)
            currentAmount = 0
            currentQuatity = 0
            currentMonth = date_str
            orderId = order.orderid
            order_details = OrderDetail.objects.filter(orderid = orderId)
            for order_detail in order_details:
                quantity = order_detail.salesquantity
                currentQuatity += quantity
                totalquantity += quantity
            amount = order.orderprice
            currentAmount += amount
            totalamount += amount
        else:
            orderId = order.orderid
            order_details = OrderDetail.objects.filter(orderid = orderId)
            for order_detail in order_details:
                quantity = order_detail.salesquantity
                currentQuatity += quantity
                totalquantity += quantity
            amount = order.orderprice
            currentAmount += amount
            totalamount += amount
        dates.append(date_str)

    #去掉第一個無意義的值
    monthSales_quantity.append(currentQuatity)
    monthSales_quantity.pop(0)
    monthSales_amount.append(currentAmount)
    monthSales_amount.pop(0)

    #去除重複的值
    dates = set(dates)
    new_dates = list(dates)
    month_list = sorted(new_dates)




    visitors = Visitors.objects.all()
    monthSales_visitor = []
    dates1 = []
    currentMonth1 = ""
    currentVisitors = 0
    
    for visitor in visitors:
        date1 = visitor.date
        date_str1 = date1.strftime("%m")
        if date_str1 != currentMonth1:
            monthSales_visitor.append(currentVisitors)
            currentVisitors = 0
            currentMonth1 = date_str1
            times = visitor.visitorcount
            currentVisitors += times
            totalVisitor += times
        else:
            times = visitor.visitorcount
            currentVisitors += times
            totalVisitor += times

        dates1.append(date_str1)

    #去掉第一個無意義的值
    monthSales_visitor.append(currentVisitors)
    monthSales_visitor.pop(0)

    #去除重複的值
    dates1 = set(dates1)
    new_dates1 = list(dates1)
    month_list1 = sorted(new_dates1)


    totalCost = 0
    purchases = Purchase.objects.all()
    for purchase in purchases:
        cost = purchase.purchaseprice
        totalCost += cost


    employees = Employee.objects.all()
    employeeList = []
    for employee in employees:
        employeeSales = 0
        employeeFeel = 0
        count = 0
        employeeId = employee.employeeid
        employeeName = employee.employeename
        employeeOrders = Order.objects.filter(employeeid = employeeId)
        for employeeOrder in employeeOrders:
            sales = employeeOrder.orderprice
            employeeSales += sales
        
        employeeFeedbacks = Feedback.objects.filter(employeeid = employeeId)
        for employeeFeedback in employeeFeedbacks:
            count += 1
            feedback = employeeFeedback.satisfaction
            employeeFeel += feedback
        averageFeel = int((employeeFeel/count) * 20)
        random_number = random.randint(1, 5)
        employeeInfo = {
            "name": employeeName,
            "sales": employeeSales,
            "satisfaction": averageFeel,
            "random": random_number
        }
        employeeList.append(employeeInfo)









    # print(month_list)
    # print(monthSales_quantity)
    # print(monthSales_amount)
    # print(month_list1)
    # print(monthSales_visitor)
    # print(totalamount)
    # print(totalquantity)
    # print(totalVisitor)
    # print(totalCost)
    print(employeeList)

    return render(request, 'dashboard.html', locals())






def customer(request):
    return render(request, 'customer.html', locals())

def massageChair(request):
    return render(request, 'chair.html', locals())

def activity(request):
    return render(request, 'activity.html', locals())
