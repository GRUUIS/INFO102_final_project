from Board import Board
from KBHit import KBHit
import pygame
import time


class Game:
    def __init__(self):
        self.board = Board()
        self.kb = KBHit() # a class that read input from the keyboard

        pygame.mixer.init() # originize
        # music files
        self.sound1 = pygame.mixer.Sound("bgm.wav")
        self.sound2 = pygame.mixer.Sound("forasd.wav")
        self.sound3 = pygame.mixer.Sound("clear.wav")
        self.sound4 = pygame.mixer.Sound("ending.wav")

        # channel for music
        self.channel1 = pygame.mixer.Channel(0)
        self.channel2 = pygame.mixer.Channel(1)
        self.channel3 = pygame.mixer.Channel(2)
        self.channel4 = pygame.mixer.Channel(3)
        self.num = 1000

        #to pause
        self.paused = False
        
        #for different modes
        #for move_limited mode
        self.mode = 0
        
        self.num_moves = 0
        self.move_limitation = -1
        
        #for time-limited mode
        self.thestart = 0
        self.duration = 0
        
        #for the main game's loop to continue playing
        self.Game_now = True
        
        



    # start the game
    def run(self) -> None:
        
        # play different music using channels
        self.channel1.play(self.sound1, loops=-1)

        #to choose the game mode: [1] time limited mode [2] endless mode
        while True:
            mode = input("choose game mode: input 1 for time-limited mode, 2 for move-limited mode, and 3 for endless mode: ")
            if mode == "3":
                self.mode = 3
                self.channel2.play(self.sound2) 
                #add music effect to the decision making part
                break
            elif mode == '1':
                self.mode = 1
                self.channel2.play(self.sound2)
                break
            elif mode == '2':
                self.mode = 2
                self.channel2.play(self.sound2)
                break
            
        #to choose the game speed as the level
        
        while True:
            lv = input("choose speed level: input 1/2/3 [1: slow, 2: modest, 3:fast] ")
            if lv == '1':
                self.num = 0.7
                self.channel2.play(self.sound2)
                break

            elif lv == '2':
                self.num = 0.58
                self.channel2.play(self.sound2)
                break

            elif lv == '3':
                self.num = 0.35
                self.channel2.play(self.sound2)
                break
                
        if self.mode == 1:
            self.run_time_limited()
            
        elif self.mode == 2:
            self.run_move_limited()
            
        elif self.mode == 3:
            self.function_run() #directly call the origin function
                
    def run_time_limited(self) -> None:
        # get the duration for the time-limited mode
        while True:
            duration_str = input("Enter the duration for the time-limited mode (in seconds): ")
            try:
                self.duration = float(duration_str)
                break
            
            except ValueError:
                print("Invalid input. Please enter a valid number.")
            except Exception:
                print("something wrong")

            
        self.thestart = time.time()
        self.channel2.play(self.sound2)

        # game loop
        self.function_run()
            
            
    def run_move_limited(self) -> None:
        # get the move limit for the move-limited mode
        while True:
            move_limit_str = input("Enter the move limit for the move-limited mode: ")
            try:
                move_limit = int(move_limit_str)
                if move_limit > 0:
                    break
                else:
                    print("Move limit must be a positive integer.")
            except ValueError:
                print("Please enter a valid integer.")
            except Exception:
                print("something wrong")
                
        self.move_limitation = move_limit
        self.channel2.play(self.sound2) #add music effect to the decision making part

        # game loop
        self.function_run()
        
        
    
    # def endless_mode(self) -> None:
    #     self.function_run()
        
        

    def function_run(self):
        start = time.time()
        

        while self.Game_now:
            self.display3()
            if self.display3() == False:
                while True:
                    a = input('stop now. continue if input i: ')
                    if a == 'i':
                        self.paused = False
                        break
            
            #to differ the modes, add a condition with self.mode
            if self.mode == 2 and self.num_moves >= self.move_limitation:
                self.Game_now = False
                
            elif self.mode == 1 and time.time() - self.thestart >= self.duration:
                self.Game_now = False #this will break the while loop to end the game
                

            if self.kb.kbhit():
                key = self.kb.getch()  # Returns a keyboard character after kbhit() has been called.
                if key == 'a':  # move left
                    if self.board.isBlockValid(self.board.cur_block.x, self.board.cur_block.y - 1):
                        self.board.cur_block.moveLeft()
                        self.num_moves += 1 #for move-limited moves
                        #self.display3()
                        self.channel2.play(self.sound2)
                elif key == 'd':  # move right
                    if self.board.isBlockValid(self.board.cur_block.x, self.board.cur_block.y + 1):
                        self.board.cur_block.moveRight()
                        self.num_moves += 1
                        self.channel2.play(self.sound2)
                        #self.display3()
                elif key == 's':  # move down
                    if self.board.isBlockValid(self.board.cur_block.x + 1, self.board.cur_block.y):
                        self.board.cur_block.moveDown()
                        self.num_moves += 1
                        self.channel2.play(self.sound2)
                        #self.display3()
                    else:
                        self.board.dump()
                        self.board.cur_block.x = 0
                        self.board.cur_block.y = 0
                        self.board.putNewBlock3()
                        #self.display3()
                        if not self.board.isBlockValid(self.board.cur_block.x, self.board.cur_block.y):
                            break
                elif key == 'w':  # rotate the block counterclockwise
                    if self.board.isBlockValid(self.board.cur_block.x + 1, self.board.cur_block.y):
                        self.board.cur_block.rotateLeft()
                        self.num_moves += 1
                        #self.display3()
                        self.channel2.play(self.sound2)
                elif key == 'q':  # quit the game
                    self.Game_now = False
                    print("bye")
                    break

                elif key == 'p': #pause the game
                    self.paused = True
                    print("game paused. Press 'i' to continue the game")

                if self.paused:
                    if key == 'i':
                        self.paused = False
                        print("game continued")
        # check if it's time to move the block down
        #pause if user input p -> self.paused = True
            if not self. paused and self.board.isBlockValid(self.board.cur_block.x + 1, self.board.cur_block.y):
                time.sleep(self.num)
                self.board.cur_block.moveDown()


            elif not self.paused and not self.board.isBlockValid(self.board.cur_block.x+1, self.board.cur_block.y):
                time.sleep(self.num)
                self.board.dump()
                self.board.cur_block.x = 0
                self.board.cur_block.y = 0
                if self.board.isBlockValid(self.board.cur_block.x, self.board.cur_block.y):

                    self.board.putNewBlock3()

                elif not self.board.isBlockValid(self.board.cur_block.x, self.board.cur_block.y):
                        break




            if self.board.remove_full_rows() != 0 and self.board.remove_full_rows() != None:
                self.board.remove_full_rows()
                self.channel3.play(self.sound3)

        print("Game over")
        cleared = self.board.score - 15
        print('cleared: ', cleared)

        self.channel1.stop()

        self.channel4.play(self.sound4)
        end = time.time()
        duration = int(end - start)
        
        print('time: ', duration, '(seconds)')
        print("total: time * (1+cleared) = ", duration *(cleared+1))
        
        #for the modes
        if self.mode == 1:
            print("time limited ver: ", self.duration, "second(s)")
        elif self.mode == 2:
            print("move limited ver: ", self.move_limitation, "move(s)")
        elif self.mode == 3:
            print("mode: endless")

        #print(self.move_limitation, self.num_moves)

        a = input('enter and send anything to end the game')




    # print board on the command line
    def display3(self) -> None:
            if not self.paused: # if not pause: continue show the board
                view = self.board.getView()
                for i in range(15):
                    for j in range(20):
                        if view[i][j] == 1:
                            print("X", end="")
                        else:
                            print(" ", end="")
                    print()
                print("""Press 'a' to move left, 'd' to move right, 's' to move down, 'w' to turn around, 'q' to quit.
                  p to pause""")
                return True
            #pause: not to display
            return False
