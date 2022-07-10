from gens import gen1, gen2 
from board import *
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np


def play(gen, iterations = 2000, size = 150):
    
    b = Board(size, size, gen)

    types = gen.get_types()
    type_colors = gen.get_colors()
    
    normalized_colors = [[x /255 for x in color] for color in type_colors]
    c = mpl.colors.ListedColormap(normalized_colors)
    n = mpl.colors.Normalize(vmin=0,vmax=len(types))

    # Create subplots
    figure, ax = plt.subplots(1,2)
    mat = ax[0].matshow(b.board, cmap=c)
    bar = ax[1].bar(types, b.histogram)
    [bar[i].set_color(normalized_colors[i]) for i in range(len(normalized_colors))]
    ax[1].set_xticks(np.arange(len(types)), types)
            
    # GUI
    plt.ion()
    #plt.axis('off')

    for i in range(iterations):
        b.get_next_state()
        mat.set_data(b.board)

        bar.remove()
        bar = ax[1].bar(types, b.histogram)
        [bar[i].set_color(normalized_colors[i]) for i in range(len(normalized_colors))]
        
        figure.canvas.draw()
        figure.canvas.flush_events()            
        plt.pause(0.05)
    plt.show()


if __name__ == '__main__':
    gen = gen2.GenData()
    size = int(input("Width & Height (square board): "))
    n = int(input("Number of iterations: "))
    play(gen, n, size)

