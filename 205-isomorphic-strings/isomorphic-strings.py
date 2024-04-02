class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hash1, hash2 = {}, {}
        # for i in range(len(s)):
        for char1, char2 in zip(s, t):
            # char1, char2 = s[i], s[2]
            if ((char1 in hash1 and hash1[char1] != char2) or (char2 in hash2 and hash2[char2]!=char1)):
                return False
            hash1[char1] = char2
            hash2[char2] = char1
        return True