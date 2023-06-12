from myapp.models import Branch, Customer, Employee, Feedback, MassageChair, MassageChairUsage, Order, OrderDetail, ProductModel, Product, Purchase, PurchaseDetail, SalesActivity, SalesOpportunity, Supplier, Visitors
from datetime import date
import random
from datetime import datetime, timedelta
from django.utils import timezone
from django.db.models import Count

def create_branches():
    # 創建分店資料
    Branch.objects.create(branchid='B001', branchname='台北分店', branchaddress='台北市中正區', branchphone='02-12345678', employeeid='E001')
    Branch.objects.create(branchid='B002', branchname='新北分店', branchaddress='新北市板橋區', branchphone='02-98765432', employeeid='E005')
    Branch.objects.create(branchid='B003', branchname='桃園分店', branchaddress='桃園市中壢區', branchphone='03-24681357', employeeid='E008')
    Branch.objects.create(branchid='B004', branchname='高雄分店', branchaddress='高雄市左營區', branchphone='07-13579246', employeeid='E001')
    Branch.objects.create(branchid='B005', branchname='台中分店', branchaddress='台中市西區', branchphone='04-56789012', employeeid='E001')

create_branches()

def create_Visitors():
    #創建訪客量資料
    Visitors.objects.create(branchid='B001', date='2022-01-31', visitorcount=300)
    Visitors.objects.create(branchid='B001', date='2022-02-28', visitorcount=250)
    Visitors.objects.create(branchid='B001', date='2022-03-31', visitorcount=270)
    Visitors.objects.create(branchid='B001', date='2022-04-30', visitorcount=320)
    Visitors.objects.create(branchid='B001', date='2022-05-31', visitorcount=400)
    Visitors.objects.create(branchid='B001', date='2022-06-30', visitorcount=330)
    Visitors.objects.create(branchid='B001', date='2022-07-31', visitorcount=370)
    Visitors.objects.create(branchid='B001', date='2022-08-31', visitorcount=290)
    Visitors.objects.create(branchid='B001', date='2022-09-30', visitorcount=330)
    Visitors.objects.create(branchid='B001', date='2022-10-31', visitorcount=400)
    Visitors.objects.create(branchid='B001', date='2022-11-30', visitorcount=380)
    Visitors.objects.create(branchid='B001', date='2022-12-31', visitorcount=340)
    
create_Visitors()

def create_customers():
    # 創建客戶資料
    Customer.objects.create(customerid='C001', customername='張三', customergender='男', customerage=30, customerprofession='軟體工程師', customerphone='0912345678', customeremail='example1@gmail.com')
    Customer.objects.create(customerid='C002', customername='李四', customergender='女', customerage=33, customerprofession='銀行員', customerphone='0923456789', customeremail='example2@gmail.com')
    Customer.objects.create(customerid='C003', customername='王五', customergender='男', customerage=41, customerprofession='教師', customerphone='0934567890', customeremail='example3@gmail.com')
    Customer.objects.create(customerid='C004', customername='陳六', customergender='女', customerage=50, customerprofession='行政人員', customerphone='0945678901', customeremail='example4@gmail.com')
    Customer.objects.create(customerid='C005', customername='張七', customergender='男', customerage=29, customerprofession='軟體工程師', customerphone='0956789012', customeremail='example5@gmail.com')
    Customer.objects.create(customerid='C006', customername='李八', customergender='女', customerage=26, customerprofession='會計師', customerphone='0967890123', customeremail='example6@gmail.com')
    Customer.objects.create(customerid='C007', customername='王九', customergender='男', customerage=33, customerprofession='教師', customerphone='0978901234', customeremail='example7@gmail.com')
    Customer.objects.create(customerid='C008', customername='陳十', customergender='女', customerage=45, customerprofession='軟體工程師', customerphone='0989012345', customeremail='example8@gmail.com')
    Customer.objects.create(customerid='C009', customername='張十一', customergender='男', customerage=32, customerprofession='教師', customerphone='0990123456', customeremail='example9@gmail.com')
    Customer.objects.create(customerid='C010', customername='李十二', customergender='女', customerage=28, customerprofession='軟體工程師', customerphone='0901234567', customeremail='example10@gmail.com')
    Customer.objects.create(customerid='C021', customername='陳二十一', customergender='男', customerage=32, customerprofession='銀行員', customerphone='0912345678', customeremail='example21@gmail.com')
    Customer.objects.create(customerid='C022', customername='王二十二', customergender='女', customerage=38, customerprofession='會計師', customerphone='0923456789', customeremail='example22@gmail.com')
    Customer.objects.create(customerid='C023', customername='張二十三', customergender='男', customerage=44, customerprofession='行政人員', customerphone='0934567890', customeremail='example23@gmail.com')
    Customer.objects.create(customerid='C024', customername='李二十四', customergender='女', customerage=52, customerprofession='銀行員', customerphone='0945678901', customeremail='example24@gmail.com')
    Customer.objects.create(customerid='C025', customername='王二十五', customergender='男', customerage=39, customerprofession='教師', customerphone='0956789012', customeremail='example25@gmail.com')
    Customer.objects.create(customerid='C026', customername='陳二十六', customergender='女', customerage=30, customerprofession='行政人員', customerphone='0967890123', customeremail='example26@gmail.com')
    Customer.objects.create(customerid='C027', customername='張二十七', customergender='男', customerage=27, customerprofession='銀行員', customerphone='0978901234', customeremail='example27@gmail.com')
    Customer.objects.create(customerid='C028', customername='李二十八', customergender='女', customerage=35, customerprofession='教師', customerphone='0989012345', customeremail='example28@gmail.com')
    Customer.objects.create(customerid='C029', customername='王二十九', customergender='男', customerage=31, customerprofession='軟體工程師', customerphone='0990123456', customeremail='example29@gmail.com')
    Customer.objects.create(customerid='C030', customername='陳三十', customergender='女', customerage=42, customerprofession='行政人員', customerphone='0901234567', customeremail='example30@gmail.com') 

