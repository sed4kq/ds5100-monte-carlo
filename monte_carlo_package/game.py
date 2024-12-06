from .die import Die
import pandas as pd
import numpy as np


class Game:
    
    """
    This class will simulate the rolling of one or more dice within a game. It can roll a specified number of times and outputs the results in a specified format.
    """
    
    def __init__(self, dice):
        """
        This initializes the game by taking a list of Die objects with the same number of faces, but potentially different weights.
        
        Arguments:
            dice: a list of similar Die objects
        """
        
        self.dice = dice
        self.results = None
    
    
    
    def play(self, num_rolls):
        """
        This rolls all the dice the given number of times.
        
        Arguments:
            num_rolls: the number of rolls for the dice   (integer)
        """
        
        rolls = {i: die.roll(num_rolls) for i, die in enumerate(self.dice)}
        self.results = pd.DataFrame(rolls)
    
    
    
    def show(self, form = 'wide'):
        """
        This returns the results of the most recent play of the game in the desired format.
        
        Arguments:
            shape: the format of the data (wide or narrow), the default for this is wide   (string)
            
        Errors to Raise:
            ValueError: if the reuqested `form` is not wide or narrow
        """
        
        if form.lower() == 'wide':
            return self.results.copy()
        elif form.lower() == 'narrow':
            return self.results.stack().reset_index(name='outcome')
        else:
            raise ValueError("Invalid format. Must be `wide` or `narrow`")
