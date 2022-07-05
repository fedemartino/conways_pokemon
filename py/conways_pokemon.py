
from bdb import effective
import random
import time
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

types_gen1 = ['NOR','FIR','WAT','ELE','GRA','ICE','FIG','POI','GRO','FLY','PSY','BUG','ROC','GHO','DRA']
types_colors1 = [
    (170, 170, 153),
    (235, 73, 40),
    (87, 154, 253),
    (255, 237, 63),
    (137, 203, 89),
    (130, 204, 254),
    (174, 87, 69),
    (160, 88, 152),
    (214, 187, 89),
    (142, 154, 253),
    (236, 90, 153),
    (172, 186, 44),
    (183, 170, 104),
    (104, 103, 186),
    (120, 105, 236)
]

types_gen2 = ['NOR','FIR','WAT','ELE','GRA','ICE','FIG','POI','GRO','FLY','PSY','BUG','ROC','GHO','DRA','DAR','STE']
types_colors2 = [
    (170, 170, 153),
    (235, 73, 40),
    (87, 154, 253),
    (255, 237, 63),
    (137, 203, 89),
    (130, 204, 254),
    (174, 87, 69),
    (160, 88, 152),
    (214, 187, 89),
    (142, 154, 253),
    (236, 90, 153),
    (172, 186, 44),
    (183, 170, 104),
    (104, 103, 186),
    (120, 105, 236),
    (140, 111, 97),
    (183, 183, 197)
]

efectiveness_gen1 = [
    [1,1,1,1,1,1,1,1,1,1,1,1,0.5,0,1],
    [1,0.5,0.5,1,2,2,1,1,1,1,1,2,0.5,1,0.5],
    [1,2,0.5,1,0.5,1,1,1,2,1,1,1,2,1,0.5],
    [1,1,2,0.5,0.5,1,1,1,0,2,1,1,1,1,0.5],
    [1,0.5,2,1,0.5,1,1,0.5,2,0.5,1,0.5,2,1,0.5],
    [1,1,0.5,1,2,0.5,1,1,2,2,1,1,1,1,2],
    [2,1,1,1,1,2,1,0.5,1,0.5,0.5,0.5,2,0,1],
    [1,1,1,1,2,1,1,0.5,0.5,1,1,2,0.5,0.5,1],
    [1,2,1,2,0.5,1,1,2,1,0,1,0.5,2,1,1],
    [1,1,1,0.5,2,1,2,1,1,1,1,2,0.5,1,1],
    [1,1,1,1,1,1,2,2,1,1,0.5,1,1,1,1],
    [1,0.5,1,1,2,1,0.5,2,1,0.5,2,1,1,0.5,1],
    [1,2,1,1,1,2,0.5,1,0.5,2,1,2,1,1,1],
    [0,1,1,1,1,1,1,1,1,1,0,1,1,2,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,2]
]

efectiveness_gen2 = [
    [1,1,1,1,1,1,1,1,1,1,1,1,0.5,0,1,1,0.5],
    [1,0.5,0.5,1,2,2,1,1,1,1,1,2,0.5,1,0.5,1,2],
    [1,2,0.5,1,0.5,1,1,1,2,1,1,1,2,1,0.5,1,1],
    [1,1,2,0.5,0.5,1,1,1,0,2,1,1,1,1,0.5,1,1],
    [1,0.5,2,1,0.5,1,1,0.5,2,0.5,1,0.5,2,1,0.5,1,0.5],
    [1,0.5,0.5,1,2,0.5,1,1,2,2,1,1,1,1,2,1,0.5],
    [2,1,1,1,1,2,1,0.5,1,0.5,0.5,0.5,2,0,1,2,2],
    [1,1,1,1,2,1,1,0.5,0.5,1,1,1,0.5,0.5,1,1,0],
    [1,2,1,2,0.5,1,1,2,1,0,1,0.5,2,1,1,1,2],
    [1,1,1,0.5,2,1,2,1,1,1,1,2,0.5,1,1,1,0.5],
    [1,1,1,1,1,1,2,2,1,1,0.5,1,1,1,1,0,0.5],
    [1,0.5,1,1,2,1,0.5,0.5,1,0.5,2,1,1,0.5,1,2,0.5],
    [1,2,1,1,1,2,0.5,1,0.5,2,1,2,1,1,1,1,0.5],
    [0,1,1,1,1,1,1,1,1,1,2,1,1,2,1,0.5,0.5],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,0.5],
    [1,1,1,1,1,1,0.5,1,1,1,2,1,1,2,1,0.5,0.5],
    [1,0.5,0.5,0.5,1,2,1,1,1,1,1,1,2,1,1,1,0.5]
]

effectiveness = efectiveness_gen2
types = types_gen2
type_colors = types_colors2

normalized_colors = [[x /255 for x in color] for color in type_colors]
c = mpl.colors.ListedColormap(normalized_colors)
n = mpl.colors.Normalize(vmin=0,vmax=len(types))

class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = []
        self.histogram = [0 for _ in range(len(types))]
        for i in range(height):
            self.board.append([])
            for j in range(width):
                type_ = random.randint(0,len(types)-1)
                self.histogram[type_] = self.histogram[type_] + 1
                self.board[i].append(type_)

    def clone(self):
        new_board = Board(self.width, self.height)
        for i in range(self.width):
            for j in range(self.height):
                new_board.board[i][j] = self.board[i][j]
        return new_board

    def print(self):
        for i in range(self.height):
            for j in range(self.width):
                print(types_gen2[self.board[i][j]], end=', ')
            print()
    
    def get_next_state(self):
        new_board = self.clone()
        for x in range(self.width):
            for y in range(self.height):
                defn = self.board[x][y]
                looseCount = 0
                winners = []
                for i in range(-1,2):
                    for j in range(-1,2):
                        if (i == 0 and j == 0) or (x+i < 0 or x+i >= self.width or y+j < 0 or y+j >= self.height):
                            continue
                        att = self.board[x+i][y+j]
                        if effectiveness[att][defn] == 2:
                        # or (effectiveness[att][defn] == 1 and random.random() <= 0.0):
                            looseCount = looseCount + 1
                            winners.append(att)
                if (looseCount > 0):
                    winner = random.choice(winners)
                    new_board.board[x][y] = winner
                    self.histogram[winner] += 1
                    self.histogram[defn] -= 1
        self.board = new_board.board
        
    def play(self, n):
        # Create subplots
        figure, ax = plt.subplots(1,2)
        mat = ax[0].matshow(self.board, cmap=c)
        bar = ax[1].bar(types, self.histogram)
        [bar[i].set_color(normalized_colors[i]) for i in range(len(normalized_colors))]
        ax[1].set_xticks(np.arange(len(types)), types)
                
        # GUI
        plt.ion()
        #plt.axis('off')

        for i in range(n):
            self.get_next_state()
            mat.set_data(self.board)

            bar.remove()
            bar = ax[1].bar(types, self.histogram)
            [bar[i].set_color(normalized_colors[i]) for i in range(len(normalized_colors))]
            
            figure.canvas.draw()
            figure.canvas.flush_events()            
            plt.pause(0.05)
        plt.show()

    def drawBoard(self):
        plt.matshow(self.board,cmap=c,norm=n)
        plt.axis('off')
        plt.show()

if __name__ == '__main__':
    
    width = int(input("Width & Height (square board): "))
    height = width
    n = int(input("Number of iterations: "))
    board = Board(width, height)
    board.play(n)

