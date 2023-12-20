# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 14:12:55 2023

@author: 13180
"""
import numpy as np

#general random graph
def G(n):
    tmp = np.zeros((n,n))
    for i in range(n):
        for j in range(i+1,n):
            rd = np.random.randint(2)
            tmp[i,j] = rd
            tmp[j,i] = rd
    return tmp


if __name__ == '__main__':
    n = 4
    G = G(n)
    #print(G)
    np.save('G',G)
