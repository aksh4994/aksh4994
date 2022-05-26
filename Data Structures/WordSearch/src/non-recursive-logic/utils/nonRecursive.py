'''
Created on May 22, 2022

@author: akshitha_k
'''
from .Position import Position

class nonRecursive():
    
    def gridCharacters(self, grid):
        '''Defines numerical position for each grid character'''
        
        neighborMap = {}
        mapList = []
        for iRowIndex in range(len(grid)):
            temp = list(grid[iRowIndex].split(' '))
            for iColIndex in range(len(temp)):
                
                #Pass row and col indices to the Position class to 
                #retrieve object of Position that has 
                #map of the numerical position and grid character
                pos = Position(iRowIndex, iColIndex)
                posMap = (pos.row, pos.col)
                
                #Create a dictionary with key as the numerical index
                #and val as grid character
                neighborMap = dict({posMap: temp[iColIndex][0]})
                mapList.append(neighborMap)
        return mapList
    
    
    def findMatchingEntries(self, ch, neighborMap):
        '''Find Matching entries using the first letter of words in the dictionary'''
        matchinglist = []
        for anEntry in neighborMap:
            aList = list(anEntry.values())
            if(ch == aList[0]):
                matchinglist.append(anEntry)
        return matchinglist
        
        
    def isNextCharacterPossibleMatch(self, iIndex, row, col, word, nbrMap):
        '''Creating list of matching words in the grid'''
        
        matchingEntries = nonRecursive.findMatchingEntries(self, word[iIndex],nbrMap)
            
        #Iterating each word in the matchingEntries list from dictionary
        #Iterating each letter in the words 
        #If the letter is found in the dictionary, repeat the process for following letters 
        for anEntry in matchingEntries:
            gridIndex = list(anEntry.keys())
            rowIndex = gridIndex[0][0]
            colIndex = gridIndex[0][1]
            pos = Position(rowIndex, colIndex)
            
            #Method findNeighbors returns a list of all neighbors of a letter
            #return: [(rowIndex, colIndex)]
            posList = pos.findNeighbors(row, col)
            
            #Iterate each element present in the position
            for i in range(len(posList)):
                neighborPosition = posList[i]
                
                #check letter is present in the list of neighboring elements for the root element
                for j in range(len(nbrMap)):
                    nbrDict = nbrMap[j]
                    
                    #Repeat until all possible neighbor elements are processed
                    if neighborPosition.items() in nbrDict.keys():
                        ch = nbrDict.get(neighborPosition.items())
                        
                        #Stop when exact word match is found
                        if(ch != None and ch == word.strip()[iIndex+1]):
                            return True
        return False

