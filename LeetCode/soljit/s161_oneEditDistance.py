class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        if len(s) == 0 and len(t) == 0:
            return False

        # Ensure that s is shorter than t.
        if len(s) > len(t):
            return self.isOneEditDistance(t, s)

        onePass = False
        for x in range(len(s)):
            if t[x] != s[x]:
                # if strings have the same length
                if len(s) == len(t):
                    return s[x + 1:] == t[x + 1:]
                else:  # if strings have different lengths
                    return s[x:] == t[x + 1:]
        # If there is no diffs on ns distance
        # the strings are one edit away only if
        # t has one more character.
        return len(s) + 1 == len(t)