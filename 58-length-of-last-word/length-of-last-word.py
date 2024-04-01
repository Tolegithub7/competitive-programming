class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s1 = s.split()
        return (len(s1[-1]))