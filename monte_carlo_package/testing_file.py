import unittest
import pandas as pd
import numpy as np
from .die import Die
from .game import Game
from .analyzer import Analyzer


class MonteCarloTest(unittest.TestCase):
    """
    This class will unit test all of the methods for the Monte Carlo game simulator from the die, game, and analyzer classes.
    """
    
    def test_init_die(self):
        """
        Testing the initializer in the die class to affirm faces is of the correct length as a numpy array.
        """
        faces = np.array([1, 2, 3, 4, 5, 6])
        die = Die(faces)
        self.assertEqual(len(die.current_state()), 6)

        
    def test_weight(self):
        """
        Testing the weight method in the die class to check if the weight of a specific die is successfully being changed.
        """
        faces = np.array([1, 2, 3, 4, 5, 6])
        die = Die(faces)
        die.weight(1, 2)
        self.assertEqual(die.current_state().loc[1, 'weight'], 2)

        
    def test_roll(self):
        """
        Testing the roll method in the die class to confirm it is rolling the correct number of times.
        """
        faces = np.array([1, 2, 3, 4, 5, 6])
        die = Die(faces)
        rolls = die.roll(5)
        self.assertEqual(len(rolls), 5)
    
    
    def test_current_state(self):
        """
        Testing the current state method in the die class to confirm the number of faces on the die.
        """
        die = Die(np.array([1, 2, 3, 4, 5, 6]))
        current = die.current_state()
        self.assertEqual(current.shape[0], 6)


        
        
        

    def test_init_game(self):
        """
        Testing the initializer method in the game class to confirm it is creating the right number of dice.
        """
        die_1 = Die(np.array([1, 2, 3, 4, 5, 6]))
        die_2 = Die(np.array([1, 2, 3, 4, 5, 6])) 
        game = Game([die_1, die_2]) 
        self.assertEqual(len(game.dice), 2)
        
        
    def test_play(self):
        """
        Testing the play method in the game class to confirm the play method is executing five times for one dice.
        """
        faces = np.array([1, 2, 3, 4, 5, 6])
        die = Die(faces)
        game = Game([die])
        game.play(5)
        outcome = game.show()
        self.assertEqual(outcome.shape, (5, 1))

        
    def test_show(self):
        """
        Testing the show method in the game class to check if the `wide` and `narrow` data structures are being stored correctly.
        The `wide` format being a row for each roll number and a column for each die number.
        The `narrow` format being a MultiIndex for the roll number and the die number.
        """
        faces = np.array([1, 2, 3, 4, 5, 6])
        die = Die(faces)
        game = Game([die])
        game.play(5)
        wide = game.show('wide')
        narrow = game.show('narrow')
        self.assertEqual(wide.shape, (5, 1))
        self.assertEqual(narrow.shape, (5, 3))

    
    
            
    
    def test_init_analyzer(self):
        """
        Testing the initializer method in the analyzer class to confirm it is created correctly.
        """
        die = Die(np.array([1, 2, 3, 4, 5, 6]))
        game = Game([die])
        game.play(5)
        analyzer = Analyzer(game)
        self.assertIsInstance(analyzer, Analyzer)

        
    def test_jackpot(self):
        """
        Testing the jackpot method in the analyzer class to check if the jackpots value is an integer.
        """
        faces = np.array([1, 2, 3, 4, 5, 6])
        die = Die(faces)
        game = Game([die])
        game.play(5)
        analyzer = Analyzer(game)
        self.assertIsInstance(analyzer.jackpot(), int)

        
    def test_roll_face_counts(self):
        """
        Testing the roll face count method in the analyzer class to check that this method returns a count for each roll.
        """
        faces = np.array([1, 2, 3, 4, 5, 6])
        die = Die(faces)
        game = Game([die])
        game.play(5)
        analyzer = Analyzer(game)
        face_counts = analyzer.roll_face_counts()
        self.assertEqual(face_counts.shape[0], 5)

        
    def test_combo_count(self):
        """
        Testing the combo count method in the analyzer class to check that this method is computing at least one different combination.
        """
        faces = np.array([1, 2, 3, 4, 5, 6])
        die = Die(faces)
        game = Game([die])
        game.play(5)
        analyzer = Analyzer(game)
        combos = analyzer.combo_count()
        self.assertGreaterEqual(len(combos), 1)

        
    def test_permutation_count(self):
        """
        Testing the permutation count method in the analyzer class to check that this method is computing at least one different permutation.
        """
        faces = np.array([1, 2, 3, 4, 5, 6])
        die = Die(faces)
        game = Game([die])
        game.play(5)
        analyzer = Analyzer(game)
        perms = analyzer.permutation_count()
        self.assertGreaterEqual(len(perms), 1)


        
        
if __name__ == '__main__':
    unittest.main()
    
    