# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 17:44:42 2023

@author: Rongfeng Xie
"""
import numpy as np

def BtoS(x,n):
  a = np.zeros(n, dtype = int)
  for i in range(n):
    if ((x << i) & 2**(n-1)!= 0):
      a[i] = 1
    else:
      a[i] = 0
  return a

def HamDis(x,y,n):
    x = BtoS(x, n)
    y = BtoS(y, n)
    d = 0
    for i in range(n):
        if(x[i] != y[i]):
            d += 1    
    return d

