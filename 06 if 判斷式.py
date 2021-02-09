# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 10:47:59 2020

@author: Jeff
"""
## 06 Python 流程控制：if 判斷式

# 判斷式

if True:
    print("True 執行")
else:
    print("False 執行")
    
if False:
    print("True 執行")
else:
    print("False 執行")

"""
# if 範例1
x = input("請輸入數值: ") # 使用者輸入(字串)
x = int(x) # 將字串轉換成數字型態

if x > 200:
    print("x 大於 200")
elif x > 100:
    print("x 大於 100, 小於 200")
else:
    print("x 小於 100")
"""

#範例2 #四則運算
'''
n1 = int(input("請輸入第一個數值: "))
n2 = int(input("請輸入第二個數值: "))

ans = n1 + n2
print(ans)
'''

# 範例3

n3 = int(input("請輸入第一個數值: "))
n4 = int(input("請輸入第二個數值: "))
op = input("請輸入運算方式(+,-,*,/): ")

if op == "+":
    print(n3 + n4)
elif op == "-":
    print(n3 - n4)
elif op == "*":
    print(n3 * n4)
elif op == "/":
    print(n3 / n4)
else:
    print("不支援的運算")
    
    
# Python 至 3.6版本不支援 Switch 功能 (別的語言用於判斷的方法之一)
 
