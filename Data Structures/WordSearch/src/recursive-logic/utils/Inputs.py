'''
Created on May 22, 2022

@author: akshitha_k
'''
import sys
sys.path.append('.')
import config


class inputFile():
    '''Retrieve elements in Grid and Dictionary'''
    
    def getNRowCol(self, gridMatrix):
        '''Get Number of rows and cols in grid''' 
        # #M*N matrix M rows and N columns
        matrix = gridMatrix.split(' ')
        return matrix[0], matrix[1]
    
        
    def getGrid(self, gridInputFile, gridMatrix, grid):
        '''Get elements in the grid in the form of matrix'''
        gridMatrix = gridInputFile.readline().rstrip('\n').lower()
        while gridMatrix != '':  
            grid.append(gridMatrix.split(' '))
            gridMatrix = gridInputFile.readline().rstrip('\n').lower()
        return grid
    
    
    def has_all(self, chars, string):
        '''Check if all letters in the words present in dictionary matches with 
        letters in the grid'''
        return all([char in string for char in chars])
    
         
    def getValidWords(self, grid, dictionaryFile, dictValidList):
        '''Make a list of words having letters made up of letters in the grid'''
        g_list = []
        for i in grid:
            for j in i:
                g_list.append(j.lower())
                
        dictText = dictionaryFile.readline().rstrip('\n')
        
        while dictText != '':
            if(inputFile.has_all(self, dictText, g_list) == True):
                dictValidList.append(dictText)
            dictText = dictionaryFile.readline().rstrip('\n')  
            
        return dictValidList
    
        
    def getInputs(self):
        '''Reading Grid.txt and englishwords.txt input file''' 
        gridInputFile = open(f'{config.GRID_FILE_PATH}', 'r')
        dictionaryFile = open(f'{config.DICT_FILE_PATH}', 'r')
        
        gridMatrix = gridInputFile.readline().rstrip('\n')
        
       
        grid = []
        dictValidList = []
        
        #Get elements in the grid 
        self.grid = inputFile.getGrid(self, gridInputFile, gridMatrix, grid)
         
        #Filter only words with letters contained in the grid 
        #This computation reduces the time taken for the program to perform word search
        #Also performance time is speeded up by searching only valid words
        self.dictValidList = inputFile.getValidWords(self, grid, dictionaryFile, dictValidList)
            
        # Finalization    
        gridInputFile.close()
        dictionaryFile.close()
        
        return self.grid, self.dictValidList