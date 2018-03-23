# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 13:31:27 2018
Problem 32:
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
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