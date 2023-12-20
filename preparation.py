# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 18:31:21 2023

@author: Rongfeng Xie
"""

import numpy as np
import func


G = np.load('G.npy')
n = G.shape[0]
# print(G)
# print(n)

class QAOA_Init:
    def __init__(self):
        self.n = n
        self.G = G
    
    def H_X(self):
       tmp = np.zeros((2**self.n,2**self.n))
       for i in range(2**self.n):
           for j in range(2**self.n):
               if func.HamDis(i,j,self.n) == 1:
                   tmp[i,j] = -1
       return tmp
   
    def H_R(self,r):
        tmp = np.zeros(2**self.n)
        for i in range(2**self.n):
            d = func.HamDis(i, r, self.n)
            tmp[i] = -(self.n-2*d)
        return np.diag(tmp)
    
    def E_R(self,x):
        a = func.BtoS(x,self.n)
        E = 0.0
        for i in range(self.n):
            for j in range(self.n):
                if (a[i]==a[j]):
                    E += self.G[i,j]*1
                else:
                    E += self.G[i,j]*(-1)
        return E/2

    def H_P(self):
        tmp = np.zeros(2**self.n)
        for i in range(2**self.n):
            tmp[i] = self.E_R(i)
        return np.diag(tmp)
    


if __name__ == '__main__':
    r = 0
    x = QAOA_Init()
    print(x.n)
    print(x.G)
    print(x.H_X())
    print(x.H_R(r))
    print(x.H_P())
