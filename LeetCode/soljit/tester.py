import unittest

from soljit.s003_LongestSubstrWOR import Solution


class tester(unittest.TestCase):

    def test_digitalroot(self):
        ##self.assertEqual(Solution.lengthOfLongestSubstring('abcabcsab'), 4)
        self.assertEqual(Solution.lengthOfLongestSubstring('abccbcabcsab'), 4)
        # self.assertEqual(digital_root(16), 7)
        # self.assertEqual(digital_root(456), 6)
        # self.assertEqual(sqInRect(14, 20), [14,6,6,2,2,2])

if __name__ == '__main__':
    unittest.test_digitalroot()