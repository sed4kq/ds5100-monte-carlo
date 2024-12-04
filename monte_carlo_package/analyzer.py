import numpy as np
import pandas as pd

class Analyzer:
    
    """
    This class will take the results of a single game and analyze the some statistical properties of the results.
    """
    
    def __init__(self, game):
        """
        This initializes the analyzer by taking a game object.
        
        Arguments:
            game: a Game object
        
        Errors to Raise:
            ValueError: if the input is not a Game object
        """
        
        if not isinstance(game, Game):
            raise ValueError("`game` must be a Game object")
        
        self.game_results = game.show('wide').copy()
        
    
    
    def jackpot(self):
        """
        This computes how many times the game ended in a jackpot which is where all dice in a roll show the same face.
        
        Returns:
            The number of jackpots as an integer
        """
        
        jackpots = (self.game_results.nunique(axis=1) == 1).sum()
        return jackpots
    
    
    
    def roll_face_counts(self):
        """
        This computes the number of times a given face value is rolled for each event.
        
        Returns:
            A dataframe with the roll numbers in the index, face counts in the columns, and the count values in the cells
        """
        
        face_counts = self.game_results.apply(pd.Series.value_counts, axis=1).fillna(0).astype(int)
        return face_counts
    
    
    
    def combo_count(self):
        """
        This computes the number of distinct face combinations over all rolls. Note: Combinations are order-independent.
        
        Returns:
            A dataframe with the combinations as a MultiIndex and their counts in a column
        """
        
        combos = self.game_results.apply(lambda x: tuple(sorted(x)), axis=1)
        combo_counts = combos.value_counts()
        return pd.DataFrame({'count': combo_counts}).set_index(combo_counts.index)
    
    
    
    
    def permutation_count(self):
        """
        This computes the number of distinct face permutations over all rolls. Note: Permutations are order-dependent.
        
        Returns:
            A dataframe with the permutations as a MultiIndex and their counts in a column
        """
        
        perms = self.game_results.apply(lambda x: tuple(x), axis=1)
        perm_counts = perms.value_counts()
        return pd.DataFrame({'count': perm_counts}).set_index(perm_counts.index)