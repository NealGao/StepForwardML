# for in 循环
names = ['A','B','C']
for name in names:
	print(name)

sum = 0
for x in [1,2,3,4,5,6,7,8,9]:
	sum = sum+x
print(sum)

# range()生成一个整数序列，list()可以整数序列转换为list()
li = list(range(5))
res = 0
for y in li:
	res = res+y
print(res)

sum2 = 0
for z in range(101):
	sum2 = sum2+z
print(sum2)

# while
sum3 = 0
n = 99
while n >0:
	sum3 = sum3+n
	n = n-2
print(sum3)

L = ['Bart', 'Lisa', 'Adam']
for x in L:
    print('Hello, %s' % x)


while 1==1:
	print('...')