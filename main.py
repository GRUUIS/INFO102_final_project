from Game import Game
#import pygame
import time

def main()->None:
    # initialize and run the Tetris game
    
    # pygame.mixer.init()
    # pygame.mixer.music.load("toby fox - UNDERTALE Soundtrack - 03 Your Best Friend.mp3")
    # pygame.mixer.music.play(-1)

    game = Game()
    game.run()
    
    return 

if __name__ == "__main__":
    main()

