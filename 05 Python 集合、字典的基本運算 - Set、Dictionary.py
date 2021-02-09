# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 16:21:25 2021

@author: Adminstrator
"""

#%% 05 Python 集合、字典的基本運算 - Set、Dictionary

#集合的運算
s1={1,3,5}
print(5 in s1)
print(7 not in s1)

s2 = {2,3,4,5}
s3 = {5,6,7,8}

s4 = (s2 & s3) #交集: 兩集合重複的值
s5 = (s2 | s3) #聯集: 兩集合全部的值(但不重複)
print(s4,s5)

s6 = s2 - s3  #差集: 從 s2 中減去和s3重複的部分
# s6 = {2,3,4}
s7 = s2 ^ s3  #反交集: 從兩個集合中取不重疊的部分
# s7 = {2, 3, 4, 6, 7, 8}
print(s6,s7)

#%% Set function 自動將字串中的文字拆解成集合
s = ("hello")
s1 = set(s)

# Test
print("H" in s1)
#False

print("h" in s1)
#True

#%% 字典 Dictionary Key - Value 配對
dic = {"蘋果":"apple","香蕉":"banana","車子":"car"}
print(dic) 
print(dic["蘋果"])    # apple
# print(dic["apple"])   # Error

# 修改字典中對應的值
dic["蘋果"] = "Apple"
print(dic)

# 判斷某物是否在dic中 (只會檢查Key 不會檢查Value)
print("house" in dic) # False
print("車子" in dic)  #True
print("car" in dic)  #False

# 刪除Dic中的項目
print(dic)
del dic["蘋果"]
print(dic)

#%% 從列表中建立Dic
# x = [2,3,4]
dic = {x:x * 3 for x in x}
#或寫成以下  
#dic = {x:x * 2 for x in [2,3,4]}

print(dic)