create_customers()


def create_employee():
    # 創建員工資料
    Employee.objects.create(employeeid='E001', employeename='John Doe', branchid='B001', employeeposition='Manager', employeeentrydate='2022-01-01', employeephone='1234567890', employeegender='男', employeeemail='john.doe@example.com')
    Employee.objects.create(employeeid='E002', employeename='Jane Smith', branchid='B001', employeeposition='Sales Associate', employeeentrydate='2022-01-01', employeephone='9876543210', employeegender='女', employeeemail='jane.smith@example.com')
    Employee.objects.create(employeeid='E003', employeename='Michael Johnson', branchid='B001', employeeposition='Manager', employeeentrydate='2022-01-01', employeephone='5551234567', employeegender='男', employeeemail='michael.johnson@example.com')
    Employee.objects.create(employeeid='E004', employeename='Emily Davis', branchid='B001', employeeposition='Sales Associate', employeeentrydate='2022-01-01', employeephone='7779876543', employeegender='女', employeeemail='emily.davis@example.com')
    Employee.objects.create(employeeid='E005', employeename='David Wilson', branchid='B002', employeeposition='Manager', employeeentrydate='2022-01-01', employeephone='9995551234', employeegender='男', employeeemail='david.wilson@example.com')
    Employee.objects.create(employeeid='E006', employeename='Olivia Martinez', branchid='B002', employeeposition='Sales Associate', employeeentrydate='2022-01-01', employeephone='1117779876', employeegender='女', employeeemail='olivia.martinez@example.com')
    Employee.objects.create(employeeid='E007', employeename='William Anderson', branchid='B002', employeeposition='Manager', employeeentrydate='2022-01-01', employeephone='2228889999', employeegender='男', employeeemail='william.anderson@example.com')
    Employee.objects.create(employeeid='E008', employeename='Sophia Wilson', branchid='B003', employeeposition='Sales Associate', employeeentrydate='2022-01-01', employeephone='3334445555', employeegender='女', employeeemail='sophia.wilson@example.com')
    Employee.objects.create(employeeid='E009', employeename='James Thompson', branchid='B003', employeeposition='Manager', employeeentrydate='2022-01-01', employeephone='6667778888', employeegender='男', employeeemail='james.thompson@example.com')
    Employee.objects.create(employeeid='E010', employeename='Ava Johnson', branchid='B003', employeeposition='Sales Associate', employeeentrydate='2022-01-01', employeephone='9991112222', employeegender='女', employeeemail='ava.johnson@example.com')

create_employee()


