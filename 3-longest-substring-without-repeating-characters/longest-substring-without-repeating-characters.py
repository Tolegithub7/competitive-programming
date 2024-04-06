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
        mx = 0 
        for end in range(len(s)):
            cur = s[end]
            if cur in seen and seen[cur]>=start:
                start = seen[cur] + 1
            seen[cur] = end
            mx = max(mx, end-start+1)
        return mx
