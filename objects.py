import pygame
from pygame.locals import *
from constants import *
from random import choice


class Game:
    def __init__(self, win, font):
        self.win = win
        self.font = font
        self.score_x = 0
        self.score_y = 0
        self.board = Board(win)
        
    def update(self, keys):
        if keys[K_r]:
            self.board.clear()
        
        winner = self.board.check_win()
        if winner:
            self.new_round(winner)

    def draw(self):
        self.board.draw_board()    
        self.board.draw_pieces() 
    
    def new_round(self, winner):
        self.draw()
        self.display_message(f'{winner.upper()} won!', (WIDTH//2, HEIGHT//2))
        pygame.display.flip()
        pygame.time.delay(2000)
        self.board.clear()
        self.board.change_player()
        if winner == 'x':
            self.score_x += 1
        else:
            self.score_y += 1
    
    def display_message(self, text, pos):
        text = self.font.render(text, True, BLACK, WHITE)
        textRect = text.get_rect()
        textRect.center = pos
        self.win.blit(text, textRect)

class Board:
    
    def __init__(self, win):
        self.win = win
        self.board = [[0, 0, 0],
                      [0, 0, 0],
                      [0, 0, 0 ]]
        
        self.piece_padding = 20
        self.won = False
        self.turn = choice(['x', 'o'])
        
        self.x_img = pygame.image.load('assets/X.png').convert_alpha()
        self.o_img = pygame.image.load('assets/O.png').convert_alpha()
        
        self.x_img = pygame.transform.scale( self.x_img, (SQUARE_SIZE - self.piece_padding, SQUARE_SIZE - self.piece_padding))
        self.o_img = pygame.transform.scale( self.o_img, (SQUARE_SIZE - self.piece_padding, SQUARE_SIZE - self.piece_padding))
        
    def draw_board(self):
        self.win.fill(TURQUOISE)
        for i in range(1, 3):
            pygame.draw.line(self.win, BLACK, (i*SQUARE_SIZE, 0), (i*SQUARE_SIZE, HEIGHT), width=3)
        for i in range(1, 3):
            pygame.draw.line(self.win, BLACK, (0, i*SQUARE_SIZE), (WIDTH, i*SQUARE_SIZE), width=3)
    
    def draw_pieces(self):
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                if piece == 'x':
                    self.win.blit(self.x_img, (col*SQUARE_SIZE + self.piece_padding//2, row*SQUARE_SIZE + self.piece_padding//2))
                elif piece == 'o':
                    self.win.blit(self.o_img, (col*SQUARE_SIZE + self.piece_padding//2, row*SQUARE_SIZE + self.piece_padding//2))

    def get_row_col_from_mouse_pos(self, mouse_pos):
        x, y = mouse_pos
        row = y//SQUARE_SIZE
        col = x//SQUARE_SIZE

        return (row, col)
    
    def update(self, mouse_pos):
        row, col = self.get_row_col_from_mouse_pos(mouse_pos)
        if self.board[row][col] == 0:
            self.board[row][col] = self.turn

            check_win = self.check_win()
            if check_win:
                # TODO draw line over winning pieces and write message + reset after 5 seconds.
                pass
            
            self.change_player()  
    
    def clear(self):
        self.board = [[0, 0, 0],
                [0, 0, 0],
                [0, 0, 0 ]]
    
    def change_player(self):
        if self.turn == 'x':
            self.turn = 'o'
        else:
            self.turn = 'x'


    def check_win(self):
        # Check rows and columns
        for i in range(3):
            if all(cell == self.board[i][0] and cell != '' for cell in self.board[i]):
                return self.board[i][0]

            if all(cell == self.board[0][i] and cell != '' for cell in (self.board[j][i] for j in range(3))):
                return self.board[0][i]

        # Check diagonals
        if all(cell == self.board[0][0] and cell != '' for cell in (self.board[i][i] for i in range(3))):
            return self.board[0][0]

        if all(cell == self.board[0][2] and cell != '' for cell in (self.board[i][2 - i] for i in range(3))):
            return self.board[0][2]

        return None  # No winner
    
    def draw_win_line(self):
        pass
        
        
        
    
