class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        res = 0
        for i in range(numOnes):
            if k>0:
                res += 1
                k -= 1
        for j in range(numZeros):
            if k>0:
                k -= 1
        for l in range(numNegOnes):
            if k>0:
                res -= 1
                k -= 1
        return res