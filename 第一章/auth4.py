


f = open("account_db","r")
accounts = {}
for line in f: #循环文件内容
    u,p = line.split(',')
    accounts[u] = p.strip()

print(accounts)

#加载锁定的用户列表
lock_file = open("lock_file","r")
lock_users = []
for line in lock_file:
    lock_users.append(line.strip())

count = 0
first_input_val = None # 空， 占位符， 为了生成一个变量
same_to_first_input = True #存储 每次输入的用户名是否一致的状态

while count < 3:
    username = input("Username:").strip()
    password = input("Password:").strip()
    #判断用户是否被锁定
    if username in lock_users:
        print("该用户已锁定，请联系珊珊解锁。")
        exit()
    if count == 0 : # first loop
        first_input_val = username
    #second loop
    if first_input_val != username: # 代表第一次和第二次输入的用户名不一样
        #记下来对比的状态
        same_to_first_input = False
        print('--------------------------')

    if username in accounts:#在字典里
        if accounts[username] == password: # 字典里的密码等于用户输入的密码
            print("welcome ", username)
            break
        else:
            print("wrong username or password!")
    else:
        print("用户不存在!")

    count += 1

else:
    print("too many attempts!fuck off .")

    #if same_to_first_input == False: # 代表三次输入的用户名一致
    if  same_to_first_input: # 代表三次输入的用户名一致
        # 要锁定这个用户
        f = open("lock_file",'a')
        f.write("%s\n" % username)
        f.close()
        print("user is locked...")