def create_feedback():
    # 創建意見回饋資料
    Feedback.objects.create(feedbackid='F001', customerid='C001', satisfaction=4, employeeid='E001', orderid='O001', feedbackdate='2023-01-01', feedbacktype='正面回饋', processstatus='處理中')
    Feedback.objects.create(feedbackid='F002', customerid='C002', satisfaction=3, employeeid='E001', orderid='O002', feedbackdate='2023-01-02', feedbacktype='服務不滿意', processstatus='已處理')
    Feedback.objects.create(feedbackid='F003', customerid='C003', satisfaction=5, employeeid='E002', orderid='O003', feedbackdate='2023-01-03', feedbacktype='服務很滿意', processstatus='已處理')
    Feedback.objects.create(feedbackid='F004', customerid='C004', satisfaction=2, employeeid='E002', orderid='O004', feedbackdate='2023-01-04', feedbacktype='品質問題', processstatus='處理中')
    Feedback.objects.create(feedbackid='F005', customerid='C005', satisfaction=4, employeeid='E003', orderid='O005', feedbackdate='2023-01-05', feedbacktype='正面回饋', processstatus='已處理')
    Feedback.objects.create(feedbackid='F006', customerid='C006', satisfaction=3, employeeid='E003', orderid='O006', feedbackdate='2023-02-01', feedbacktype='服務不滿意', processstatus='處理中')
    Feedback.objects.create(feedbackid='F007', customerid='C007', satisfaction=5, employeeid='E004', orderid='O007', feedbackdate='2023-02-02', feedbacktype='服務很滿意', processstatus='已處理')
    Feedback.objects.create(feedbackid='F008', customerid='C008', satisfaction=2, employeeid='E004', orderid='O008', feedbackdate='2023-02-03', feedbacktype='品質問題', processstatus='處理中')
    Feedback.objects.create(feedbackid='F009', customerid='C009', satisfaction=4, employeeid='E005', orderid='O009', feedbackdate='2023-02-04', feedbacktype='正面回饋', processstatus='已處理')
    Feedback.objects.create(feedbackid='F010', customerid='C010', satisfaction=3, employeeid='E005', orderid='O010', feedbackdate='2023-02-05', feedbacktype='服務不滿意', processstatus='已處理')
    Feedback.objects.create(feedbackid='F011', customerid='C011', satisfaction=5, employeeid='E006', orderid='O011', feedbackdate='2023-03-01', feedbacktype='服務很滿意', processstatus='處理中')
    Feedback.objects.create(feedbackid='F012', customerid='C012', satisfaction=4, employeeid='E006', orderid='O012', feedbackdate='2023-03-02', feedbacktype='正面回饋', processstatus='已處理')
    Feedback.objects.create(feedbackid='F013', customerid='C013', satisfaction=3, employeeid='E007', orderid='O013', feedbackdate='2023-03-03', feedbacktype='服務不滿意', processstatus='處理中')
    Feedback.objects.create(feedbackid='F014', customerid='C014', satisfaction=5, employeeid='E007', orderid='O014', feedbackdate='2023-03-04', feedbacktype='服務很滿意', processstatus='已處理')
    Feedback.objects.create(feedbackid='F015', customerid='C015', satisfaction=2, employeeid='E008', orderid='O015', feedbackdate='2023-03-05', feedbacktype='品質問題', processstatus='處理中')
    Feedback.objects.create(feedbackid='F016', customerid='C016', satisfaction=4, employeeid='E008', orderid='O016', feedbackdate='2023-04-01', feedbacktype='正面回饋', processstatus='已處理')
    Feedback.objects.create(feedbackid='F017', customerid='C017', satisfaction=3, employeeid='E009', orderid='O017', feedbackdate='2023-04-02', feedbacktype='服務不滿意', processstatus='已處理')
    Feedback.objects.create(feedbackid='F018', customerid='C018', satisfaction=5, employeeid='E009', orderid='O018', feedbackdate='2023-04-03', feedbacktype='服務很滿意', processstatus='處理中')
    Feedback.objects.create(feedbackid='F019', customerid='C019', satisfaction=4, employeeid='E010', orderid='O019', feedbackdate='2023-04-04', feedbacktype='正面回饋', processstatus='已處理')
    Feedback.objects.create(feedbackid='F020', customerid='C020', satisfaction=3, employeeid='E010', orderid='O020', feedbackdate='2023-04-05', feedbacktype='服務不滿意', processstatus='處理中')

create_feedback()


def create_massagechairusage():
    # 生成按摩椅 ID 和顧客 ID 的列表
    massager_ids = ["M001", "M002", "M003", "M004", "M005"]
    customer_ids = ["C001", "C002", "C003", "C004", "C005", "C006", "C007", "C008", "C009", "C010",
                    "C011", "C012", "C013", "C014", "C015", "C016", "C017", "C018", "C019", "C020",
                    "C021", "C022", "C023", "C024", "C025", "C026", "C027", "C028", "C029", "C030"]

    # 生成 100 筆範例資料
    example_data = []

    for _ in range(100):
        massager_id = random.choice(massager_ids)
        customer_id = random.choice(customer_ids)
        total_time = random.randint(1, 12) * 5  # 隨機生成使用時間（10 到 60 分鐘之間）

        # 隨機生成開始時間（在 2023 年內的不同月份）
        start_time = timezone.make_aware(datetime(
            2023, random.randint(1, 12), random.randint(1, 28), random.randint(8, 23), random.randint(0, 59))
        )

        # 根據使用時間計算結束時間
        end_time = start_time + timedelta(minutes=total_time)

        example_data.append(MassageChairUsage(
            massagerid=massager_id,
            customerid=customer_id,
            totaltime=total_time,
            starttime=start_time,
            endtime=end_time
        ))

    # 將範例資料批量寫入資料庫
    MassageChairUsage.objects.bulk_create(example_data)

