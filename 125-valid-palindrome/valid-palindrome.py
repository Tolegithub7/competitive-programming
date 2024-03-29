class Solution:
    def isPalindrome(self, s: str) -> bool:
        # s = [c for c in s.lower() if c.isalnum()]
        # return s == s[::-1]
        s = [elt for elt in s.lower() if elt.isalnum()]
        lt, rt = 0, len(s)-1
        while lt < rt:
            if s[lt] != s[rt]:
                return False
            lt += 1
            rt -= 1
        return True