class Solution:
    def isPalindrome(self, s: str) -> bool:
        ## remove space and special characters and make lower
        s = ''.join(e for e in s if e.isalnum()).lower()
        rev = s[::-1]
        return s == rev