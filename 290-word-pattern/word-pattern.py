class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        if len(s) != len(pattern):
            return False
        hash = {}
        for i in range(len(pattern)):
            if pattern[i] in hash:
                if hash[pattern[i]] != s[i]:
                    return False
            else:
                if s[i] in hash.values():
                    return False
                hash[pattern[i]] = s[i]
        return True