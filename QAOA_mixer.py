# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 21:40:56 2023

@author: Rongfeng Xie
"""

import numpy as np
from scipy.linalg import expm
from preparation import QAOA_Init

class QAOA_Mixer:
    
    def __init__(self,r,a,b,c):
        self.r = r
        self.a = a
        self.b = b
        self.c = c
    
    def psi_init(self):
        QI = QAOA_Init()
        H_tmp = QI.H_X() + self.c*QI.H_R(self.r)
        e,v =  np.linalg.eigh(H_tmp)
        idx = np.argsort(e)
        vcs = v[:,idx]
        return vcs[:,0]
    
    def psi_final(self):
        QI = QAOA_Init()
        u_a = expm(-1j*self.a*QI.H_P())
        u_b = expm(-1j*self.b*QI.H_X())
        u_c = expm(-1j*self.c*QI.H_R(self.r))
        psia = np.matmul(u_a,self.psi_init())
        psib = np.matmul(u_b,psia)
        return np.matmul(u_c,psib)
    
    def Energy(self):
        QI = QAOA_Init()
        Hp = QI.H_P()
        w = self.psi_final()
        w1 = np.conjugate(w)
        tmp = np.matmul(Hp,w)
        return np.real(np.matmul(w1,tmp))
    


if __name__ == '__main__':
    r = 0
    a = 0.8
    b = 0.4
    c = 0
    x = QAOA_Mixer(r, a, b, c)
    print(x.Energy())