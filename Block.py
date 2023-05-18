class Block():
    def __init__(self, x:int=0, y:int=0):
        self.shapes = \
            [[[0, 1, 0, 0],
             [0, 1, 0, 0],
             [0, 1, 0, 0],
             [0, 1, 1, 0]],

             [[0, 0, 0, 0],
             [0, 0, 0, 1],
             [1, 1, 1, 1],
             [0, 0, 0, 0]],
             
             [[0, 1, 1, 0],
              [0, 0, 1, 0],
              [0, 0, 1, 0],
              [0, 0, 1, 0]],

              [[0, 0, 0, 0],
               [1, 1, 1, 1],
               [1, 0, 0, 0],
               [0, 0, 0, 0]]]

        self.x = x
        self.y = y
        self.current_direction = 0
        
    # rotate the current block counterclockwise by 90 degree
    def rotateLeft(self)->None:
        # your code here
        if self.current_direction == len(self.shapes)-1 :
            self.current_direction = 0
        else:
            self.current_direction = self.current_direction + 1

        return #self.current_direction
    
    # move the current block downward by one
    def moveDown(self)->None:
        # your code here
        self.x = self.x + 1
        return #self.x
    
    # move the current block rightward by one
    def moveRight(self)->None:
        # your code here
        
        # if limited..
        self.y = self.y + 1
        return #self.y
    
    # move the current block leftward by one 
    def moveLeft(self)->None:
        # your code here
        if self.y != 0:
            self.y = self.y - 1

        return #self.y
    
    # return current shape of the block
    def getShape(self)->"list[list[int]]":
        return self.shapes[self.current_direction]
    

    def getDimensions(self) -> tuple[int, int]:
        """
        Get the dimensions of the block shape.

        Returns:
        Tuple of (height, width)
        """
        shape = self.getShape()
        height = len(shape)
        width = len(shape[0])
        return (height, width)

    

class shape2(Block):
    def __init__(self, x:int=0, y:int=0):

        super().__init__(x, y)
        self.shapes = \
            [[[0, 1, 0, 0],
             [0, 1, 0, 0],
             [0, 1, 0, 0],
             [0, 1, 0, 0]],

             [[0, 0, 0, 0],
             [0, 0, 0, 0],
             [1, 1, 1, 1],
             [0, 0, 0, 0]],
             
             [[0, 0, 1, 0],
              [0, 0, 1, 0],
              [0, 0, 1, 0],
              [0, 0, 1, 0]],

              [[0, 0, 0, 0],
               [1, 1, 1, 1],
               [0, 0, 0, 0],
               [0, 0, 0, 0]]]
        

class shape3(Block):
    def __init__(self, x:int=0, y:int=0):
        
        super().__init__(x, y)
        self.shapes = \
            [[[1, 1, 0],
              [0, 1, 1],
              [0, 0, 0]],
             
             [[0, 0, 1],
              [0, 1, 1],
              [0, 1, 0]],
             
             [[0, 0, 0],
              [1, 1, 0],
              [0, 1, 1]],
             
             [[0, 1, 0],
              [1, 1, 0],
              [1, 0, 0]]]
        

class shape4(Block):
    def __init__(self, x:int=0, y:int=0):
        
        super().__init__(x, y)
        self.shapes = \
            [[[0, 1, 0],
              [0, 1, 0],
              [1, 1, 0]],
             
             [[0, 0, 0],
              [1, 1, 1],
              [0, 0, 1]],
             
             [[0, 1, 1],
              [0, 1, 0],
              [0, 1, 0]],
             
             [[1, 0, 0],
              [1, 1, 1],
              [0, 0, 0]]]
        
class shape5(Block):
    def __init__(self, x:int=0, y:int=0):
        
        super().__init__(x, y)
        self.shapes = \
            [[[0, 1, 0],
              [1, 1, 1],
              [0, 0, 0]],
             
             [[0, 1, 0],
              [1, 1, 0],
              [0, 1, 0]],
             
             [[0, 0, 0],
              [1, 1, 1],
              [0, 1, 0]],
             
             [[0, 1, 0],
              [0, 1, 1],
              [0, 1, 0]]]
        
class shape6(Block):
    def __init__(self, x:int=0, y:int=0):
        
        super().__init__(x, y)
        self.shapes = \
            [[[0, 1, 1],
              [1, 1, 0],
              [0, 0, 0]],
             
             [[1, 0, 0],
              [1, 1, 0],
              [0, 1, 0]],
             
             [[0, 0, 0],
              [0, 1, 1],
              [1, 1, 0]],
             
             [[0, 1, 0],
              [0, 1, 1],
              [0, 0, 1]]]
            

