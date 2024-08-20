class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        @cache  #
        def wordBrk(i):
            if i == n:
                return True
            for word in wordDict:
                j = i
                useWord = True
                for ch in word:
                    if j >= n or s[j] != ch:
                        useWord = False
                        break
                    j += 1
                if useWord and wordBrk(j):
                    return True
            return False
        return wordBrk(0)