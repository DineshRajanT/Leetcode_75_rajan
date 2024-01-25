from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Get the number of rows and columns in the grid
        rows = len(grid)
        cols = len(grid[0])
        
        # Initialize the variable to count the number of islands
        islandCount = 0    

        # Loop through each cell in the grid
        for i in range(rows):
            for j in range(cols):
                # If the cell contains '1', it is part of an island
                if grid[i][j] == '1':
                    # Increment the island count and perform DFS to mark all connected '1's as visited
                    islandCount += 1
                    self.dfs(grid, rows, cols, i, j)
        
        # Return the total number of islands
        return islandCount

    def dfs(self, grid, rows, cols, i, j):
        # Check if the current cell is out of bounds or already visited
        if i < 0 or i == rows or j < 0 or j == cols or grid[i][j] == '0':
            return
        
        # Mark the current cell as visited by changing '1' to '0'
        grid[i][j] = '0'
        
        # Recursively perform DFS on adjacent cells
        self.dfs(grid, rows, cols, i-1, j)  # Up
        self.dfs(grid, rows, cols, i+1, j)  # Down
        self.dfs(grid, rows, cols, i, j-1)  # Left
        self.dfs(grid, rows, cols, i, j+1)  # Right
