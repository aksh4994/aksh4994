'''
Created on May 22, 2022

@author: akshitha_k
'''

#Importing libraries
import sys
import time

from module_1.utils.Inputs import inputFile as input
from module_1.utils.wordSearch import wordSearch as wordSearch

class main():
    '''
    Program to find possible words with the elements in given grid.
    
    Computation time for 4*4 matrix: 0.357s
    Algorithm used: Recursive algorithm using Iteration
    Primary Data Structure used: Trie (to store letters in dictionary words as root and child nodes)
    
    '''
    def findWords(self):
        try:
            gridList, dictValidList = input.getInputs(self)
            found = wordSearch.solve(self, gridList, dictValidList)
            listOfWords = list(found.keys())
            if len(listOfWords) == 0:
                print(-1)
            else:
                print(len(listOfWords))
                print("\n".join(sorted(listOfWords)))
                
        except:
            print("The program terminated unexpectedly")
                       
            
        
if __name__ == '__main__':
    
    start = time.time()
    
    result = main()
    result.findWords()
    
    end = time.time()
    print("\nThe time of execution of above program is :", end-start)