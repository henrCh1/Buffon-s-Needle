# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 18:25:23 2023

@author: 86319
"""

# 其实这里根据已知的pi然后计算出概率算出自己的pi
import numpy as np
import matplotlib.pyplot as plt
import math

# 针的长度
l = 0.520
# 平行线宽度
a = 1.314
# 试验次数n
n = 10000
# 相交次数
count = 0
# 在0~a/2之间产生n个随机数
x = np.random.rand(1, n) * a / 2
phi = np.random.rand(1, n) * math.pi

def test(times):
    global count
    for i in range(0, times):
        if x[0][i] <= 1 / 2 * math.sin(phi[0][i]):
            count = count + 1
            plt.scatter(phi[0][i] ,x[0][i] ,c='r',marker='.')
        else:
            plt.scatter(phi[0][i], x[0][i], c='g',marker='.')
test(n)

p = count / n
mPi = (2 * 1) / (a * p)
print("蒙特卡洛方法得到Pi为：",mPi)
plt.show()
