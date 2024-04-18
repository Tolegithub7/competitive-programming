class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # s = Counter(s)
        # t = Counter(t)
        # if s == t:
        #     return True
        # return False
        return Counter(s) == Counter(t)
        # hash_table = {}
        # if len(s) != len(t):
        #     return False
        # for char in s:
        #     hash_table[char] = hash_table.get(char, 0) + 1
        #     # if char in hash_table:
        #     #     hash_table[char] += 1
        #     # else:
        #     #     hash_table[char] = 1
        # for char in t:
        #     if char in hash_table:
        #         hash_table[char] -= 1
        #         if (hash_table[char] == 0):
        #             del hash_table[char]
        #     else:
        #         return False
        # return True

        # if len(s)!=len(t):return False
        # for char in set(s):
        #     if s.count(char) != t.count(char): return False
        # return True