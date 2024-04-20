class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        r = len(matrix)
        c = len(matrix[0])
        self.ps = [[0] * (c+1) for _ in range(r+1)]
        for i in range(r):
            for j in range(c):
                self.ps[i+1][j+1] = self.ps[i][j+1] + self.ps[i+1][j] - self.ps[i][j] + matrix[i][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return ( self.ps[row2+1][col2+1] - self.ps[row2+1][col1] - self.ps[row1][col2+1] + self.ps[row1][col1])


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)