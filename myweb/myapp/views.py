from django.shortcuts import render, redirect
from .models import Branch, Customer, Employee, Feedback, MassageChair, MassageChairUsage, Order, OrderDetail, ProductModel, Product, Purchase, PurchaseDetail, SalesActivity, SalesOpportunity, Supplier, Visitors, User
from datetime import datetime
import random
from django.db.models import Count,Sum
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.

#營運儀表板首頁
def index(request):
    if request.session.get('is_authenticated', False):
        #銷售量和銷售額的部分
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


        #訪客數的部分
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


        #成本計算的部分
        totalCost = 0
        purchases = Purchase.objects.all()
        for purchase in purchases:
            cost = purchase.purchaseprice
            totalCost += cost


        #員工績效的部分
        employees = Employee.objects.all()
        employeeList = []
        employeeRank = []
        employeeCount = 0

        for employee in employees:
            employeeCount += 1
            employeeRank.append(employeeCount)
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
                "random": random_number,
                "color": generate_random_color()
            }
            employeeList.append(employeeInfo)

        sortedEmployeeList = sorted(employeeList, key=lambda x: x['sales'], reverse=True)
        # 在 sortedEmployeeList 的每個 employeeInfo 字典中增加 'rank' 屬性
        for i, employee in enumerate(sortedEmployeeList):
            employee['rank'] = i + 1

        

        # 定義預測銷售金額的字典
        sales_by_month = {}
        predicts = SalesOpportunity.objects.all()
        for predict in predicts:
            month = predict.salesoppexcd.month
            sales2 = predict.salesoppexsa
            date3 = f"{month}月"

            # 累計該月份的預測銷售金額
            if date3 in sales_by_month:
                sales_by_month[date3] += sales2
            else:
                sales_by_month[date3] = sales2

        
        #分店銷售額排行
        branchList = []
        branchs = Branch.objects.all()
        for branch in branchs:
            branchname = branch.branchname
            branchsales = branch.salesyear
            branchInfo = {
                "name": branchname,
                "sales": branchsales
            }
            branchList.append(branchInfo)

        sortedbranchList = sorted(branchList, key=lambda x: x['sales'], reverse=True)
        for i, branch in enumerate(sortedbranchList):
            branch['rank'] = i + 1

    else:
        messages.error(request, '您還未登入！請輸入帳號密碼登入。')
        return redirect('/signin/')
    

    return render(request, 'dashboard.html', locals())