create_massagechairusage()   


def create_massagechair():
    # 創建公共按摩椅資料
    MassageChair.objects.create(massagerid='M001', branchid='B001', status='營運中', usagecount=0)
    MassageChair.objects.create(massagerid='M002', branchid='B001', status='營運中', usagecount=0)
    MassageChair.objects.create(massagerid='M003', branchid='B002', status='維修中', usagecount=0)
    MassageChair.objects.create(massagerid='M004', branchid='B003', status='營運中', usagecount=0)
    MassageChair.objects.create(massagerid='M005', branchid='B003', status='營運中', usagecount=0)

create_massagechair()

def update_usage_count():
    # 從MassageChairUsage模型中根據massagerid進行分組，並計算每個massagerid的使用次數
    usage_count = MassageChairUsage.objects.values('massagerid').annotate(count=Count('massagerid'))

    # 遍歷使用次數結果
    for data in usage_count:
        massager_id = data['massagerid']
        count = data['count']

        # 在MassageChair模型中根據massagerid更新相應的usagecount
        MassageChair.objects.filter(massagerid=massager_id).update(usagecount=count)

# 執行更新使用次數的函數
update_usage_count()


def create_order():
    # 創建訂單資料
    Order.objects.create(orderid='O001', employeeid='E001', customerid='C001', orderdate='2022-01-07', orderprice=48000)
    Order.objects.create(orderid='O002', employeeid='E001', customerid='C002', orderdate='2022-02-10', orderprice=60000)
    Order.objects.create(orderid='O003', employeeid='E002', customerid='C003', orderdate='2022-02-23', orderprice=72000)
    Order.objects.create(orderid='O004', employeeid='E002', customerid='C004', orderdate='2022-03-05', orderprice=51000)
    Order.objects.create(orderid='O005', employeeid='E003', customerid='C005', orderdate='2022-03-22', orderprice=100000)
    Order.objects.create(orderid='O006', employeeid='E003', customerid='C006', orderdate='2022-04-08', orderprice=106000)
    Order.objects.create(orderid='O007', employeeid='E004', customerid='C007', orderdate='2022-04-19', orderprice=25000)
    Order.objects.create(orderid='O008', employeeid='E004', customerid='C008', orderdate='2022-05-13', orderprice=104000)
    Order.objects.create(orderid='O009', employeeid='E005', customerid='C009', orderdate='2022-05-23', orderprice=18000)
    Order.objects.create(orderid='O010', employeeid='E005', customerid='C010', orderdate='2022-06-01', orderprice=30000)
    Order.objects.create(orderid='O011', employeeid='E006', customerid='C011', orderdate='2022-06-17', orderprice=63000)
    Order.objects.create(orderid='O012', employeeid='E006', customerid='C012', orderdate='2022-07-06', orderprice=62000)
    Order.objects.create(orderid='O013', employeeid='E007', customerid='C013', orderdate='2022-07-16', orderprice=50000)
    Order.objects.create(orderid='O014', employeeid='E007', customerid='C014', orderdate='2022-08-07', orderprice=15000)
    Order.objects.create(orderid='O015', employeeid='E008', customerid='C015', orderdate='2022-08-28', orderprice=115000)
    Order.objects.create(orderid='O016', employeeid='E008', customerid='C016', orderdate='2022-09-16', orderprice=62000)
    Order.objects.create(orderid='O017', employeeid='E009', customerid='C017', orderdate='2022-10-11', orderprice=33000)
    Order.objects.create(orderid='O018', employeeid='E009', customerid='C018', orderdate='2022-10-22', orderprice=62000)
    Order.objects.create(orderid='O019', employeeid='E010', customerid='C019', orderdate='2022-11-10', orderprice=50000)
    Order.objects.create(orderid='O020', employeeid='E010', customerid='C020', orderdate='2022-12-15', orderprice=94000)

create_order()


