#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 条件判断
age = 3
if age >= 18:
	print('your age is',age)
	print('adult')
elif age >= 6:
	print('teenager')
else:
	print('your age is',age)
	print('kid')


# input
birth = input('birth:')
if int(birth) < 2000: # int() 字符串转换为整数
	print('00前')
else:
	print('00后')

