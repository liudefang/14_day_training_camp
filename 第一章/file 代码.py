

# r read
# w write
# a append追加
#
# f = open("test.txt","w") #创建文件
#
# f.write("hello world\n")
# f.write("hello world2\n")
#
# f.close()

# f = open("test.txt","r") #读文件

# data  = f.readline() #读一行
# data2  = f.readline() #读一行

#
# print(f.readlines())

f = open("test.txt","a") #读文件
f.write('new line')
