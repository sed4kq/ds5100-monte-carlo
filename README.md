# Monte Carlo Simulator Project

## Metadata

Project Name: monte_carlo_package

Author: S. Delaney


## Synopsis

```python
### Die
import numpy as np
from monte_carlo_package.die import Die

faces = np.array([1, 2, 3, 4, 5, 6])
die = Die(faces)
die.weight(1, 2)
die.roll(5)
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



## API

### Die
__init__(faces)
 - This initializes a Die object that contains user provided faces and default weights of one.
        
 - Arguments: faces: a numpy array of unique values representing the faces of the die   (strings or integers)

 - Errors to Raise: TypeError: if faces is not a numpy array        ValueError: if faces contains any duplicate values
  
weight(face_value, new_weight)
 - This can change the weight of a specific face.

 - Arguments: face_value: the face whose weight is being changed   (string or integer)            new_weight: the new weight value for the given face  (integer or float)

 - Errors to Raise: IndexError: if the face_value is not found in the dataframe                   TypeError: if the new_weight is not in numeric form  

roll(num_rolls=1)
 - This rolls the die one or more times.
        
 - Arguments: num_rolls: the number of times to roll the die - the default is 1  (integer)
        
 - Returns: A list of all outcomes from the roll
            
current_state()
 - This will return the current state of the die as a DataFrame of all faces and weights.


### Game
__init__(dice)
 - This initializes the game by taking a list of Die objects with the same number of sides and faces, but potentially different weights.
        
 - Arguments: dice: a list of similar Die objects  

play(num_rolls)
 - This rolls all the dice the given number of times.
        
 - Arguments: num_rolls: the number of rolls for the dice   (integer)  

show(form='wide')
 - This returns the results of the most recent play of the game in the desired format.
        
 - Arguments: shape: the format of the data (wide or narrow), the default for this is wide   (string)
            
 - Errors to Raise: ValueError: if the reuqested `form` is not wide or narrow


### Analyzer
__init__(game)
 - This initializes the analyzer by taking a game object.
        
 - Arguments: game: a Game object
        
 - Errors to Raise: ValueError: if the input is not a Game object 
 
jackpot()
 - This computes how many times the game ended in a jackpot which is where all dice in a roll show the same face.
        
 - Returns: The number of jackpots as an integer  
 
roll_face_counts()
 - This computes the number of times a given face value is rolled for each event.
        
 - Returns: A dataframe with the roll numbers in the index, face counts in the columns, and the count values in the cells
  
combo_count()
 - This computes the number of distinct face combinations over all rolls. Note: Combinations are order-independent.

 - Returns: A dataframe with the combinations as a MultiIndex and their counts in a column
  
permutation_count()
 - This computes the number of distinct face permutations over all rolls. Note: Permutations are order-dependent.

 - Returns: A dataframe with the permutations as a MultiIndex and their counts in a column

