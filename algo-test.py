import unittest
from algo import *

class TestAbsFunction(unittest.TestCase):
    def test_positive_number(self):
        self.assertEqual(abs(10), 10)

    def test_negative_number(self):
        self.assertEqual(abs(-10), 10)

    def test_zero(self):
        self.assertEqual(abs(0), 0)
    def test_afficher_grille(self):
        grid= [ ["S","O","O"],
        [ "O","O","O"],
        [ "O","O","E"],
        ]
        self.assertEqual(affichgrille(grid),'''['S', 'O', 'O']
['O', 'O', 'O']
['O', 'O', 'E']
''')


if __name__ == "__main__":
    unittest.main()