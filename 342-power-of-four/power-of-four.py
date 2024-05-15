class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        while (n>4):
            n /= 4
        if n==1 or n==4:
            return True
        return False



















        