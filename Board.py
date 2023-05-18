from Block import Block, shape2, shape3,shape4,shape5,shape6
import random

class Board:
    def __init__(self):
        
        self.type1 = Block()
        self.type2 = shape2()
        self.type3 = shape3()
        self.type4 = shape4()
        self.type5 = shape5()
        self.type6 = shape6()
        
        self.score = 0
        
        self.board = [[0] * 20 for _ in range(15)]
        
        theshapes = [self.type1, self.type2, self.type3, self.type4, self.type5, self.type6]

        self.current_direction = random.randint(0, 5) #[0,5]
        self.cur_block = theshapes[self.current_direction]
        
    # check if current block is valid
    
    # x is for numbers in columns, and y is for numbers in rows.
    def isBlockValid(self, x:int, y:int)->bool:
        shape = self.cur_block.getShape()
        height, width = self.cur_block.getDimensions() # get the dimensions of the block shape
        valid = True # initialize it to True
        for i in range(height):
            for j in range(width):
                if shape[i][j] == 1:
                    if x + i < 0 or x + i >= 15 or y + j < 0 or y + j >= 20 or self.board[x+i][y+j] == 1:

                        valid = False
                        break
                
            if valid == False:
                break
        return valid

    
    # move the block downward by 1 positon if the move is valid, otherwise do nothing 
    def tryMoveDown(self) -> None:
        # your code here
        if self.cur_block.x != 15-1 and self.isBlockValid(self.cur_block.x+1, self.cur_block.y):
            self.cur_block.moveDown()
            
        else:
            self.dump()
            self.putNewBlock()
        return
    
    # write current shape to the board permanently
    def dump(self)->None:
        shape = self.cur_block.getShape()
        for i in range(0,len(shape)):
            for j in range(0,len(shape[0])):
                if shape[i][j] == 1 and self.cur_block.x + i in range (0,16) and self.cur_block.y + j in range (0,21):
                    self.board[self.cur_block.x + i][self.cur_block.y + j] = 1
        return 


    # put a new block on the top of the board
    #randomly
    def putNewBlock3(self) -> None:
        
        
        theshapes = [self.type1, self.type2, self.type3, self.type4, self.type5, self.type6]

        #import random

        self.current_direction = random.randint(0, 5) #[0,5]
        self.cur_block = theshapes[self.current_direction]
        self.cur_block.x = 0
        self.cur_block.y = random.randint(0, 15)
        
        return 
    

    
    # return the current board with block on it
    # create a copy of the board, and then add the shape of the current block to the copy 
    def getView(self)->"list[list[int]]":
        tmp = [self.board[i][:] for i in range(15)]
        shape = self.cur_block.getShape()
        for i in range(len(shape)):
            for j in range(len(shape[0])):
                if (self.cur_block.x + i < 15 and 
                    self.cur_block.y + j < 20 and 
                    self.cur_block.y + j >= 0 and 
                    self.cur_block.getShape()[i][j] == 1):
                    
                    tmp[self.cur_block.x + i][self.cur_block.y + j] = 1
        return tmp


    def remove_full_rows(self):
        rows_to_remove = []
        
        # Check which rows are full
        for row in range(15):
            #all are True
            if all(self.board[row][col] != None for col in range(20)):

                rows_to_remove.append(row)
                self.score += 1
        
        # Delete full rows and move blocks down
        for row in rows_to_remove:
            del self.board[row]
            self.board.insert(0, [None] * 20)
        
            
        # Return the number of rows removed
        return len(rows_to_remove)