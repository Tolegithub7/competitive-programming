class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
#         lenRow, lenCol = len(points), len(points[0])
#         leftMax, rightMax = [0] * lenCol, [0] * lenCol
#         currRow = points[0]
#         for row in points[1:]:
#             leftMax[0], rightMax[-1] = currRow[0], currRow[-1]
#             for i in range(1, lenCol):
#                 leftMax[i] = max(leftMax[i-1]-1, currRow[i])
#             for i in range(lenCol-2, -1, -1):
#                 rightMax[i] = max(rightMax[i+1]-1, currRow[i])
#             for i in range(lenCol):
#                 currRow[i] = max(leftMax[i], rightMax[i]) + row[i]
            
#         return max(currRow)

        m, n = len(points), len(points[0])
        for i in range(m - 1):
            for j in range(1, n):
                points[i][j] = max(points[i][j], points[i][j - 1] - 1)
            for j in range(n - 2, -1, -1):
                points[i][j] = max(points[i][j], points[i][j + 1] - 1)
            for j in range(n):
                points[i + 1][j] += points[i][j]   
        return max(points[m - 1])