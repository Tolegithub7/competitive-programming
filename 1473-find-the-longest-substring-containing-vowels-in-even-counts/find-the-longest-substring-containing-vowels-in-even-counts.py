class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        dic_mask = {'a' : 1, 'e' : 2, 'i' : 4, 'o' : 8, 'u' : 16}
        d = {}
        ans, pref, d[0] = 0, 0, -1
        for i, ch in enumerate(s):
            pref ^= dic_mask.get(ch, 0)
            ans = max(i - d.setdefault(pref, i), ans)
        return ans