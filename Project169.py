# -*- coding: utf-8 -*-
"""
Created on Sun Mar 25 12:55:02 2018
Define f(0)=1 and f(n) to be the number of different ways n can be expressed as a sum of integer powers of 2 using each power no more than twice.

For example, f(10)=5 since there are five different ways to express 10:

1 + 1 + 8
1 + 1 + 4 + 4
1 + 1 + 2 + 2 + 4
2 + 4 + 4
2 + 8

What is f(10**25)?
@author: byron
"""
from math import *
import matplotlib.pyplot as plt
import numpy


def subset_sum(numbers, target, partial=[],solutions = set()):
    s = sum(partial)
    # check if the partial sum is equals to target
    if s == target: 
        solutions.add(tuple(partial))
#        if not partial in solutions:
#            solutions.append(partial)
           # print "sum(%s)=%s" % (partial, target)
            
    if s >= target:
        return len(solutions)   # if we reach the number why bother to continue

    for i in range(len(numbers)):
        n = numbers[i]
        remaining = numbers[i+1:]
        subset_sum(remaining, target, partial + [n],solutions) 
        

    return len(solutions)

def F(n):
    largestPower = int(floor(log(n,2)))
    powers = range(largestPower+1) + range(largestPower+1)
    powers.sort(reverse = True)
    numbers = [pow(2,x) for x in powers]
    numbers.sort()

    return subset_sum(numbers,n,partial = [],solutions = set())




if __name__ == '__main__':
    #F(9)
    N = 4
    plt.clf()
    seeds = [2]
    for seed in seeds:
        X = range(1,N+1)
        X = [seed*pow(5,x) for x in X]

        R = map(F,X)
        plt.plot(R)
    
    names = map(str,seeds)
    plt.legend(names)
    
#    golden = (1 + 5 ** 0.5) / 2
#    N = 2**7
#    print F(N)
#    plt.clf()
#    X = numpy.arange(1,N+1)
#    R = 0*X
#
#    for i in X:
#        R[i-1] = F(i)
#       # print bin(i), bin(R[i-1])
#    plt.plot(X,R)
#    R2 = R[:N/2]
#    for i in range(2):
#        R2 = numpy.append(R2,golden*R[N/4:N/2]) 
#        
# 
#    R2 =  map(round,R2)
#    plt.plot(X,R2)