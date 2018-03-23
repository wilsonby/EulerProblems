# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 14:43:06 2018
The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
@author: byron
"""
from fractions import Fraction
from numpy import prod

def checkResult(numerator,denominator, j,k,SuccessN,SuccessD):
    if numerator/denominator == float(j)/k and numerator < denominator :
        #print(numerator,denominator) #Print to ensure results are non-trivial
        SuccessN.append(int(numerator))
        SuccessD.append(int(denominator))
        
if __name__ == '__main__':
    SuccessN = []
    SuccessD = []
    for i in range(1,10): #Trivial Results for i,j or k =  0 
        for j in range(1,10):
            for k in range(1,10):
                #First numbers being crossed out
                numerator = i*10. + j
                denominator= i*10. +k
                checkResult(numerator,denominator, j,k,SuccessN,SuccessD)
                
                #Second numbers being crossed out                 
                numerator = j*10. +i
                denominator =k*10. + i
                checkResult(numerator,denominator, j,k,SuccessN,SuccessD)
                
                #First in num, second in den
                numerator = i*10. +j
                denominator = 10*k + i
                checkResult(numerator,denominator, j,k,SuccessN,SuccessD)
                    
                #second in num, first in den
                numerator = j*10. +i
                denominator = i*10. + k
                checkResult(numerator,denominator, j,k,SuccessN,SuccessD)
                
    print(Fraction(prod(SuccessN),prod(SuccessD)))
                