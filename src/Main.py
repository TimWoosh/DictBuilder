#!/usr/bin/env python

# 
#Purpose:
# The program allows the user to create a list of word variations to be used in, for example, 
# a dictionary for guessing passwords
# 
#User stories:
# Must have: 
# *The user can load in a list of words or a single word
# *A list of word variations can be generated from a list of words or a single word
# *Variations of an input word can be created by using all possible combinations of synonyms for the letters of the word
# *The output is saved to a file
#
# Nice to have:
# *The user can specify a file name for the output to be saved to
# *The user can maintain letter synonyms e.g. synonyms for the letter 'a' could be: 'a','A','4'
# 

from Synonym import Synonym
from Word import Word
if __name__ == '__main__':
    pass


wrd = Word()
syn = Synonym()

syn.synonymAtPos("a", 1)
wrd.setWord("bed")
wrd.nextWord(wrd.mWord)
