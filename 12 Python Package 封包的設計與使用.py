# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 10:09:19 2021

@author: Jeff
"""

# 12 Python Package 封包的設計與使用 
# import 封包名稱.模組名稱 as 模組別名
'''
- 專案資料夾
    -主程式.py
    -封包資料夾
        - __init__.py #有此py檔案 此資料夾才會被認定為封包資料夾
        - 模組一.py
        - 模組二.py

- 專案資料夾
    -main.py
    -geometry
        - __init__.py #有此py檔案 此資料夾才會被認定為封包資料夾
        - point.py
        - line.py
'''
#%%
import geometry.point as pt
result = pt.distance(3,4)
print("距離",result)
        
import geometry.line
slp = geometry.line.slope(1,1,3,3)
print("斜率",slp)