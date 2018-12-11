import unittest

from PrManOco.HW01 import HW01


class tester(unittest.TestCase):

    def test_digitalroot(self):
        self.assertEqual(HW01.idOf([1, 2, 3, 4, 5, 6], 5), 4)
        self.assertEqual(HW01.mergeFun([1,3,9], [2,4,8]), [1, 2, 3, 4, 8, 9])
        self.assertEqual(HW01.mergeFun([12, 25, 40],[20, 37, 45]), [12, 20, 25, 37, 40, 45])
        self.assertEqual(HW01.mergeFun([10, 13, 24], [12, 35]), [10, 12, 13, 24, 35])
        # self.assertEqual(digital_root(16), 7)
        # self.assertEqual(digital_root(456), 6)
        # self.assertEqual(sqInRect(14, 20), [14,6,6,2,2,2])

if __name__ == '__main__':
    unittest.main()