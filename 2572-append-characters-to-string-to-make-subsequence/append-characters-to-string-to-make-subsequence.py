class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        # l = r = 0
        # while l < len(s) and r < len(t):
        #     if s[l] == t[r]:
        #         r += 1
        #     l += 1
        # return len(t) - r

        idx, n = 0, len(t)
        for c in s:
            if idx < n and t[idx] == c:
                idx += 1
        return n - idx