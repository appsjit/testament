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



############ To test inside file
# s = Solution();
# matrix = [[36376,85652,21002,4510],[68246,64237,42962,9974],[32768,97721,47338,5841],[55103,18179,79062,46542]]
# ##matrix = [[3,7,8],[9,11,13],[15,16,17]]
# print(s.luckyNumbers(matrix))