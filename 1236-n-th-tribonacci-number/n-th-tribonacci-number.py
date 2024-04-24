class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1
        return self.tri(0, 1, 1, n - 2)
    
    def tri(self, t1: int, t2: int, t3: int, n: int) -> int:
        if n == 1:
            return t3 + t2 + t1
        t4 = t1 + t2 + t3
        ans = self.tri(t2, t3, t4, n - 1)
        return ans