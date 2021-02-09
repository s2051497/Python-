# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 11:58:26 2021

@author: Adminstrator
"""

# 09 Python 函式基礎：定義並呼叫函式
''' 
函式: 將程式碼包裝於一區塊當中，方便隨時呼叫使用

使用步驟:
1. 定義函式
2. 呼叫函式

基本語法:
def 函示名稱(參數名稱):
    函室內程式碼
'''
# 程式範例
#1 定義一個印出Hello的函式
def sayHello():
    print("Hello")

#2 定義可以印出任何訊息的函式
def say(msg):
    print(msg)
    
#3 定義一個可以做加法的函式
def add(n1,n2):
    result = n1 + n2
    print(result)

# 呼叫函式
# 基本語法
# 函示名稱(參數資料)
#1 
sayHello()

#2
say("Hi Python")
say("Hi Function")
say(3)

#3
add(5,10)
add(2,3)

#%% 回傳值
def 函示名稱(參數名稱):
    函室內程式碼
    return # 結束函式，回傳 None

def 函示名稱(參數名稱):
    函室內程式碼
    return 資料 # 結束函式，回傳資料(回傳值)
#%%

#1
def say(msg):
    print(msg)
    return
    
value = say("Hi Funuction")
print(value)

#2
def add(n1,n2):
    result = n1 + n2
    return "Hello"

value2 = add(3,4)
print(value2)

#3 
def add(n1,n2):
    result = n1 + n2
    return result

value3 = add(4,5)
print(value3)

#%%
# 定義函式
def multiply(n1,n2):
    return n1 * n2
# 呼叫函式
#multiply() # Error
Ans = multiply(1,5)
print(Ans)

Ans2 = multiply(3, 3) + multiply(4, 4)
print(Ans2)
