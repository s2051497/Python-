# -*- coding: utf-8 -*-

# 線的長度
def len(x1,y1,x2,y2):
    return ((x2-x1)**2 + (y2-y1)**2)**0.5

# 線的斜率
def slope(x1,y1,x2,y2):
    return (y2-y1)/(x2-x1)
