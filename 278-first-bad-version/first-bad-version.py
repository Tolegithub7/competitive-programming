# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l, r = 1, n
        res = n
        while l <= r:
            md = (l+r)//2
            if isBadVersion(md): 
                res = md
                r = md-1
            else: l = md+1
        return res
