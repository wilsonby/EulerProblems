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
import numpy as np



def subset_sum(powers,numPowers,target,solutions = set(),j = 0):

   # print j
    s = np.dot(powers,numPowers)
    
    if s== target:
        solutions.add(tuple(numPowers))

    if s>= target:
        return len(solutions)
    if j<len(numPowers):
        
        for i in range(3):
            numPowers[j] = i
            subset_sum(powers,numPowers,target,solutions,j+1)
        numPowers[j] =0
        
    return len(solutions)

    

def FSmallN(n):
    '''Nieve solution which is solves with iteration. Scales badly '''
    if n>1000:
        return -1

    largestPower = int(floor(log(n,2)))
    powers = 2**np.arange(largestPower,-1,-1)
    
    numPowers = np.zeros(len(powers))
    
    solutions = set()
    A = subset_sum(powers, numPowers,n,solutions)
    return A




def findIteration(solution,newSolutions):
    for i in range(len(solution)-1):
        if solution[i]>0 and solution[i+1]==0:
            newSolution = list(solution) #Create a new Solution
            newSolution[i] = newSolution[i]-1 
            newSolution[i+1] += 2
            newSolutions.add(tuple(newSolution))
    

def F(n,solutions = []):
    
    newSolutions = set()
    numSolutions = 0
    if len(solutions) ==0:
        solutions = [map(int, str(bin(n))[2:])] #Convert to binary and make into list
        numSolutions += 1

    for solutioni in solutions: #For each solution in thing
        #Find all of the 
        findIteration(solutioni,newSolutions)        
    print(len(newSolutions))
    numSolutions += len(newSolutions)
    if len(newSolutions)>0:
        solutions = None #Clear the memory spot of solutions
        numSolutions += F(n,newSolutions)
        
    return numSolutions

if __name__ == '__main__':
    print 'num solutions', F(10**18)
#    N = 10**np.arange(1,10)
#    plt.plot(map(F,N))
#    
    #Debugging    
#    R = range(1,100)
#    A =  map(FSmallN,R)
#    B = map(F,R)
#    print A ==B
#    
#    
