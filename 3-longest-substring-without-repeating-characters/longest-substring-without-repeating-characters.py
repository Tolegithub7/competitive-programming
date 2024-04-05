class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # l = ans = 0
        # seen = {}zzz
        # for r in range(len(s)):
        #     if s[r] in seen:
        #         l = max(l, seen[s[r]] + 1)
        #     ans = max(ans, r-l+1)
        #     seen[s[r]] = r 
        # return ans

        seen = {}
        start = 0
        max_length = 0
        for idx in range(len(s)):
            cur = s[idx]
            if cur in seen and seen[cur] >= start:
                start = seen[cur] + 1
            seen[cur] = idx
            max_length = max(max_length, idx-start+1)
        return max_length