def create_orderdetail():
    # 創建訂單詳細資料
    OrderDetail.objects.create(orderid='O001', productid='P001', modelid='M001', salesquantity=2, salesamount=30000)
    OrderDetail.objects.create(orderid='O001', productid='P002', modelid='M002', salesquantity=1, salesamount=18000)
    OrderDetail.objects.create(orderid='O002', productid='P003', modelid='M003', salesquantity=3, salesamount=60000)
    OrderDetail.objects.create(orderid='O003', productid='P004', modelid='M004', salesquantity=1, salesamount=22000)
    OrderDetail.objects.create(orderid='O003', productid='P005', modelid='M005', salesquantity=2, salesamount=50000)
    OrderDetail.objects.create(orderid='O004', productid='P006', modelid='M002', salesquantity=2, salesamount=36000)
    OrderDetail.objects.create(orderid='O004', productid='P007', modelid='M001', salesquantity=1, salesamount=15000)
    OrderDetail.objects.create(orderid='O005', productid='P008', modelid='M005', salesquantity=4, salesamount=100000)
    OrderDetail.objects.create(orderid='O006', productid='P009', modelid='M004', salesquantity=3, salesamount=66000)
    OrderDetail.objects.create(orderid='O006', productid='P010', modelid='M003', salesquantity=2, salesamount=40000)
    OrderDetail.objects.create(orderid='O007', productid='P011', modelid='M005', salesquantity=1, salesamount=25000)
    OrderDetail.objects.create(orderid='O008', productid='P012', modelid='M004', salesquantity=2, salesamount=44000)
    OrderDetail.objects.create(orderid='O008', productid='P013', modelid='M003', salesquantity=3, salesamount=60000)
    OrderDetail.objects.create(orderid='O009', productid='P014', modelid='M002', salesquantity=1, salesamount=18000)
    OrderDetail.objects.create(orderid='O010', productid='P015', modelid='M001', salesquantity=2, salesamount=30000)
    OrderDetail.objects.create(orderid='O011', productid='P016', modelid='M001', salesquantity=3, salesamount=45000)
    OrderDetail.objects.create(orderid='O011', productid='P017', modelid='M002', salesquantity=1, salesamount=18000)
    OrderDetail.objects.create(orderid='O012', productid='P018', modelid='M003', salesquantity=2, salesamount=40000)
    OrderDetail.objects.create(orderid='O012', productid='P019', modelid='M004', salesquantity=1, salesamount=22000)
    OrderDetail.objects.create(orderid='O013', productid='P020', modelid='M005', salesquantity=2, salesamount=50000)
    OrderDetail.objects.create(orderid='O014', productid='P022', modelid='M001', salesquantity=1, salesamount=15000)
    OrderDetail.objects.create(orderid='O015', productid='P022', modelid='M003', salesquantity=2, salesamount=40000)
    OrderDetail.objects.create(orderid='O015', productid='P023', modelid='M005', salesquantity=3, salesamount=75000)
    OrderDetail.objects.create(orderid='O016', productid='P024', modelid='M002', salesquantity=1, salesamount=18000)
    OrderDetail.objects.create(orderid='O016', productid='P025', modelid='M004', salesquantity=2, salesamount=44000)
    OrderDetail.objects.create(orderid='O017', productid='P026', modelid='M001', salesquantity=1, salesamount=15000)
    OrderDetail.objects.create(orderid='O017', productid='P027', modelid='M002', salesquantity=1, salesamount=18000)
    OrderDetail.objects.create(orderid='O018', productid='P028', modelid='M003', salesquantity=2, salesamount=40000)
    OrderDetail.objects.create(orderid='O018', productid='P029', modelid='M004', salesquantity=1, salesamount=22000)
    OrderDetail.objects.create(orderid='O019', productid='P030', modelid='M005', salesquantity=2, salesamount=50000)
    OrderDetail.objects.create(orderid='O020', productid='P031', modelid='M005', salesquantity=2, salesamount=50000)
    OrderDetail.objects.create(orderid='O020', productid='P032', modelid='M004', salesquantity=2, salesamount=44000)

create_orderdetail()


