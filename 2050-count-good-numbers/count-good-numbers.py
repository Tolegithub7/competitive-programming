class Solution:
    def __init__(self):
        self.MOD = 10**9 + 7
    @cache
    def countGoodNumbers(self, n: int) -> int:
        if n == 1: return 5
        if n == 2: return 20
        if (n // 2) % 2 == 0:
            return (self.countGoodNumbers(n//2) * self.countGoodNumbers((n+1)//2)) % self.MOD
        else:
            return (self.countGoodNumbers(n//2+1) * self.countGoodNumbers((n+1)//2-1)) % self.MOD