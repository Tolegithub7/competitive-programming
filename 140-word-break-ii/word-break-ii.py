class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
        def backtrack(index, curr):
            if index == n:
                res.append(curr)
                return
            for i in range(index, n):
                if s[index:i+1] in wordDict: backtrack(i+1, curr + s[index:i+1] + (" " if i < n-1 else ""))
        
        res = []
        n = len(s)
        backtrack(0, "")

        return res