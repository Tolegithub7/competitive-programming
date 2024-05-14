class Solution:
    def getMaximumGold(self, grid: list[list[int]]) -> int:
        max_gold = 0
        rows = len(grid)
        cols = len(grid[0])

        def explore_paths(row, col, current_sum):
            if not 0 <= row < rows or not 0 <= col < cols or grid[row][col] == 0:
                return current_sum

            gold_in_cell = grid[row][col]
            grid[row][col] = 0
            current_sum += gold_in_cell

            current_sum = max(
                explore_paths(row + 1, col, current_sum),
                explore_paths(row - 1, col, current_sum),
                explore_paths(row, col + 1, current_sum),
                explore_paths(row, col - 1, current_sum),
            )

            grid[row][col] = gold_in_cell
            return current_sum

        for start_row in range(rows):
            for start_col in range(cols):
                if grid[start_row][start_col] != 0:
                    max_gold = max(max_gold, explore_paths(start_row, start_col, 0))

        return max_gold