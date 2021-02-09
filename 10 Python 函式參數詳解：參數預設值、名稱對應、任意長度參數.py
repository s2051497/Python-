# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 17:16:16 2021

@author: Jeff
"""

# 10 Python 函式參數詳解：參數預設值、名稱對應、任意長度參數

#%% 參數的預設資料
'''
def 函式名稱(參數名稱=預設資料):
    函式內部的程式碼
'''  
#程式範例
def say(msg="Hello"):
    print(msg)

say() #印出預設資料
say("Hi Python")
#%% 參數使用對應的名稱
def divide(n1,n2):
    result = n1 / n2
    print(result)

divide(2, 4)
divide(n2 = 2, n1 = 4)
#%% 無限長度個參數
'''
def函式名稱(*無限參數):
    無限參數以Tuple資料型態處理
    函式內部的程式碼

#  呼叫函式，可傳入無限數量的參數
函式名稱(資料一，資料二，資料三)
'''

# 程式範例
def say(*msgs): #以Tuple形式處理
    for msg in msgs:
        print(msg)

say("Hi","Hello","Cheers")
#%% 程式範例
#1
def power(base,exp):
    print(base**exp)
power(3,2)
#power(3) # Error

def power(base,exp=0):
    print(base**exp)
power(3)

#2
def divide(n1,n2):
    result = n1 / n2
    print(result)

divide(2, 4)
divide(n2 = 2, n1 = 4)

#3 無限/不定 參數資料 Average 
def avg(*number):
    result = 0
    for i in number:
        result = (result + i)/len(number)    
    print(result)

avg(3,4)
avg(3,4,7)
        