def create_product():
    # 創建產品資料
    Product.objects.create(productid='P033', modelid='M001', productiondate='2021-11-01', supplierid='S001')
    Product.objects.create(productid='P034', modelid='M001', productiondate='2021-11-01', supplierid='S002')
    Product.objects.create(productid='P035', modelid='M002', productiondate='2021-11-01', supplierid='S003')
    Product.objects.create(productid='P036', modelid='M002', productiondate='2021-11-01', supplierid='S001')
    Product.objects.create(productid='P037', modelid='M002', productiondate='2021-11-01', supplierid='S002')
    Product.objects.create(productid='P038', modelid='M003', productiondate='2021-11-01', supplierid='S003')
    Product.objects.create(productid='P039', modelid='M003', productiondate='2021-11-01', supplierid='S001')
    Product.objects.create(productid='P040', modelid='M004', productiondate='2021-11-01', supplierid='S002')
    Product.objects.create(productid='P041', modelid='M004', productiondate='2021-11-01', supplierid='S003')
    Product.objects.create(productid='P042', modelid='M005', productiondate='2021-11-01', supplierid='S001')
    Product.objects.create(productid='P043', modelid='M001', productiondate='2021-11-01', supplierid='S002')
    Product.objects.create(productid='P044', modelid='M002', productiondate='2021-11-01', supplierid='S003')
    Product.objects.create(productid='P045', modelid='M003', productiondate='2021-11-01', supplierid='S001')
    Product.objects.create(productid='P046', modelid='M003', productiondate='2021-11-01', supplierid='S002')
    Product.objects.create(productid='P047', modelid='M004', productiondate='2021-11-02', supplierid='S003')
    Product.objects.create(productid='P048', modelid='M005', productiondate='2021-11-02', supplierid='S001')
    Product.objects.create(productid='P049', modelid='M005', productiondate='2021-11-02', supplierid='S002')
    Product.objects.create(productid='P050', modelid='M001', productiondate='2021-11-02', supplierid='S003')
    Product.objects.create(productid='P051', modelid='M002', productiondate='2021-11-02', supplierid='S001')
    Product.objects.create(productid='P052', modelid='M004', productiondate='2021-11-02', supplierid='S002')
    Product.objects.create(productid='P053', modelid='M001', productiondate='2021-11-02', supplierid='S003')
    Product.objects.create(productid='P054', modelid='M001', productiondate='2021-11-02', supplierid='S001')
    Product.objects.create(productid='P055', modelid='M002', productiondate='2021-11-02', supplierid='S002')
    Product.objects.create(productid='P056', modelid='M002', productiondate='2021-11-02', supplierid='S003')
    Product.objects.create(productid='P057', modelid='M003', productiondate='2021-11-02', supplierid='S001')
    Product.objects.create(productid='P058', modelid='M003', productiondate='2021-11-02', supplierid='S002')
    Product.objects.create(productid='P059', modelid='M004', productiondate='2021-11-02', supplierid='S003')
    Product.objects.create(productid='P060', modelid='M004', productiondate='2021-11-02', supplierid='S001')

create_product()


def create_productmodel():
    # 創建產品型號資料
    ProductModel.objects.create(modelid='M001', productname='Massage Chair Model A', productprice=15000, inventory=1)
    ProductModel.objects.create(modelid='M002', productname='Massage Chair Model B', productprice=18000, inventory=1)
    ProductModel.objects.create(modelid='M003', productname='Massage Chair Model C', productprice=20000, inventory=1)
    ProductModel.objects.create(modelid='M004', productname='Massage Chair Model D', productprice=22000, inventory=1)
    ProductModel.objects.create(modelid='M005', productname='Massage Chair Model E', productprice=25000, inventory=1)

create_productmodel()

def calculate_product_quantities():
    product_data = Product.objects.values('modelid').annotate(quantity=Count('modelid'))
    for data in product_data:
        modelid = data['modelid']
        quantity = data['quantity']
        ProductModel.objects.filter(modelid=modelid).update(inventory=quantity)
calculate_product_quantities()

def create_purchase():
    # 創建進貨資料
    Purchase.objects.create(purchaseid='P001', employeeid='E001', supplierid='S001', purchasedate='2022-01-01', purchaseprice=168000, purchasepayment='Credit Card')
    Purchase.objects.create(purchaseid='P002', employeeid='E002', supplierid='S002', purchasedate='2022-02-01', purchaseprice=70000, purchasepayment='Cash')
    Purchase.objects.create(purchaseid='P003', employeeid='E003', supplierid='S003', purchasedate='2022-02-15', purchaseprice=252000, purchasepayment='Cash')
    Purchase.objects.create(purchaseid='P004', employeeid='E004', supplierid='S004', purchasedate='2022-03-01', purchaseprice=245000, purchasepayment='Credit Card')
    Purchase.objects.create(purchaseid='P005', employeeid='E005', supplierid='S005', purchasedate='2022-03-15', purchaseprice=87500, purchasepayment='Cash')
    Purchase.objects.create(purchaseid='P006', employeeid='E006', supplierid='S006', purchasedate='2022-04-01', purchaseprice=217000, purchasepayment='Credit Card')
    Purchase.objects.create(purchaseid='P007', employeeid='E007', supplierid='S007', purchasedate='2022-04-15', purchaseprice=87500, purchasepayment='Cash')
    Purchase.objects.create(purchaseid='P008', employeeid='E008', supplierid='S008', purchasedate='2022-05-01', purchaseprice=224000, purchasepayment='Credit Card')
    Purchase.objects.create(purchaseid='P009', employeeid='E009', supplierid='S009', purchasedate='2022-05-15', purchaseprice=126000, purchasepayment='Cash')
    Purchase.objects.create(purchaseid='P010', employeeid='E010', supplierid='S010', purchasedate='2022-06-01', purchaseprice=52500, purchasepayment='Credit Card')
    Purchase.objects.create(purchaseid='P011', employeeid='E011', supplierid='S011', purchasedate='2022-06-15', purchaseprice=231000, purchasepayment='Cash')
    Purchase.objects.create(purchaseid='P012', employeeid='E012', supplierid='S012', purchasedate='2022-07-01', purchaseprice=217000, purchasepayment='Credit Card')
    Purchase.objects.create(purchaseid='P013', employeeid='E013', supplierid='S013', purchasedate='2022-07-15', purchaseprice=87500, purchasepayment='Cash')
    Purchase.objects.create(purchaseid='P014', employeeid='E014', supplierid='S014', purchasedate='2022-08-01', purchaseprice=63000, purchasepayment='Credit Card')
    Purchase.objects.create(purchaseid='P015', employeeid='E015', supplierid='S015', purchasedate='2022-08-15', purchaseprice=182000, purchasepayment='Cash')
    Purchase.objects.create(purchaseid='P016', employeeid='E016', supplierid='S016', purchasedate='2022-09-01', purchaseprice=227500, purchasepayment='Credit Card')
    Purchase.objects.create(purchaseid='P017', employeeid='E017', supplierid='S017', purchasedate='2022-09-15', purchaseprice=241500, purchasepayment='Cash')
    Purchase.objects.create(purchaseid='P018', employeeid='E018', supplierid='S018', purchasedate='2022-10-01', purchaseprice=203000, purchasepayment='Credit Card')
    Purchase.objects.create(purchaseid='P019', employeeid='E019', supplierid='S019', purchasedate='2022-11-01', purchaseprice=105000, purchasepayment='Cash')
    Purchase.objects.create(purchaseid='P020', employeeid='E020', supplierid='S020', purchasedate='2022-12-01', purchaseprice=140000, purchasepayment='Credit Card')

