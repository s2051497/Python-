# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 15:49:47 2020

@author: Jeff
"""

##07 Python 流程控制：迴圈基礎，while 迴圈、for 迴圈 

# 迴圈: 重複執行一段程式
# while 迴圈
n =1 
while n < 5:
    print("變數n的資料是: ",n)
    n += 1

# 累加 while loop
n =1 
sum = 0
while n <= 10:
    sum = sum + n
    n += 1
print(sum)

# 累加 for loop
n = 1
sum = 0
for n in range(11):
    sum = sum + n
print(sum)


# For 迴圈
for x in [4,1,2]:
    print("逐一取得列表中的資料",x)
    
for c in "Hello":
    print("逐一取得列表中的資料",c)
    
# 使用range()
# for 變數名稱 in range(3): == for 變數名稱 in [0,1,2]:
# for 變數名稱 in range(3,6): == for 變數名稱 in [3,4,5]:

    
    
    