
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

efectiveness = [
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
                att = self.board[x][y]
                count = 0
                for i in range(-1,2):
                    for j in range(-1,2):
                        if (i == 0 and j == 0) or (x+i < 0 or x+i >= self.width or y+j < 0 or y+j >= self.height):
                            continue
                        defn = self.board[x+i][y+j]
                        if effectiveness[att][defn] == 2:
                            new_board.board[x+i][y+j] = att
                            self.histogram[att] += 1
                            self.histogram[defn] -= 1
                        #elif effectiveness[att][defn] == 1 and random.random() <= 0.5:
                        #    new_board.board[x+i][y+j] = att
        self.board = new_board.board
        
    def play(self, n):
        # Create subplots
        figure, ax = plt.subplots(1,2)
        mat = ax[0].matshow(self.board, cmap=c)
        bar = ax[1].bar(len(types), self.histogram, 0.5)
        ax[1].set_xticks(np.arange(len(types)), types)
        #ax[1].legend()
        #print(self.histogram)
        #rects2 = ax.bar(x + width/2, women_means, width, label='Women')

        # Add some text for labels, title and custom x-axis tick labels, etc.
        #ax.set_ylabel('Scores')
        #ax.set_title('Scores by group and gender')
        #ax.set_xticks(x, labels)
        #ax.legend()
        #bar.xticks(range(len(types)), types)

        #objects = ('Python', 'C++', 'Java', 'Perl', 'Scala', 'Lisp')
        #y_pos = np.arange(len(objects))
        #performance = [10,8,6,4,2,1]

        #plt.bar(y_pos, performance, align='center', alpha=0.5)
        #plt.xticks(y_pos, objects)
        #plt.ylabel('Usage')
        #plt.title('Programming language usage')

        
        # GUI
        plt.ion()
        plt.axis('off')

        for i in range(n):
            self.get_next_state()
            mat.set_data(self.board)
            #bar.(self.histogram)
            figure.canvas.draw()
            figure.canvas.flush_events()            
            plt.pause(0.1)
        plt.show()

    def drawBoard(self):
        plt.matshow(self.board,cmap=c,norm=n)
        plt.axis('off')
        plt.show()

if __name__ == '__main__':
    
    width = int(input("Width: "))
    height = int(input("Height: "))
    board = Board(width, height)
    board.play(300)

