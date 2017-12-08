'''
Created on 30 nov. 2017

@author: Gebruiker
'''

from Synonym import Synonym

class Word(object):
    '''
    classdocs
    '''
    
    mWord = ""
    mWordList = []
    mLetterArray = []
    
    
# Set the word to generate variations for
    def setWord(self, pWord):

        if len(pWord) == 0 :
            print("empty word")
        else :
            self.mWord = pWord
            print("Word: " + self.mWord)
            
            
# Start generating variations of the set word
    def generateWords(self):
        print ("Generate list of word synonyms")
        self.letterArray = list(self.mWord)
        self.nextWord(self.letterArray, 0)
        
    #Function nextWord(self, letterArray)
    #pre:
    # *parameter letterArray contains an array of letters 
    #post:
    # *a list of variations of the input letterArray is created by generating all possible combinations of all synonyms of all letters in the letterArray
#     
#     If 
#     
#     
#     
#      
    def nextWordVariation(self, pWordArray, pCurrLetterPos):
        print(pWordArray)
        sLetterArray = self.letterArray
        
        letter = pWordArray[pCurrLetterPos]
        
        if Synonym.numSynonyms(letter) > 0 : #If synonyms exist for this letter, continue
            #TODO: how to recognise where I am letter.synonym?
            if (Synonym.posOfSynonym(letter) >= (Synonym.numSynonyms(letter) - 1)):
                print("last synonym of this letter")
                #last synonym of this letter
                #TODO: check if this is also the last letter.
                if pCurrLetterPos == (len(pWordArray) - 1):# If so: finish the word
                    print("word done")
                # If not: set the next synonym of the next letter and reset synonym of this letter and all before to the initial synonym
                else:
                    print("word not yet done")
                    lNextLetterPos
            else :
                print("not last synonym of this letter")
                #not the last synonym of this letter
                # TODO: set the next synonym for this letter and do no more
            self.nextWord(outputWordArray, lNextLetterPos)
        else :
            return -1 #No synonyms exist for this letter return error code NICE: ignore this letter instead of throwing error
    
    
    
    #function nextLetter
    #acts as a recursive letter cursor
    #cursor can go right or left
    def nextLetter(self, pLetter, pDirection='r'):
        print("nextLetter "+ pLetter)
        outputSynonym = ""
    
        if ((pCurrSynonymPos + 1) % Synonym.numSynonyms(pLetter) >= 1):
            print("");
            
        return outputSynonym
        
    
    
    
    def __init__(self):
        
        '''
        Constructor
        '''
        