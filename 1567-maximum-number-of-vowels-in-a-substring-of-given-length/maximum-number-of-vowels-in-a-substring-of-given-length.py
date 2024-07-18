class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set(['a', 'e', 'i', 'o', 'u'])
        l, vowelCount, maxCount = 0, 0, 0
        for r in range(len(s)):
            if r - l + 1 > k:
                if s[l] in vowels:
                    vowelCount -= 1
                l += 1
            if s[r] in vowels:
                    vowelCount += 1
                    maxCount = max(maxCount, vowelCount)
        return maxCount
        