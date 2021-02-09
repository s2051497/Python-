# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 09:25:01 2021

@author: Jeff
"""

# 11 Python Module 模組的載入與使用
#%% sys模組
# 取得系統相關資訊
import sys

print(sys.platform) #印出作業系統
print(sys.maxsize)  #印出整數型態的最大值

# 調整搜尋模組的路徑
print(sys.path)     #印出搜尋模組的路徑
sys.path.append("Modules") #在模組的搜尋路經中，加入新的路徑

#%% 自訂模組
'''
建立幾何運算模組

建立檔案geometry.py 定義平面幾何運算的函式
'''

import geometry
dis = geometry.distance(1,1,5,5)
print(dis)

slope = geometry.slope(2,2,4,4)
print(slope)
