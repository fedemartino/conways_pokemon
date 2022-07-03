
import random
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

types = ['NOR','FIR','WAT','ELE','GRA','ICE','FIG','POI','GRO','FLY','PSY','BUG','ROC','GHO','DRA']
types_colors = [
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
normalized_colors = [[x /255 for x in color] for color in types_colors]
c = mpl.colors.ListedColormap(normalized_colors)
n = mpl.colors.Normalize(vmin=0,vmax=14)

efectiveness = [
    [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0.5,0,-1],
    [-1,0.5,0.5,-1,2,2,-1,-1,-1,-1,-1,2,0.5,-1,0.5],
    [-1,2,0.5,-1,0.5,-1,-1,-1,2,-1,-1,-1,2,-1,0.5],
    [-1,-1,2,0.5,0.5,-1,-1,-1,0,2,-1,-1,-1,-1,0.5],
    [-1,0.5,2,-1,0.5,-1,-1,0.5,2,0.5,-1,0.5,2,-1,0.5],
    [-1,-1,0.5,-1,2,0.5,-1,-1,2,2,-1,-1,-1,-1,2],
    [2,-1,-1,-1,-1,2,-1,0.5,-1,0.5,0.5,0.5,2,0,-1],
    [-1,-1,-1,-1,2,-1,-1,0.5,0.5,-1,-1,2,0.5,0.5,-1],
    [-1,2,-1,2,0.5,-1,-1,2,-1,0,-1,0.5,2,-1,-1],
    [-1,-1,-1,0.5,2,-1,2,-1,-1,-1,-1,2,0.5,-1,-1],
    [-1,-1,-1,-1,-1,-1,2,2,-1,-1,0.5,-1,-1,-1,-1],
    [-1,0.5,-1,-1,2,-1,0.5,2,-1,0.5,2,-1,-1,0.5,-1],
    [-1,2,-1,-1,-1,2,0.5,-1,0.5,2,-1,2,-1,-1,-1],
    [0,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,-1,-1,2,-1],
    [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,2]
]

class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = []
        for i in range(height):
            self.board.append([])
            for j in range(width):
                self.board[i].append(random.randint(0,len(types)-1))

    def clone(self):
        new_board = Board(self.width, self.height)
        for i in range(self.width):
            for j in range(self.height):
                new_board.board[i][j] = self.board[i][j]
        return new_board

    def print(self):
        for i in range(self.height):
            for j in range(self.width):
                print(types[self.board[i][j]], end=', ')
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
                        if efectiveness[att][defn] == 2:
                            new_board.board[x+i][y+j] = att
                            #print(types[att] + ' beats ' + types[defn])
        self.board = new_board.board
        #print()
        #new_board.print()
        #print()
    
    def drawBoard(self):
        plt.matshow(self.board,cmap=c,norm=n)
        plt.axis('off')
        plt.show()
        #plt.figure(figsize=(10,10))
        #plt.matshow(self.board, cmap=c, norm=n)
        #plt.axis('off')
        #plt.show()

if __name__ == '__main__':
    print(len(types))
    width = int(input("Width: "))
    height = int(input("Height: "))
    board = Board(width, height)
    #board.print()
    board.drawBoard()
    #print()
    board.get_next_state()
    #board.print()
    board.drawBoard()
    
    #att = int(input("Attacker: "))
    #print("Attacker: ", types[att])

    #defn = int(input("Defender: "))
    #print("Defender: ", types[defn])

    #result = efectiveness[att][defn]
    #if (result == -1):
    #    print("Attacker and Defender are neutral")
    #elif (result == 0):
    #    print("Attacker has no effect on Defender")
    #elif (result == 0.5):
    #    print("Attacker is Not very effective against Defender")
    #elif (result == 2):
    #    print("Attacker is super effective against Defender")

