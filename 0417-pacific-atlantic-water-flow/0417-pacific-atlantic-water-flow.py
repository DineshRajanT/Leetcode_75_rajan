from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        # Get the number of rows and columns in the input matrix
        ROWS, COLS = len(heights), len(heights[0])
        
        # Initialize sets to keep track of cells reachable by Pacific and Atlantic
        atlantic, pacific = set(), set()

        # Depth-First Search (DFS) function to explore cells
        def dfs(r, c, visit, prevHeight):
            # Check if the cell has already been visited or if it's out of bounds
            # or if the current height is lower than the previous height
            if ((r, c) in visit or 
                r < 0 or c < 0 or r == ROWS or c == COLS or # check out of bounds
                heights[r][c] < prevHeight): # going from the ocean towards inside of island 
                return 

            # Mark the cell as visited
            visit.add((r, c))

            # Explore neighboring cells in all four directions
            dfs(r + 1, c, visit, heights[r][c])
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])

        # Start DFS from the top and bottom rows
        for c in range(COLS):
            dfs(0, c, pacific, heights[0][c])               # Pacific reachable cells (first row)
            dfs(ROWS - 1, c, atlantic, heights[ROWS-1][c])   # Atlantic reachable cells (last row)

        # Start DFS from the left and right columns
        for r in range(ROWS):
            dfs(r, 0, pacific, heights[r][0])               # Pacific reachable cells (first col)
            dfs(r, COLS - 1, atlantic, heights[r][COLS - 1]) # Atlantic reachable cells (last col)

        # Find cells that are reachable from both Pacific and Atlantic
        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pacific and (r, c) in atlantic:
                    res.append([r, c])

        return res 

# Time Complexity: The DFS function is called for each cell in the matrix once, so the time complexity is O(ROWS * COLS).
# Space Complexity: The space complexity is O(ROWS * COLS) as we are using sets to keep track of visited cells. Additionally, the recursion depth for DFS can be at most O(ROWS + COLS).