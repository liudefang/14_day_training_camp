


f = open("account_db","r")
accounts = {}
for line in f: #循环文件内容
    u,p = line.split(',')
    accounts[u] = p.strip()

print(accounts)


count = 0
while count < 3:
    username = input("Username:").strip()
    password = input("Password:").strip()

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

#