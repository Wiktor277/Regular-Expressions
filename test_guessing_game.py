import unittest


import guessing_game

class TestGame(unittest.TestCase):
    def test_input(self):
        result = guessing_game.run_guessing_game(5, 5)
        self.assertTrue(result)

class TestGame2(unittest.TestCase):
    def test_input_incorrect(self):
        result = guessing_game.run_guessing_game(7, 5)
        self.assertFalse(result)

class TestGame3(unittest.TestCase):
    def test_input_outofrange(self):
        result = guessing_game.run_guessing_game(15, 5)
        self.assertFalse(result)

class TestGame4(unittest.TestCase):
    def test_input_wrong_type(self):
        result = guessing_game.run_guessing_game('15', 5)
        self.assertFalse(result)



if __name__ == "__main__":
    unittest.main()
