import pygame
import sys
from pygame.locals import *
from constants import *
from objects import Board, Game

def main():
    #setup
    pygame.init()
    win = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Tic-Tac-Toe')
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(pygame.font.get_default_font(), 64)
    game = Game(win, font)
        
    #variables   
    run = True
    
    #main loop
    while run:
        for event in pygame.event.get():
            if event.type == QUIT:
                run = False
            elif event.type == MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                game.board.update(mouse_pos)
        
        keys = pygame.key.get_pressed()

        game.update(keys)
        game.draw()
        
        clock.tick(FPS)
        pygame.display.flip()

    #exit properly
    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()