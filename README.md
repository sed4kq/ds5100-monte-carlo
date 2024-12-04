# Monte Carlo Simulator Project

# Metadata

Project Name: monte_carlo_package

Author: S. Delaney

License: MIT

Version: 1.0

Description: Monte Carlo simulator package for dice-based games.



# Synopsis

```python
### Die
from monte_carlo_package.die import Die
import numpy as np

die = Die(np.array([1, 2, 3, 4, 5, 6]))
die.roll(5)
die.weight(6, 2)
die.current_state()


### Game
from monte_carlo_package.game import Game

game = Game([die, die])
game.play(5)
game.show('wide')


### Analyzer
from monte_carlo_package.analyzer import Analyzer

analyzer = Analyzer(game)
analyzer.jackpot()
analyzer.roll_face_counts()
analyzer.combo_count()
analyzer.permutation_count()
```


# API

## Die
__init__(faces)
  - Initializes a Die with faces
  
weight(face_value, new_weight)
  - Sets the weight for a face value
  
roll(num_rolls=1)
  - Rolls the die a given number of times
  
current_state()
  - Returns the current state of the die

## Game
__init__(dice)
  - Initializes a Game with Die objects.
  
play(num_rolls)
  - Rolls all dice a given number of times
  
show(form='wide')
  - Displays the results as either a 'wide' or 'narrow' format.

## Analyzer
__init__(game)
  - Initializes an Analyzer with a Game object
  
jackpot()
  - Outputs the number of rolls where all dice show the same face
  
roll_face_counts()
  - Outputs a DataFrame containing the number of times each face value was rolled
  
combo_count()
  - Outputs a DataFrame containing the number of distinct face combinations
  
permutation_count()
  - Outputs a DataFrame containing the number of distinct face permutations


