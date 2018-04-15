# -*- encoding: utf-8 -*-
# @Time    : 2018-04-14 12:34
# @Author  : mike.liu
# @File    : 列表_练习题.py

# 1、创建一个空列表，命名为names，往里面添加old_driver，rain,jack,shanshan,peiqi,black_girl元素
'''names = []

names.append('old_driver')
names.append('rain')
names.append('jack')
names.append('shanshan')
names.append('peiqi')
names.append('black_girl')

print (names)'''

# 2、往names列表里black_girl前面插入一个alex
'''names = ['old_driver', 'rain', 'jack', 'shanshan', 'peiqi', 'black_girl']
names.insert(-1,'alex')
print (names)'''
# 3、把shanshan的名字改成中文 姗姗
'''names = ['old_driver', 'rain', 'jack', 'shanshan', 'peiqi', 'black_girl']
names[3] = '姗姗'
print (names)'''

# 4、往names列表里rain的后面插入一个子列表[oldboy,oldgirl]
'''names = ['old_driver', 'rain', 'jack', 'shanshan', 'peiqi', 'black_girl']
names.insert(1,'[oldboy,oldgirl]')
print (names)'''
# 5、返回peiqi的索引
''''names = ['old_driver', 'rain', 'jack', 'shanshan', 'peiqi', 'black_girl']
index = names.index('peiqi')
print (index)'''
# 6、创建新列表[1,2,3,4,2,5,6,2]，合并入names列表
'''list = [1,2,3,4,2,5,6,2]
names = ['old_driver', 'rain', 'jack', 'shanshan', 'peiqi', 'black_girl']
names.extend(list)
print (names)'''

# 7、取出names列表中索引4-7的元素
'''names = ['old_driver', 'rain', 'jack', 'shanshan', 'peiqi', 'black_girl', 1, 2, 3, 4, 2, 5, 6, 2]
print (names[4:7])'''
# 8、取出names列表中索引2-10的元素，步长为2
'''names = ['old_driver', 'rain', 'jack', 'shanshan', 'peiqi', 'black_girl', 1, 2, 3, 4, 2, 5, 6, 2]
print (names[2:10:2])'''
# 9、取出names列表中最后3个元素
'''names = ['old_driver', 'rain', 'jack', 'shanshan', 'peiqi', 'black_girl', 1, 2, 3, 4, 2, 5, 6, 2]
print (names[-3:])'''

# 10、循环names列表，打印每个元素的索引值，和元素
'''names = ['old_driver', 'rain', 'jack', 'shanshan', 'peiqi', 'black_girl']
count = 0
for i in names:
    print (count, i)
    count += 1'''

# 11、循环names列表，打印每个元素的索引值和元素，当索引值为偶数，把对应的元素改成-1
'''names = ['old_driver', 'rain', 'jack', 'shanshan', 'peiqi', 'black_girl']
count = 0
for i in names:
    print (count, i)
    if count % 2 == 0 :
        names[count] = '-1'
        print (names)
    count += 1'''


# 12、names里有3个2，请返回第2个2的索引值，不要人肉数，要动态找（提示，找到第一个2的位置，在此基础上再找第2个）
'''names = ['old_driver',2, 'rain', 'jack',2, 'shanshan', 'peiqi', 'black_girl',2]
fist_index = names.index(2)

new_list = names[fist_index+1:]

second_index = new_list.index(2)

second_val = names[fist_index+second_index+1]
second_val = names[fist_index+second_index+1]
print (new_list,fist_index,second_index)
print (fist_index+second_index+1)'''

# 13、现有商品列表如下：
# products = [ ['Iphone8',6888],['MacPro',14800], ['小米6',2499],['Coffee',31],['Book',80],['Nike Shoes',799]]
# 需打印出这样的格式
# ---------商品列表----------
# 0. Iphone8    6888
# 1. MacPro    14800
# 2. 小米6    2499
# 3. Coffee    31
# 4. Book    80
# 5. Nike Shoes    799

'''products = [['Iphone8',6888],['MacPro',14800], ['小米6',2499],['Coffee',31],['Book',80],['Nike Shoes',799]]
print ("---------商品列表----------")
#count = 0
for index,p in enumerate(products):
    print("%s. %s   %s"  %(index,p[0],p[1]))
    #count += 1'''


# 14、写一个循环，不断的问用户想买什么，用户选择一个商品编号，就把对应的商品添加到购物车里，最终用户输入q退出时，打印购物车里边的商品列表
products = [['Iphone8',6888],['MacPro',14800], ['小米6',2499],['Coffee',31],['Book',80],['Nike Shoes',799]]
print ("---------商品列表----------")

shopping_cat = []

exit_flag = False
while not exit_flag:
    for index,p in enumerate(products):
        print("%s. %s   %s"  %(index,p[0],p[1]))

    choice = input("请输入商品的编号:")
    if choice.isdigit():
        choice = int(choice)
        if choice > 0 and choice < len(products):
            shopping_cat.append(products[choice])
            print("添加商品%s到购物车:"  %(products[choice]))
        else:
            print("商品不存在!")
    elif choice == 'q':
        if len(shopping_cat) > 0:
            print("----您已经购买的商品如下----")
            for index, p in enumerate(shopping_cat):
                print("%s. %s   %s" % (index, p[0], p[1]))
        #break
        exit_flag = True


