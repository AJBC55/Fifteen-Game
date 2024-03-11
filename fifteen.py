''' DO NOT FORGET TO ADD COMMENTS '''

import numpy as np
from random import choice


class Fifteen:
    
    def __init__(self, size = 4):
        self.size = size
        self.tiles = np.array([i for i in range(1,size**2)] + [0])
        self.adj = self.create_adj()
                
        
        
            
    def create_adj(self):
        adj = []
        for row in range(self.size):
            for col in range(self.size):
                connects = []
                # Convert row and column to linear index
                index = row * self.size + col
                # Check possible moves (up, down, left, right) and add them if within bounds
                if row > 0: connects.append(index - self.size)  # Move up in a 1D array
                if row < self.size - 1: connects.append(index + self.size)  # Move down in a 1D array
                if col > 0: connects.append(index - 1)  # Move left in a 1D array
                if col < self.size - 1: connects.append(index + 1)  # Move right in a 1D array
                adj.append(connects)
        return adj
           
    def find_index(self, move):
        for idx, val in np.ndenumerate(self.tiles):
            if val == move:
                return idx[0]
    
    
    def update(self, move):
        index = self.find_index(move)
        zero_index = self.find_index(0)
        if self.is_valid_move(move) :
            self.tiles[zero_index], self.tiles[index] = self.tiles[index], self.tiles[zero_index]
       
      
        
    def transpose(self, i, j):
        pass 
        

    def shuffle(self, steps=100):
        for _ in range(steps):
            index = np.where(self.tiles == 0)[0][0]
            move_index = choice(self.adj[index])
            self.tiles[index], self.tiles[move_index] = self.tiles[move_index], self.tiles[index]
    
        
        
        
        
    def is_valid_move(self, move):
        index = self.find_index(move)
        zero_index = self.find_index(0)
        return index in self.adj[zero_index]
            

    def is_solved(self):
        solved_state = np.arange(1, self.size**2 + 1)
        solved_state[-1] = 0  
            
            
        return np.array_equal(self.tiles, solved_state)

    def draw(self):
        print('+---' * self.size + '+')
        for i in range(self.size):
            for j in range(self.size):
                tile = ' ' if self.tiles[i*self.size + j] == 0 else self.tiles[i*self.size + j]
                print(f'|{tile:3}', end='')
            print('|')
            print('+---' * self.size + '+')

        
        
    def __str__(self):
        
        formatted_tiles = self.tiles.astype(str)
        formatted_tiles[formatted_tiles == '0'] = ' '  
        formatted_tiles = np.array([f"{tile: >2}" for tile in formatted_tiles])

        # string representation
        puzzle_str = ""
        for i in range(self.size):
            row_str = ' '.join(formatted_tiles[i*self.size:(i+1)*self.size])
            puzzle_str += row_str + " \n" if i < self.size - 1 else row_str + " \n"

        return puzzle_str
    

if __name__ == '__main__':
    
    game = Fifteen()
    assert str(game) == ' 1  2  3  4 \n 5  6  7  8 \n 9 10 11 12 \n13 14 15    \n'
    assert game.is_valid_move(15) == True
    assert game.is_valid_move(12) == True
    assert game.is_valid_move(14) == False
    assert game.is_valid_move(1) == False
    game.update(15)
    
    assert str(game) == ' 1  2  3  4 \n 5  6  7  8 \n 9 10 11 12 \n13 14    15 \n'
    game.update(15)
   
    assert str(game) == ' 1  2  3  4 \n 5  6  7  8 \n 9 10 11 12 \n13 14 15    \n'
    assert game.is_solved() == True
    game.shuffle()
    assert str(game) != ' 1  2  3  4 \n 5  6  7  8 \n 9 10 11 12 \n13 14 15    \n'
    assert game.is_solved() == False
    
    
    '''You should be able to play the game if you uncomment the code below'''
    
    game = Fifteen()
    game.shuffle()
    game.draw()
    
    while True:
        move = input('Enter your move or q to quit: ')
        if move == 'q':
            break
        elif not move.isdigit():
            continue
        game.update(int(move))
        game.draw()
        if game.is_solved():
            break
    print('Game over!')

    
    
        
