# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 13:31:27 2018

@author: byron
"""
import itertools
Z = range(1,10)
pandigitalProduct = set()
for p in itertools.permutations(range(1,10)):
    P1 = (p[0]*10 +p[1]) * (100*p[2] + 10*p[3] + p[4])
    P2 = 1000*p[5] + 100*p[6] + 10*p[7] + p[8]
    if P1 == P2:
        print ((p[0]*10 +p[1]),(100*p[2] + 10*p[3] + p[4]), P2)
        pandigitalProduct.add(P2)
    
    P1 = p[0]*(1000*p[1] +100*p[2] + 10*p[3] + p[4])
    P2 = 1000*p[5] + 100*p[6] + 10*p[7] + p[8]
    if P1 == P2:
        print (p[0],(1000*p[1] +100*p[2] + 10*p[3] + p[4]), P2)
        pandigitalProduct.add(P2)
        
print pandigitalProduct
print sum(pandigitalProduct)