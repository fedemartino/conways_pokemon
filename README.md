# conways_pokemon
This is a celular automation inspired in pokemon effectiveness rules. 

The rules are simple:
 * Each cell has a type assigned
 * Every cell battles all four adjacent cells (vertical and horizontal, not diagonal)
    * If any of the adjacent cells are supereffective against the current cell, then the current cell changes type to the same of the winner.
    * If more than one adjacent cell is supereffective, then a winner is chosen at random from one of the potential winners.
    * If none of the adjacent cells are supereffective, the current cell retains its type. 

## Implementation
This is just something I did for fun over a weekend. I tried implementing in two very different languages (python and C#) to see how different it would be.

### Python 
Python implmentation is very simple and uses MatPlotLib as the main way to visualize data.