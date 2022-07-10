import random


class Board:
    def __init__(self, width, height, gen, tie_breaker=0):
        self.width = width
        self.height = height
        self.gen = gen
        self.board = []
        self.effectiveness = gen.get_effectiveness()
        self.types = gen.get_types()
        self.histogram = [0 for _ in range(len(gen.get_types()))]
        self.tie_breaker = tie_breaker

        for i in range(height):
            self.board.append([])
            for j in range(width):
                type_ = random.randint(0,len(gen.get_types())-1)
                self.histogram[type_] = self.histogram[type_] + 1
                self.board[i].append(type_)

    def clone(self):
        new_board = Board(self.width, self.height, self.gen)
        for i in range(self.width):
            for j in range(self.height):
                new_board.board[i][j] = self.board[i][j]
        return new_board

    def print(self):
        for i in range(self.height):
            for j in range(self.width):
                print(self.types[self.board[i][j]], end=', ')
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
                        if self.effectiveness[att][defn] == 2 or (self.effectiveness[att][defn] == 1 and random.random() <= self.tie_breaker):
                            looseCount = looseCount + 1
                            winners.append(att)
                if (looseCount > 0):
                    winner = random.choice(winners)
                    new_board.board[x][y] = winner
                    self.histogram[winner] += 1
                    self.histogram[defn] -= 1
        self.board = new_board.board