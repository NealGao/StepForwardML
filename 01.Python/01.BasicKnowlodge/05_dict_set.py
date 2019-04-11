# -*- coding: utf-8 -*-

# dict
d={'Michael':80,'Bob':90,'Tracy':75}
print(d['Michael'])

# put value into dict by key
d['admin']=67
print(d['admin'])

# if set the key by different value,the later one will overvide the previous one
d['Jack']=23
# print(d['Jack'])

d['Jack']=15
print(d['Jack'])

# error will arise will the key not exist
# two ways to check if the key exist in dict,the 1'st as below
res='Thomas' in d
print(res)

# 2nd way is to the method get()
res1=d.get('Thomas')
print(res1)
res2=d.get('Thomas',-1)
print(res2)

# use the pop(key) method to delete one key,the value of this key will also be deleted 
print(d)
d.pop('Bob')
print(d)

# dict与list区别
# dict查找和插入的速度快，不会随着key的增加而变慢
# 占用大量内存，内存浪费很多

# list刚好相反
# 查找和插入的时间随着元素的增加而增加
# 占用空间小，浪费内存很小 
# dict和list的区别就是计算机的空间和时间的矛盾：以时间换取空间或者以空间换取时间

# dict可以用在需要高速查找的地方，需要注意，dict的key必须是不可变对象
# 字符串，整数都是不可变对象，而list是可变的，不能作为dict的key

#set
# set只存储key,由于key不能重复，在set中，没有重复的key
# 把list转换为set
s=set([1,2,3])
print(s)

# 重复的元素会被字段过滤掉（使用set对list进行去重）
s=set([1,1,2,2,3,3])
print(s)

# add(key)可以添加元素到set中，重复添加无效果
s.add(4)
print(s)

s.add(4)
print(s)

# remove(key)可以删除元素,如果key不存在，则报错-->移除之前应该下判断key是否存在
s.remove(4)
print(s)

# set也不可以放入可变对象







