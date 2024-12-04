"""
The Die Class

This class represents a die with faces and custom weights (defaults to 1). It rolls the die and gets the current state of the die.
"""


import numpy as np
import pandas as pd


class Die:
    
    """
    This class represents a die that can be rolled one or more times.

    Attributes:
        die: A private pandas DataFrame containing all faces (as the index) and their respective weights.
    """

    def __init__(self, faces):
        """
        This initializes a Die object that contains user provided faces and default weights of one.
        
        Arguments:
            faces: a numpy array of unique values representing the faces of the die   (strings or integers)

        Errors to Raise:
            TypeError: if faces is not a numpy array
            ValueError: if faces contains any duplicate values
        """
        
        if not isinstance(faces, np.ndarray):
            raise TypeError("`faces` must be stored as a numpy array.")
        if len(faces) != len(np.unique(faces)):
            raise ValueError("`faces` must be different.")

        self.die = pd.DataFrame({'face': faces, 'weight': np.ones(len(faces))})
        self.die.set_index('face', inplace=True)

        
               
    def weight(self, face_value, new_weight):
        """
        This can change the weight of a specific face.

        Arguments:
            face_value: the face whose weight is being changed   (string or integer)
            new_weight: the new weight value for the given face  (integer or float)

        Errors to Raise:
            IndexError: if the face_value is not found in the dataframe
            TypeError: if the new_weight is not in numeric form
        """
        
        if face_value not in self.die.index:
            raise IndexError("`face_value` is not found in self.die ")
        try:
            new_weight = float(new_weight)
        except ValueError:
            raise TypeError("`new_weight` must be a numeric value")
        
        self.die.loc[face_value, 'weight'] = new_weight
    
    
    
    def roll(self, num_rolls = 1):
        """
        This rolls the die one or more times.
        
        Arguments:
            num_rolls: the number of times to roll the die - the default is 1  (integer)
        
        Returns:
            A list of all outcomes from the roll
        """
        
        dice_rolls = list(self.die.sample(n = num_rolls, weights = 'weight', replace = True).index)
        return dice_rolls
    
    
    
    def current_state(self):
        """
        This will return the current state of the die.
        
        Returns:
            A copy of the private DataFrame of all faces and weights
        """
        
        return self.die.copy()
