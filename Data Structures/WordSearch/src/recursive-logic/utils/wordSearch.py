'''
Created on May 22, 2022

@author: akshitha_k
'''
class wordSearch():
    '''Program to find the list of words in the grid'''
    
    def solve(self, grid, dictionary):
        '''Word Search'''
        
        #Creating a Trie Data Structure for each word in the dictionary
        #Trie has a root node(the first letter of word) and several children nodes
        #(containing following letters in the word)
        
        #Trie is considered to be the best datastructure for this program as it 
        #reduces the computation time and facilitates easy retrieval
        trie = wordSearch.createTrie(self, dictionary)
        found = {}
        
        #Using the word trie, each grid element and the neighboring elements is checked if it matches the 
        #root elements of the trie.
        #If match found, the neighbor then becomes the root element, and the process
        #continues till neighboring elements are exhausted
        for i, row in enumerate(grid):
            for j, letter in enumerate(row):
                nextLetters = wordSearch.retrieveNextLetter(self, trie, letter)
                if nextLetters == False:
                    continue
                wordSearch.checkWordIsInDictionary(self, nextLetters,letter,i,j,grid,trie, found,dictionary)
        return found
    
    
    def neighbors(self, point, grid):
        '''Find neighbors of each element in the grid'''
        nRows = len(grid)
        nCols = len(grid[0])
        neighbors = []
        
        #Neighbors can be elements from 8 directions (top, bottom, right, left,
        #diagonal top left, diagonal top right, diagonal bottom left, diagonal bottom right
        #These directions are specified by relative indices from the grid element
        for nextCell in [[1,0], [-1,0], [0,-1], [0,1],[1,1],[-1,1],[-1,-1], [1,-1]]:
            if(0 <= point[0] + nextCell[0] < nRows) and (0 <= point[1] + nextCell[1] < nCols):
                neighbors.append([point[0] + nextCell[0], point[1] + nextCell[1]] )
        return neighbors
    
    
    def notVisited(self, x, visited):
        '''Toggle unvisited neighbor in the grid'''
        l = len(list(filter(lambda o:o[0] == x[0] and o[1]== x[1], visited)))
        return l ==0

            
    def createTrie(self, listOfKeys):
        '''Creating Trie Data structure'''
        
        #Creating a Trie Data Structure for each word in the dictionary
        #Trie has a root node(the first letter of word) and several children nodes
        #(containing following letters in the word)
        
        #Trie is considered to be the best datastructure for this program as it 
        #reduces the computation time and facilitates easy retrieval
        trie = {}
        for key in listOfKeys:
            tmp = trie
            for letter in key:
                if letter not in tmp:
                    tmp[letter] ={}
                tmp =tmp[letter]
                
        return trie
    
    
    def retrieveNextLetter(self, trie, prefix):
        '''Retrieve the next letter of the grid based on current trie index'''
        tmp = trie
        for letter in prefix:
            if letter not in tmp:
                return False
            tmp = tmp[letter]
        return tmp
    
    
    def checkWordIsInDictionary(self, nextLetters, word, x, y, grid, trie, found,dictionary, visited=[]):
        '''Check if the word is present in the dictionary'''
        if not nextLetters:
            found[word] = 1
            return
        if word in dictionary:
            found[word] =1
        nbrs = wordSearch.neighbors(self, [x,y], grid)
        nbrs = list(filter(lambda n: grid[n[0]][n[1]] in list(nextLetters.keys()), nbrs))
        visited.append([x,y])
        for nbr in nbrs:
            if wordSearch.notVisited(self, nbr, visited.copy()):
                combinedWord = word + grid[nbr[0]][nbr[1]]
                wordSearch.checkWordIsInDictionary(self, wordSearch.retrieveNextLetter(self, trie, combinedWord), combinedWord, nbr[0], nbr[1], grid, trie, found, dictionary, visited)
        visited.pop()        
            

