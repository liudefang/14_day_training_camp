from tabulate import tabulate
import os
goods = [
    {"name": "电脑", "price": 1999},
    {"name": "鼠标", "price": 10},
    {"name": "游艇", "price": 20},
    {"name": "美女", "price": 998},
]

# shop_list = {
#     #"美女": {'count':0,'price':0}
#
# }  # 已购商品列表

username = input("Username:").strip()
password = input("Password:").strip()

f_path = "accounts/%s" % username
if os.path.isfile(f_path):
    f_obj = open(f_path,encoding="gbk")
    data = eval(f_obj.read() ) #把账号数据加载到内存
    #print(type(data))
    #print(data["account"])
else:
    exit("User is not exist.")
# salary = input("input your salary>:").strip()  # 初始余额
# if salary.isdigit():
#     salary = int(salary)
# else:
#     exit("salary must be an integer.")

while True:
    for index, p in enumerate(goods):
        print(index, p['name'], p['price'])
    choice = input(">>:").strip()
    if choice.isdigit():
        choice = int(choice)
        if choice >= 0 and choice < len(goods):  # 选择没问题
            # 1. 判断能否买的起，
            #    1.1 如果能买的起，就扣钱，然后加入已够商品列表
            #    1.2 如果买不起，打印买不起，继续循环
            selected_p = goods[choice]
            if selected_p['price'] <= data['account']['balance']:  # 买得起
                data['account']['balance'] -= selected_p['price']  # 扣钱
                #shop_list.append(selected_p)  # 加入购物车
                #1.判断商品名称是否在已购列表里，如果不在，初始化一条
                #2 如果在，给已存在的商品计数+1
                if selected_p['name'] not in data['shop_list']:
                    data['shop_list'][selected_p["name"]] = {"count":0,"price":0}
                data['shop_list'][selected_p["name"]]["count"] += 1
                data['shop_list'][selected_p["name"]]["price"] += selected_p["price"]

                print("Added '%s' into your shop list,your balance is \033[41;1m%s\033[0m " % (selected_p["name"],
                                                                                       data['account']['balance']))
            else:
                print("Opps,you cannot afford this product.")
        else:
            print("Invalid choice.")
    elif choice == "exit":
        print("products you've bought".center(50,'-'))
        #print(shop_list)
        tmp_shop_list = []
        total_cost = 0
        for p in data['shop_list']:
            tmp_shop_list.append([p,data['shop_list'][p]["count"],
                                  data['shop_list'][p]["price"]/data['shop_list'][p]["count"],
                                  data['shop_list'][p]["price"],
                                ])
            total_cost += data['shop_list'][p]["price"]
        tmp_shop_list.append(["总价","","",total_cost])

        print(tabulate(tmp_shop_list,headers=['商品','数量','单价','总价'],tablefmt="grid"))
        print("Your balance is %s, good luck." % data['account']['balance'])

        #save to db
        f = open(f_path,'w',encoding="GBK")
        f.write(str(data))
        f.close()
        break



