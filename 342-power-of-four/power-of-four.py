class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n == 1: return True
        if n <= 1: return False

        return self.isPowerOfFour(n/4)
        # while (n>4):
        #     n /= 4
        # if n==1 or n==4:
        #     return True
        # return False























         # if n==1:
        #     return True
        # while (n >= 4):

        #     if n/4 >= 4 :
        #         n = n/4
        #     elif n/4 == 1:
        #         return True
        #     else: return False