#客戶資訊頁面
def customer(request):
    if request.session.get('is_authenticated', False):
        #客戶資料的部分
        customers = Customer.objects.all()
        customerList = []
        malestagetotal = []
        totalPeople = []
        femalestagetotal = []
        for customer in customers:
            customerId = customer.customerid
            customerName = customer.customername
            customerEmail = customer.customeremail
            customerPhone = customer.customerphone
            customerGender = customer.customergender
            customerAge = customer.customerage
            customerProfession = customer.customerprofession
            customerTotaltime = 0
            customerStage = ""
            random_number = random.randint(1, 5)

            usages = MassageChairUsage.objects.filter(customerid = customerId)
            if usages:
                for usage in usages:
                    time = usage.totaltime
                    customerTotaltime += time
            else:
                customerTotaltime = 0

            try:
                salesopp = SalesOpportunity.objects.get(customerid = customerId)
                salesactId = salesopp.salesactid
                salesStage = SalesActivity.objects.get(salesactid = salesactId)
                customerStage = salesStage.salesstage
            except SalesOpportunity.DoesNotExist:
                customerStage = "第五階段"

            customerInfo = {
                "name": customerName,
                "email": customerEmail,
                "phone": customerPhone,
                "gender": customerGender,
                "age": customerAge,
                "profession": customerProfession,
                "totaltime": customerTotaltime,
                "stage": customerStage,
                "random": random_number
            }
            customerList.append(customerInfo)


            #階段分析圖的部分
            maleFirst = 0
            maleSecond = 0
            maleThird = 0
            maleFourth = 0
            maleFifth = 0
            males = Customer.objects.filter(customergender = "男")
            for male in males:
                maleId = male.customerid
                try:
                    maleopp = SalesOpportunity.objects.get(customerid = maleId)
                    salesstageId = maleopp.salesactid
                    if salesstageId == "A001":
                        maleFirst += 1
                    elif salesstageId == "A002":
                        maleSecond += 1
                    elif salesstageId == "A003":
                        maleThird += 1
                    else:
                        maleFourth += 1
                except:
                    maleFifth += 1

            femaleFirst = 0
            femaleSecond = 0
            femaleThird = 0
            femaleFourth = 0
            femaleFifth = 0
            females = Customer.objects.filter(customergender = "女")
            for female in females:
                femaleId = female.customerid
                try:
                    femaleopp = SalesOpportunity.objects.get(customerid = femaleId)
                    salesstageId = femaleopp.salesactid
                    if salesstageId == "A001":
                        femaleFirst += 1
                    elif salesstageId == "A002":
                        femaleSecond += 1
                    elif salesstageId == "A003":
                        femaleThird += 1
                    else:
                        femaleFourth += 1
                except:
                    femaleFifth += 1
        
        malestagetotal.append(maleFirst)
        malestagetotal.append(maleSecond)
        malestagetotal.append(maleThird)
        malestagetotal.append(maleFourth)
        malestagetotal.append(maleFifth)

        femalestagetotal.append(femaleFirst)
        femalestagetotal.append(femaleSecond)
        femalestagetotal.append(femaleThird)
        femalestagetotal.append(femaleFourth)
        femalestagetotal.append(femaleFifth)

        firstTotal = maleFirst + femaleFirst
        secondTotal = maleSecond + femaleSecond
        thirdTotal = maleThird + femaleThird
        fourthTotal = maleFourth + femaleFourth
        fifthTotal = maleFifth + femaleFifth

        totalPeople.append(firstTotal)
        totalPeople.append(secondTotal)
        totalPeople.append(thirdTotal)
        totalPeople.append(fourthTotal)
        totalPeople.append(fifthTotal)


        #性別分布的部分
        genderpercent = []
        maleTotal = maleFirst + maleSecond + maleThird + maleFourth + maleFifth
        femaleTotal = femaleFirst + femaleSecond + femaleThird + femaleFourth + femaleFifth
        genderpercent.append(femaleTotal)
        genderpercent.append(maleTotal)


        #職業分布的部分
        occupationList = []
        occupationCount = []
        occupationColor = []
        occupation_counts = Customer.objects.values('customerprofession').annotate(total=Count('customerid'))
        for item in occupation_counts:
            occupation = item['customerprofession']
            total_count = item['total']
            random_color = generate_random_color()
            occupationList.append(occupation)
            occupationCount.append(total_count)
            occupationColor.append(random_color)

        
        #年齡分布的部分
        agelist = []
        colorlist = []
        firstAge = 0
        secondAge = 0
        thirdAge = 0
        fourthAge = 0
        fifthAge = 0
        sixthAge = 0
        customers1 = Customer.objects.all()
        for customer1 in customers1:
            customerage1 = customer1.customerage
            if customerage1 >= 70:
                sixthAge += 1
            elif customerage1 >= 60:
                fifthAge += 1
            elif customerage1 >= 50:
                fourthAge += 1
            elif customerage1 >= 40:
                thirdAge += 1
            elif customerage1 >= 30:
                secondAge += 1
            else:
                firstAge += 1
        
        for i in range(1, 7):
            random_color1 = generate_random_color()
            colorlist.append(random_color1)
            
        agelist.append(firstAge)
        agelist.append(secondAge)
        agelist.append(thirdAge)
        agelist.append(fourthAge)
        agelist.append(fifthAge)
        agelist.append(sixthAge)


        #購買目的的部分
        purposeList = []
        purposeNum = []
        purposeColor = []
        purposes = Feedback.objects.values('feedbacktype').annotate(total = Count('feedbackid'))
        for purpose in purposes:
            intent = purpose['feedbacktype']
            totalCount = purpose['total']
            random_color2 = generate_random_color()
            purposeList.append(intent)
            purposeNum.append(totalCount)
            purposeColor.append(random_color2)



        #各階段成敗率
        # successRateList = []
        # actList = ["A001", "A002", "A003", "A004"]
        # for act in actList:
        #     successRate = 0
        #     opportunities1 = SalesOpportunity.objects.filter(salesactid = act)
        #     allOpportunity = opportunities1.count()
        #     seccessopps1 = SalesOpportunity.objects.filter(salesactid = act, status = "成功")
        #     sucOpportunity = seccessopps1.count()
        #     successRate = int((sucOpportunity / allOpportunity) * 100)
        #     successRateList.append(successRate)

        successRateList = []
        #第一階段
        stage1all = SalesOpportunity.objects.all()
        stage1suc = SalesOpportunity.objects.filter(status = "成功")
        allCount1 = stage1all.count()
        sucCount1 = stage1suc.count()
        successRate1 = int((sucCount1 / allCount1) * 100)
        successRateList.append(successRate1)

        #第二階段
        stage2all = SalesOpportunity.objects.exclude(salesactid = "A001")
        stage2suc = SalesOpportunity.objects.exclude(salesactid = "A001").filter(status = "成功")
        allCount2 = stage2all.count()
        sucCount2 = stage2suc.count()
        successRate2 = int((sucCount2 / allCount2) * 100)
        successRateList.append(successRate2)

        #第三階段
        stage3all = SalesOpportunity.objects.exclude(salesactid = "A001").exclude(salesactid = "A002")
        stage3suc = SalesOpportunity.objects.exclude(salesactid = "A001").exclude(salesactid = "A002").filter(status = "成功")
        allCount3 = stage3all.count()
        sucCount3 = stage3suc.count()
        successRate3 = int((sucCount3 / allCount3) * 100)
        successRateList.append(successRate3)

        #第四階段
        stage4all = SalesOpportunity.objects.exclude(salesactid = "A001").exclude(salesactid = "A002").exclude(salesactid = "A003")
        stage4suc = SalesOpportunity.objects.exclude(salesactid = "A001").exclude(salesactid = "A002").exclude(salesactid = "A003").filter(status = "成功")
        allCount4 = stage4all.count()
        sucCount4 = stage4suc.count()
        successRate4 = int((sucCount4 / allCount4) * 100)
        successRateList.append(successRate4)


        factorList = []
        feedbacks = Feedback.objects.all()
        for feedback in feedbacks:
            factorPrice = feedback.factor_price
            factorComfort = feedback.factor_comfort
            factor = {
                "price": factorPrice,
                "comfort": factorComfort
            }
            factorList.append(factor)
    else:
        messages.error(request, '您還未登入！請輸入帳號密碼登入。')
        return redirect('/signin/')
    
    return render(request, 'customer.html', locals())


