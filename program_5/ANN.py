#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 12:51:47 2021

@author: Sanjay NT
"""

import numpy as np
X = np.array(([21,91],[1,5],[3,6],[2,9],[1,6],[7,6],[9,9],[7,5],[8,6],[1,91],[1,7],[9,0],[11,77],[5,7],[3,7]),dtype=float)
y = np.array(([92],[86],[89],[90],[80],[79],[62],[90],[87],[92],[77],[55],[98],[90],[81]),dtype=float)
X = X/np.amax(X,axis=0)
y = y/100

def sigmoid(x):
    return 1/(1 + np.exp(-x))

def dersig(x):
    return x*(1-x)

le = [1000,1500,2000,2500,3000,4000,7000,9000]
lr=0.1
iln=2
hln=3                                                                                                                
oln=1

wh=np.random.uniform(size=(iln,hln))
bh=np.random.uniform(size=(1,hln))
wout=np.random.uniform(size=(hln,oln))
bout=np.random.uniform(size=(1,oln))
ls = []
for j in le:
    for i in range(j):
        h1 = np.dot(X,wh)
        h = h1+bh
        hla = sigmoid(h)
        oi1 = np.dot(hla,wout)
        oi = oi1 + bout
        op = sigmoid(oi)
        
        EO = y-op
        og =dersig(op)
        dop = EO* og
        EH = dop.dot(wout.T)
        hg = dersig(hla)
        dhl = EH* hg
        wout += hla.T.dot(dop) *lr
        wh += X.T.dot(dop) *lr
    ls.append(np.square(np.subtract(y,op)).mean())

print("||epoc||-------||mean error||")
print("=============================")
for i in range(len(ls)):
    print("||"+str(le[i])+"||-------||"+str(round(ls[i],7))+"||")
print("=============================")
