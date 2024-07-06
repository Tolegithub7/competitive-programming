class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        idx = 1
        for i in range(time):
            idx += 1 - 2 * (i % (2 * (n - 1)) >= n - 1)
        return idx