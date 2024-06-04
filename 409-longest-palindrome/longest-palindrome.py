class Solution:
    def longestPalindrome(self, s: str) -> int:
        hash = {}
        for char in s:
            hash[char] = hash.get(char, 0) + 1
        length = 0
        for freq in hash.values():
            length += freq // 2 * 2
        if any(freq % 2 == 1 for freq in hash.values()):
            length += 1
        return length