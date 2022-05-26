'''
Created on May 22, 2022

@author: akshitha_k
'''
#Importing libraries
import sys
import time

from module_2.utils.Inputs import inputFile as input
from module_2.utils.nonRecursive import nonRecursive as wordSearch

logs_file_path = "./app.log"
sys.stdout = open(logs_file_path, "w", buffering=1, encoding='utf-8')

class main():
    '''
    Program to find possible words with the elements in given grid.
    
    Computation time for 4*4 matrix: 0.4289s
    Algorithm used: Non-Recursive algorithm using Iteration
    Primary Data Structure used: HashMap (to store position of grid elements)
    
    '''
    
    '''This program follows a non-recursive algorithm to retrieve possible words 
    from the dictionary'''
    def findWords(self):
        
        try:
            #Get inputs from grid.txt and englishwords.txt
            grid, words, maxRows, maxCols = input.getInputs(self)
            
            #Create a HashMap of object Position that defines the index of grid element
            #(rowIndex, colIndex) and the grid element
            #This creates a list of dict of {Position(row,col), grid Character}
            gridMap = wordSearch.gridCharacters(grid)
            
            matchedWords = []
            possibleMatch = False
            
            #Iterates each word from the dictionary, check if letters of these words 
            #matches the neighbor elements in the grid
            for word in words:
                for iIndex in range(len(word.strip())):
                    if(iIndex < len(word.strip()) -1):
                        possibleMatch = wordSearch.isNextCharacterPossibleMatch(iIndex, maxRows, maxCols, word.strip(), gridMap);
                        if(possibleMatch == False):
                            break
                        elif(possibleMatch == True):
                            matchedWords.append(word)
                            
            print(len(matchedWords))
            print("\n".join(sorted(matchedWords)))
                
        except:
            print("The program terminated unexpectedly")
                                
        
if __name__ == '__main__':
    
    start = time.time()
    
    result = main()
    result.findWords()
    
    end = time.time()
    print("\nThe time of execution of above program is :", end-start)