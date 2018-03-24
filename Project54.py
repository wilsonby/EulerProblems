# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 22:29:38 2018

@author: byron
"""
class Card(object):
    def __init__(self,number,suit):
        '''Given a string suit and number'''
        self.suit = suit
        self.number = number
        
    def __cmp__(self,other):

        return other.getValue() - self.getValue()
    
    def __str__(self):
        return self.number + self.suit
        
    def getValue(self):
        possibleCards = map(str, range(2,10))
        possibleCards.extend(['T','J','Q','K','A'])
        return possibleCards.index(self.number)
  

        

class Hand(list):
    def __cmp__(self,other):
        dRank = self.findRank() - other.findRank()
        if dRank == 0 : #Tie breaker
        
            for i in range(5):
                
                if self[i].getValue() != other[i].getValue():
                    return self[i].getValue() - other[i].getValue()
        return dRank
    
    def __str__(self):
        
        S = ''
        for i in range(len(self)):
            S += self[i].__str__() + ' '
            
        
        return S
        
    def hasPair(self):
        self.sort()  
        for i in range(len(self)-1):
            if self[i].number == self[i+1].number:
                self.insert(0, self.pop(i))
                self.insert(0, self.pop(i+1)) #bring the pair to front
                return 1
        return 0
                
    def hasTwoPair(self):
        if self.hasPair():
            for i in range(2,len(self)-1):
                if self[i].number == self[i+1].number:
                    self.insert(2, self.pop(i))
                    self.insert(2, self.pop(i+1)) #bring the pair to the 2 and 3 index
                    return 1
        return 0
    
    def hasThreeOfKind(self):
        if self.hasPair():
            for i in range(2,len(self)):
                if self[0] == self[i]:
                    self.insert(2,self.pop(i))
                    return 1
        return 0
    
    def hasStraight(self):
        self.sort()
        possibleCards = map(str, range(2,10))
        possibleCards.extend(['T','J','Q','K','A'])
        for i in range(len(self)-1):
            if self[i].getValue()-self[i+1].getValue() != 1:
                return 0
        return 1
        
    def hasFlush(self):
        for i in range(1,len(self)):
            if self[i].suit != self[0].suit:
                return 0
        return 1
    
    def hasFullHouse(self):
        if self.hasThreeOfKind():
            if self[3] == self[4]:
                return 1
        return 0
    
    def hasFourKind(self):
        if self.hasThreeOfKind():
            for i in range(3,4):
                if self[0] == self[i]:
                    return 1
        return 0
        
    def hasStraightFlush(self):
        if self.hasFlush():
            if self.hasStraight():
                return 1
        return 0
        
    def hasRoyalFlush(self):
        #Technically this function is not needed, as straight flush ties are
        #resolved by highest card
        if self.hasStraightFlush() and self[0].number == 'A':
            return 1
        return 0
    
    
            
    def findRank(self):
        '''given a set of 5 cards, return the int rank of the hand:
        0 High Card: Highest value card.
        1 One Pair: Two cards of the same value.
        2 Two Pairs: Two different pairs.
        3 Three of a Kind: Three cards of the same value.
        4 Straight: All cards are consecutive values.
        5 Flush: All cards of the same suit.
        6 Full House: Three of a kind and a pair.
        7 Four of a Kind: Four cards of the same value.
        8 Straight Flush: All cards are consecutive values of same suit.
        9 Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.'''
        if not len(self): #Empty Hand
            return -1
        F = (self.hasRoyalFlush,self.hasStraightFlush,self.hasFourKind,
             self.hasFlush,self.hasStraight,self.hasThreeOfKind,self.hasTwoPair,
             self.hasPair)
             
        for i in range(len(F)):
            if F[i]() ==1:
                return len(F)-i
        return 0
        



if __name__ == '__main__':
    F = open('Project54Data.txt')
    N  = 0 #Number of won hands
    for Line in F:
        L = Line.split()
        H1 = Hand()
        H2 = Hand()
        
        for i in range(5):
            
            H1.append(Card(L[i][0],L[i][1]))
            H2.append(Card(L[i+5][0],L[i+5][1]))
      
        if H1.__cmp__(H2)>0:
            N += 1
            
    F.close()