# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 12:13:40 2020

@author: Jeff
"""
### 08 Python 流程控制：迴圈進階控制，break、continue、else 命令 

#　break 
n = 1 
while n < 5:
    if n == 3:
        break # 當if為True 不會執行break 會繼續進行迴圈
              # 
    n += 1
print(n)

# continue 讓迴圈強制執行下一圈
