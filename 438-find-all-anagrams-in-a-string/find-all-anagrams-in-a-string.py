class Solution:
    def findAnagrams(self, s, p):
        # result = []
        # target_counts = collections.Counter(p)
        # win = collections.Counter(s[:len(p) - 1])
        # for i in range(len(p) - 1, len(s)):
        #     curr_char = s[i]
        #     win[curr_char] += 1
        #     if win == target_counts:
        #         result.append(i - len(p) + 1)
        #     win[s[i - len(p) + 1]] -= 1
        #     if win[s[i - len(p) + 1]] == 0:
        #         del win[s[i - len(p) + 1]]
        # return result
        
        result = []
        window = Counter(s[:len(p)-1])
        target = Counter(p)
        for r in range(len(p)-1, len(s)):
            current = s[r]
            window[current] += 1
            if window == target:
                result.append(r-len(p)+1)
            window[s[r-len(p)+1]] -= 1
            if window[s[r-len(p)+1]] == 0:
                del window[s[r-len(p)+1]]
        return result