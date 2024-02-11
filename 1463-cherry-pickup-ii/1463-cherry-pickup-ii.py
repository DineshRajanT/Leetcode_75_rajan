from typing import List

class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        def dfs(grid, i, robot1j, robot2j, memo):
            # Base case: if reached the bottom row, return 0
            if i == ROWS:
                return 0

            # Check for out-of-bounds conditions for robot positions
            if robot1j < 0 or robot2j < 0 or robot1j >= COLS or robot2j >= COLS:
                return 0

            # Check if result for this state is already memoized
            if memo[i][robot1j][robot2j] != -1:
                return memo[i][robot1j][robot2j]

            # Collect cherries from the current cell
            res = grid[i][robot1j]
            if robot1j != robot2j:
                res += grid[i][robot2j]

            # Explore all possible next positions for both robots in the next row
            maxNextRow = 0
            for x in range(robot1j-1, robot1j+2):
                for y in range(robot2j-1, robot2j + 2):
                    maxNextRow = max(maxNextRow, dfs(grid, i+1, x, y, memo))

            # Accumulate the result and memoize it
            res += maxNextRow
            memo[i][robot1j][robot2j] = res
            return res

        ROWS = len(grid)
        COLS = len(grid[0])

        # Initialize memoization array with -1
        memo = [[[-1] * COLS for _ in range(COLS)] for _ in range(ROWS)]

        # Start DFS from the top row with both robots at the specified positions
        res1 = dfs(grid, 0, 0, COLS-1, memo)
        return res1

# Time Complexity: O(ROWS * COLS^2) - Each cell in the memo array is visited once, and for each cell, the function may recurse up to COLS^2 times.
# Space Complexity: O(ROWS * COLS^2) - The memo array is used to store intermediate results for each cell in the grid, and its size is proportional to the grid size.
