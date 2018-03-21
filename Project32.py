# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 13:31:27 2018

@author: byron
"""
import itertools
def concatNum(T):
    '''given a tuple T of single digit intergers, return the concatination of 
    the tuple as an interger'''
    S = 0
    for i in range(len(T)):
        S += T[i]*10**(len(T)-i-1)
    return S

if __name__ == '__main__':
    pandigitalProduct = set()
    
    for p in itertools.permutations(range(1,10)):
        
        P1 = concatNum(p[0:2]) * concatNum(p[2:5])
        P2 = concatNum(p[5:])
        
        if P1 == P2:
            pandigitalProduct.add(P2)
        
        P1 = p[0] * concatNum(p[1:5])

        if P1 == P2:
            pandigitalProduct.add(P2)
            

    print sum(pandigitalProduct)