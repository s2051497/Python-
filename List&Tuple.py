# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 15:12:03 2020

@author: Jeff
"""
## 04
# List & Tuple 兩種有序列表
""" 基本索引運用
    連續資料處理 
    取得列表長度
    巢狀列表
    Tuple中的資料不可變動
    """

# 有序可變動列表 List [DATA]
grades = [10, 20, 30, 40, 50]
print(grades[0])
grades[0] = 30
print(grades[0])

print(grades)
grades[2:4+1] = [] #沒+1則不包含原本那項(不包含第4項)
print(grades)

grades = grades + [20, 30 , 40]
print(grades)

# 巢狀列表
data = [[3,4,5],[6,7,8]]
print(data[0])
print(data[0][1]) # 第一層第二個值

print(data)
data [0][0:2] = [5,5,5] #要留意[x:y]的後者是不在計算內的。
print(data)

# 有序不可變動列表 Tuple (Data)
data = (3,4,5)
#data[0] = 5 #會出現錯誤 TUPLE資料無法變動

##05 Python 集合、字典的基本運算 - Set、Dictionary
print("05 Python 集合、字典的基本運算 - Set、Dictionary")

####### 集合的運算 #######
s1 = {3,4,5}
print(3 in s1)
print(3 not in s1)
print(10 in s1)
print(10 not in s1)

# 交集(&):兩個集合中相同的資料
s2 = {4,5,6,7}
s3 = s1 & s2 
print("s3 =",s3,"(交集)")

# 聯集(|):取兩個資料中所有的資料 (但不重複)
s4 = s1 | s2 
print("s4 =",s4,"(聯集)")

# 差集(-): 從 s1中減去和 s2 重疊的部分
s5 = s1 - s2 
print(s5)
s6 = s2 -s1
print(s6)

# 反交集(^): 取兩個集合中部重複的地方
s7 = s1 ^ s2
print(s7)

# Set 字串 : 把字串的字母拆解成集合
s = set("Hello") # 無順序性
print(s)
print("H" in s)


###### 字典的運算 Key-Value Pairs ######
dic = {"apple":"蘋果","banana":"香蕉"}
print(dic["apple"])

dic["apple"] = "大蘋果"
print(dic["apple"])

# 判斷 Key 是否存在
print("apple" in dic) 
print("cake" in dic) 

# 刪除字典中的鍵值對 
print(dic)
del dic["apple"]
print(dic)

# 從列表[]的資料產生字典{}(字典運算)
# dic = {x:x*2 for x in [列表]}
a = [4,5,6]
dic = {x:x*2 for x in a}
print(dic)