create_purchase()


def create_purchasedetail():
    # 創建進貨詳細資料
    PurchaseDetail.objects.create(purchaseid='P001', modelid='M001', purchasequantity=10, purchaseamount=105000)
    PurchaseDetail.objects.create(purchaseid='P001', modelid='M002', purchasequantity=5, purchaseamount=63000)
    PurchaseDetail.objects.create(purchaseid='P002', modelid='M003', purchasequantity=5, purchaseamount=70000)
    PurchaseDetail.objects.create(purchaseid='P003', modelid='M004', purchasequantity=5, purchaseamount=77000)
    PurchaseDetail.objects.create(purchaseid='P003', modelid='M005', purchasequantity=10, purchaseamount=175000)
    PurchaseDetail.objects.create(purchaseid='P004', modelid='M001', purchasequantity=10, purchaseamount=105000)
    PurchaseDetail.objects.create(purchaseid='P004', modelid='M003', purchasequantity=10, purchaseamount=140000)
    PurchaseDetail.objects.create(purchaseid='P005', modelid='M005', purchasequantity=5, purchaseamount=875000)
    PurchaseDetail.objects.create(purchaseid='P006', modelid='M002', purchasequantity=5, purchaseamount=63000)
    PurchaseDetail.objects.create(purchaseid='P006', modelid='M004', purchasequantity=10, purchaseamount=154000)
    PurchaseDetail.objects.create(purchaseid='P007', modelid='M005', purchasequantity=5, purchaseamount=87500)
    PurchaseDetail.objects.create(purchaseid='P008', modelid='M003', purchasequantity=5, purchaseamount=70000)
    PurchaseDetail.objects.create(purchaseid='P008', modelid='M004', purchasequantity=10, purchaseamount=154000)
    PurchaseDetail.objects.create(purchaseid='P009', modelid='M002', purchasequantity=10, purchaseamount=126000)
    PurchaseDetail.objects.create(purchaseid='P010', modelid='M001', purchasequantity=5, purchaseamount=52500)
    PurchaseDetail.objects.create(purchaseid='P011', modelid='M001', purchasequantity=10, purchaseamount=105000)
    PurchaseDetail.objects.create(purchaseid='P011', modelid='M002', purchasequantity=10, purchaseamount=126000)
    PurchaseDetail.objects.create(purchaseid='P012', modelid='M003', purchasequantity=10, purchaseamount=140000)
    PurchaseDetail.objects.create(purchaseid='P012', modelid='M004', purchasequantity=5, purchaseamount=77000)
    PurchaseDetail.objects.create(purchaseid='P013', modelid='M005', purchasequantity=5, purchaseamount=87500)
    PurchaseDetail.objects.create(purchaseid='P014', modelid='M002', purchasequantity=5, purchaseamount=63000)
    PurchaseDetail.objects.create(purchaseid='P015', modelid='M001', purchasequantity=10, purchaseamount=105000)
    PurchaseDetail.objects.create(purchaseid='P015', modelid='M004', purchasequantity=5, purchaseamount=77000)
    PurchaseDetail.objects.create(purchaseid='P016', modelid='M003', purchasequantity=10, purchaseamount=140000)
    PurchaseDetail.objects.create(purchaseid='P016', modelid='M005', purchasequantity=5, purchaseamount=87500)
    PurchaseDetail.objects.create(purchaseid='P017', modelid='M004', purchasequantity=10, purchaseamount=154000)
    PurchaseDetail.objects.create(purchaseid='P017', modelid='M005', purchasequantity=5, purchaseamount=87500)
    PurchaseDetail.objects.create(purchaseid='P018', modelid='M002', purchasequantity=5, purchaseamount=63000)
    PurchaseDetail.objects.create(purchaseid='P018', modelid='M003', purchasequantity=10, purchaseamount=140000)
    PurchaseDetail.objects.create(purchaseid='P019', modelid='M001', purchasequantity=10, purchaseamount=105000)
    PurchaseDetail.objects.create(purchaseid='P020', modelid='M002', purchasequantity=5, purchaseamount=63000)
    PurchaseDetail.objects.create(purchaseid='P020', modelid='M004', purchasequantity=5, purchaseamount=77000)

