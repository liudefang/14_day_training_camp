
_user = 'alex'
_passwd = 'abc123'


count = 0
while count < 3:
    username = input("Username:").strip()
    password = input("Password:").strip()

    if username == _user and password == _passwd:
        print("welcome ", username)
        break
    else:
        print("wrong username or password!")

    count += 1

else:
    print("too many attempts!fuck off .")

#