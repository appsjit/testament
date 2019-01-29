class Solution:
    def isValid(self, s):
        if len(s) % 2 != 0:
            return False
        stack = []
        match = set([('(', ')'), ('[', ']'), ('{', '}')])

        for c in s:
            if c in ('(', '[', '{'):
                stack.append(c)

            if c in (')', ']', '}'):
                if len(stack) == 0:
                    return False
                else:
                    lastOp = stack.pop()
                    if (lastOp, c) not in match:
                        return False

        if (len(stack) > 0):
            return False

        return True

        """
        :type s: str
        :rtype: bool
        """
