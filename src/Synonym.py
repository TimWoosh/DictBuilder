#!/usr/bin/env python

class Synonym(object):
        
    
    synonyms = {
        'a': ['a','A','4'],
        'b': ['b','B','8'],
        'c': ['c','C'],
        'd': ['d','D'],
        'e': ['e','E','3'],
        'f': ['f','F'],
        'g': ['g','G','9'],
        'h': ['h','H','#'],
        'i': ['i','I','!'],
        'j': ['j','J']
        }
    
    
    s_a = ('a','A','4')
    s_b = ('b','B','8')
    s_c = ('c','C')
    s_d = ('d','D')
    s_e = ('e','E','3')
    
    
    #Letter index
    _a = 0
    _b = 1
    _c = 2
    _d = 3
    _e = 4
    _f = 5
    _g = 6
    _h = 7
    _i = 8
    _j = 9
    _k = 10
    _l = 11
    _m = 12
    _n = 13
    _o = 14
    _p = 15
    _q = 16
    _r = 17
    _s = 18
    _t = 19
    _u = 10
    _v = 21
    _w = 22
    _x = 23
    _y = 24
    _z = 25
    _1 = 26
    _2 = 27
    _3 = 28
    _4 = 29
    _5 = 30
    _6 = 31
    _8 = 32
    _7 = 33
    _9 = 34
    _0 = 35

    '''
    classdocs
    '''
    def synsForLetter(self, mLetter):
        print(self.synonyms[mLetter])
        
        
    # Function synonymAtPos(self, mLetter, pos)
    # Pre:
    # *parameter pLetter contains one character
    # Post:
    # *The number of synonyms is returned
    # *If no synonyms are defined for the letter, 0 is returned  
    def synonymAtPos(self, mLetter, pos):
        if mLetter in self.synonyms :
            if pos < len(self.synonyms[mLetter]) :
                lLetter = self.synonyms[mLetter][pos]
                print(lLetter)
                return lLetter
            else:
                print("pos out of bounds")
        else:
            print("letter not found in dictionary")
            return -1

    def posOfSynonym(self, pLetter):
        if pLetter in self.synonyms :
            print("letter found: " + pLetter)
            lPos = self.synonyms.index(pLetter)
            return lPos
        else :
            print("Letter cannot be found")
            return -1
        
    # Function numSynonyms(self, pLetter)
    # Pre:
    # *parameter pLetter contains one character
    # Post:
    # *The number of synonyms is returned
    # *If no synonyms are defined for the letter, 0 is returned
    def numSynonyms(self, pLetter):
        if self.posOfSynonym(pLetter) >= 0 :
            return len(self.synonyms[pLetter])
        else :
            return 0
        
    def getNextSynonym(self, pLetter, pCurrSynonym): #Get the next synonym in line, as long as pCurrSynonym is not the last synonym
        if self.posOfSynonym(pLetter) >= 0 :
            return self.synonymAtPos(pLetter, self.posOfSynonym(pCurrSynonym) + 1)
        else:
            return -1
        
    def __init__(self):
        '''
        Constructor
        '''
        