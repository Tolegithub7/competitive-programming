class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:

        rows,cols = len(grid),len(grid[0])
        for r in range(rows):
            if grid[r][0] == 0:
                for c in range(cols):
                    if grid[r][c] == 0:
                        grid[r][c] = 1
                    else:
                        grid[r][c] = 0

        counts = collections.defaultdict(int)
        for c in range(1,cols):
            for r in range(rows):
                if grid[r][c] == 0:
                    counts[c] += 1

        res = rows * (2**(cols-1))
        for c in range(1,cols):
            res += max(counts[c],rows - counts[c])*2**(cols - c - 1)

        return res