class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        n = len(rowSum)
        m = len(colSum)
        
        mat = [[0]*m for i in range(n)]
        i = 0
        j = 0
        while i < n and j < m:
            mat[i][j] = min(rowSum[i], colSum[j])
            if rowSum[i] == colSum[j]:
                i += 1
                j += 1
            elif rowSum[i] > colSum[j]:
                rowSum[i] -= colSum[j]
                j += 1
            else:
                colSum[j] -= rowSum[i]
                i += 1

        return mat