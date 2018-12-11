import unittest

from CodeWarriors.digitalRoot import digital_root
from CodeWarriors.RectToSquare import sqInRect

class tester(unittest.TestCase):

    def test_digitalroot(self):
        self.assertEqual(digital_root(16), 7)
        self.assertEqual(digital_root(456), 6)
        self.assertEqual(sqInRect(14, 20), [14,6,6,2,2,2])

if __name__ == '__main__':
    unittest.main()

