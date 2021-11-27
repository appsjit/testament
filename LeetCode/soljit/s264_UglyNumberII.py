class Solution:
    def nthUglyNumber(self, n: int) -> int:
        # 0   0   0   1
        # 0   0   0   2
        # 1   0   0   3
        # 1   1   0   4
        # 2   1   0   5
        # 2   1   1   6
        # 3   2   1   8
        # 4   2   1   9
        # 4   3   1   10
        # 5   3   2   12
        # 6   4   2   15
        # https://leetcode.com/problems/ugly-number-ii/discuss/718879/Python-O(n)-universal-dp-solution-explained

        ans = [0] * n
        ans[0] = 1
        f2, f3, f5 = 0, 0, 0
        for x in range(1, n):
            ans[x] = min(ans[f2] * 2, ans[f3] * 3, ans[f5] * 5)
            print('f2:' + str(f2) + '  f3:' + str(f3) + '  f5:' + str(f5) + '   ans:' + str(x) + '   ' + str(ans[x]))
            if ans[x] == ans[f2] * 2:
                f2 += 1
            if ans[x] == ans[f3] * 3:
                f3 += 1
            if ans[x] == ans[f5] * 5:
                f5 += 1

        return ans[-1]

