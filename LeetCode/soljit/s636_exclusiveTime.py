class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        lenL = len(logs)

        stack = []
        res = [0] * n
        i = 0
        prevStTime = 0
        while i < lenL:
            s = logs[i].split(':')
            newPrc = int(s[0])
            newTime = int(s[2])
            if s[1] == 'start':
                if stack:  ## If
                    res[stack[-1]] = res[stack[-1]] + newTime - prevStTime
                stack.append(newPrc)
                print('putting ' + str(newPrc) + '  ' + str(newTime))
                prevStTime = newTime
            else:
                endPrc = stack.pop()
                res[endPrc] = res[endPrc] + newTime - prevStTime + 1
                prevStTime = newTime + 1
                print('pulling out ' + str(endPrc) + '   ' + str(newPrc) + '  ' + str(newTime))

            i += 1
        return res
