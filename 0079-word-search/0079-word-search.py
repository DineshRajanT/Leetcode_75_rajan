class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        path = set()

        # DFS function to check if the word can be formed from the current position
        def dfs(i, j, ind):

            # If the index reaches the length of the word, the word is found
            if ind == len(word):
                return True

            # Check boundary conditions and if the current cell is already visited
            if (i < 0 or j < 0 or 
                i >= rows or j >= cols or
                word[ind] != board[i][j] or 
                (i, j) in path):
                return False

            # Mark the current cell as visited
            path.add((i, j))

            # Explore adjacent cells in all four directions
            res = (dfs(i+1, j, ind+1) or
                   dfs(i-1, j, ind+1) or
                   dfs(i, j+1, ind+1) or
                   dfs(i, j-1, ind+1))

            # Backtrack: Remove the current cell from the path set
            path.remove((i, j))

            return res

        # Iterate through each cell in the board to initiate DFS search
        for i in range(rows):
            for j in range(cols):
                if dfs(i, j, 0):  # Start DFS search from each cell
                    return True

        # If no match is found, return False

        # Time complexity: O(rows * cols * 4^len(word))
        # The worst-case time complexity is dominated by the DFS search, which explores
        # all possible paths in each cell (4^len(word) represents the four directions
        # for each step, and len(word) is the maximum depth of the search).

        # Space complexity: O(len(word))
        # The space complexity is determined by the recursive calls and the path set,
        # which stores the visited cells. In the worst case, the maximum depth of
        # the recursion is len(word), and the path set may store up to len(word) cells.
        return False