#按摩椅資訊頁面
def massageChair(request):
    if request.session.get('is_authenticated', False):
        ##公共按摩椅熱門時段折線圖完成
        Massages = MassageChair.objects.all()
        status_list = []
        for massage in Massages:
            status_list.append(massage.status)
        # print(status_list)
        # 設定時間區間
        intervals = [
            ("08:00", "10:00"),
            ("10:00", "12:00"),
            ("12:00", "14:00"),
            ("14:00", "16:00"),
            ("16:00", "18:00"),
            ("18:00", "20:00"),
            ("20:00", "22:00"),
            ("22:00", "00:00")
        ]
        times=["08","10","12","14","16","18","20","22"]
        # 按摩椅的列表
        massager_ids = ["M001", "M002", "M003", "M004", "M005"]

        # 計算每個時間區間內各按摩椅的使用次數
        usage_counts_by_massager = {massager_id: [] for massager_id in massager_ids}

        for start, end in intervals:
            start_time = datetime.strptime(start, "%H:%M").time()
            end_time = datetime.strptime(end, "%H:%M").time()
            if start_time > end_time:
                end_time = datetime.strptime("23:59", "%H:%M").time()

            for massager_id in massager_ids:
                usage_count = MassageChairUsage.objects.filter(
                starttime__time__gte=start_time,
                starttime__time__lt=end_time,
                massagerid=massager_id
                ).count()
                usage_counts_by_massager[massager_id].append(usage_count)
                usage_sums_by_massager = {massager_id: sum(counts) for massager_id, counts in usage_counts_by_massager.items()}
        #print(times)
        #print(usage_counts_by_massager)
        ##產品銷售量分析長條圖
        sales_quantities = []
        sales_data = OrderDetail.objects.values('modelid').annotate(total_sales=Sum('salesquantity'))
        for data in sales_data:
            modelId = data['modelid']
            modelData = ProductModel.objects.filter(modelid = modelId)
            modelName = modelData[0].productname   
            sales_quantities.append({'modelid':modelName, 'purchasequantity': data['total_sales']})
        #print(sales_quantities)
        ##產品庫存量分析圓餅圖
        product_quantities = []
        product_data = Product.objects.values('modelid').annotate(quantity=Count('modelid'))
        for data in product_data:
            modelId = data['modelid']
            modelData = ProductModel.objects.filter(modelid = modelId)
            modelName = modelData[0].productname   
            product_quantities.append({'modelid': modelName, 'quantity': data['quantity']})
        

        #公共按摩椅的使用次數分布
        usageList = []
        usages = MassageChair.objects.all()
        for usage in usages:
            massageChairId = usage.massagerid
            massageChairCount = usage.usagecount
            massageChairInfo = {
                "id": massageChairId,
                "count": massageChairCount,
                "color": generate_random_color()
            }
            usageList.append(massageChairInfo)

    else:
        messages.error(request, '您還未登入！請輸入帳號密碼登入。')
        return redirect('/signin/')

    return render(request, 'chair.html', locals())


#登入頁面
def signin(request):
    return render(request, 'sign-in.html')


#登入判斷
def login(request):
    if request.method == 'POST':
        email = str(request.POST.get('email'))
        password = str(request.POST.get('password'))
        remember_me = request.POST.get('rememberMe')
        try:
            user = User.objects.get(userid=email, userpassword=password)
            print(user)
            request.session['is_authenticated'] = True
            request.session['user_id'] = user.employeeid

            if not remember_me:
                request.session.set_expiry(0)  # 若未勾選 Remember Me，設定 session 的過期時間為瀏覽器關閉即失效

            return redirect('/index/')  # 登入成功後導向首頁

        except ObjectDoesNotExist:
            messages.error(request, '登入失敗！請檢查您的帳號和密碼。')
            return redirect('/signin/')

    messages.error(request, '登入失敗！請檢查您的帳號和密碼。')
    return redirect('/signin/')
    

#登出判斷:
def signout(request):
    messages.success(request, '成功登出！')
    return redirect('/signin/')

        
# 生成隨機的十六進制顏色碼
def generate_random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color_code = '#{:02x}{:02x}{:02x}'.format(r, g, b)
    return color_code