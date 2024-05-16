class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        ans = 0
        n, m = len(matrix), len(matrix[0])

        for i in range(n):
            d = [0] * m
            for j in range(i, n):
                for k in range(m):
                    d[k] += matrix[j][k]
                q = {0: 1}
                s = 0
                for x in d:
                    s += x
                    ans += q.get(s - target, 0)
                    q[s] = q.get(s, 0) + 1

        return ans