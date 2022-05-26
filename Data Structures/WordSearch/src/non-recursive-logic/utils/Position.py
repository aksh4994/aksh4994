'''
Created on May 22, 2022

@author: akshitha_k
'''

class Position:
    ''''Class Position to define numerical position of the grid elements'''
    
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.nbrMap = {}
        self.pos = ()
          
    def __setitem__(self, position, index):
        self.nbrMap[position] = index
        
    def __getitem__(self, index):
        return (self.nbrMap.values())
    
    def __repr__(self):
        return f'({self.row}, {self.col})'
        
    def findNeighbors(self, maxRow, maxCol):
        '''Finds neighboring elements of a positional character'''
        if self.col < (maxCol - 1):
            index = Position(self.row, self.col+1)
            self.__setitem__("RIGHT", index)
            
        if self.col > 0:
            index = Position(self.row, self.col-1)
            self.__setitem__("LEFT", index)
            
        if self.row > 0:
            index = Position(self.row-1, self.col)
            self.__setitem__("TOP",index)
            
        if self.row <(maxRow - 1):
            index = Position(self.row+1, self.col)
            self.__setitem__("BOTTOM", index)
            
        if self.row < (maxRow - 1) and self.col > 0:
            index = Position(self.row+1, self.col-1)
            self.__setitem__("DIAGONAL_BOTTOM_LEFT", index)
        
        if (self.row < (maxRow - 1) and self.col < (maxCol - 1)):
            index = Position(self.row+1, self.col+1)
            self.__setitem__("DIAGONAL_BOTTOM_RIGHT", index)
            
        if (self.row > 0 and self.col > 0):
            index = Position(self.row-1, self.col-1)
            self.__setitem__("DIAGONAL_TOP_LEFT", index)
            
        if (self.row > 0 and self.col < (maxCol - 1)):
            index = Position(self.row-1, self.col+1)
            self.__setitem__("DIAGONAL_TOP_RIGHT", index)
        
        return list(self.nbrMap.values())
    
    def items(self):
        items_list=[]
        items_list.append(self.row)
        items_list.append(self.col)
        return (self.row, self.col)        
    