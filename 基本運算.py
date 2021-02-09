# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 11:39:07 2020

@author: Jeff
"""

# 數字運算

# 小數除法
x = 3/6
print(x)

# 整數除法
y = 3//6
print(y)

z = 2 ** 4

# 取餘數
a = 7 % 3
print(a)

# 變數數字+1

a += 1 #等於a = a + 1 
#a -= 1 a *= 1
#a /= 3
print(a)


# 字串運算
# 跳脫
s = "Hell\"o"
print(s)
#字串串接
a = "Hello" + "World"

b = "Hello" "World"

print(a,b)

# 字串換行
s = "Hello\nWorld"

s2 = """Hello


World"""
print(s)
print(s2)

# 重複文字
s3 = "Hello " * 3 +"World"
print(s3)

# 字串會對內部的字元編號，從0開始算起
print(s3[0])
print(s3[2:5])
print(s3[3:])
print(s3[:4])
         