create_purchasedetail()


def create_salesactivity():
    # 創建銷售活動資料
    SalesActivity.objects.create(salesactid='A001', salesstage='第一階段',salesacttype='透過公共按摩椅或到店試坐', salesactremark='贈送虛擬按摩券或填寫意見回饋')
    SalesActivity.objects.create(salesactid='A002', salesstage='第二階段',salesacttype='邀請家人來店試坐按摩椅', salesactremark='贈送虛擬按摩券給適用人及推薦人')
    SalesActivity.objects.create(salesactid='A003', salesstage='第三階段',salesacttype='銷售促推', salesactremark='推送產品資訊、新產品介紹、確保多來幾次')
    SalesActivity.objects.create(salesactid='A004', salesstage='第四階段',salesacttype='決戰', salesactremark='送出優惠方案，期限結束即敗戰')
    SalesActivity.objects.create(salesactid='A005', salesstage='第五階段',salesacttype='交易完成', salesactremark='注重於售後服務')

create_salesactivity()


def create_salesopportunity():
    # 創建銷售機會資料
    SalesOpportunity.objects.create(salesoppid='SO021', customerid='C021', salesactid='A001', employeeid='E001', salesoppexcd='2023-05-01', salesoppexsa=15000)
    SalesOpportunity.objects.create(salesoppid='SO022', customerid='C022', salesactid='A002', employeeid='E002', salesoppexcd='2023-05-02', salesoppexsa=62000)
    SalesOpportunity.objects.create(salesoppid='SO023', customerid='C023', salesactid='A003', employeeid='E003', salesoppexcd='2023-05-03', salesoppexsa=18000)
    SalesOpportunity.objects.create(salesoppid='SO024', customerid='C024', salesactid='A004', employeeid='E004', salesoppexcd='2023-05-04', salesoppexsa=106000)
    SalesOpportunity.objects.create(salesoppid='SO025', customerid='C025', salesactid='A001', employeeid='E005', salesoppexcd='2023-05-05', salesoppexsa=115000)
    SalesOpportunity.objects.create(salesoppid='SO026', customerid='C026', salesactid='A002', employeeid='E006', salesoppexcd='2023-05-06', salesoppexsa=15000)
    SalesOpportunity.objects.create(salesoppid='SO027', customerid='C027', salesactid='A003', employeeid='E007', salesoppexcd='2023-05-07', salesoppexsa=33000)
    SalesOpportunity.objects.create(salesoppid='SO028', customerid='C028', salesactid='A004', employeeid='E008', salesoppexcd='2023-05-08', salesoppexsa=50000)
    SalesOpportunity.objects.create(salesoppid='SO029', customerid='C029', salesactid='A001', employeeid='E009', salesoppexcd='2023-05-09', salesoppexsa=94000)
    SalesOpportunity.objects.create(salesoppid='SO030', customerid='C030', salesactid='A002', employeeid='E010', salesoppexcd='2023-05-10', salesoppexsa=106000)

create_salesopportunity()


def create_supplier():
    # 創建供應商資料
    Supplier.objects.create(supplierid='S001', suppliername='供應商A', supplierphone='0912345678', supplieraddress='台北市中正區', contactperson='張先生', supplieremail='supplierA@example.com')
    Supplier.objects.create(supplierid='S002', suppliername='供應商B', supplierphone='0923456789', supplieraddress='新北市永和區', contactperson='李小姐', supplieremail='supplierB@example.com')
    Supplier.objects.create(supplierid='S003', suppliername='供應商C', supplierphone='0934567890', supplieraddress='台中市西屯區', contactperson='王先生', supplieremail='supplierC@example.com')

create_supplier()




