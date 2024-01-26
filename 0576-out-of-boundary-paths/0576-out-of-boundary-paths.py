class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        mod = 10**9 + 7

        def moveBall(m, n, move, i, j):
            # Base case: if moves are exhausted, check if the ball is out of bounds
            if move < 0:
                return 0
            
            # If the ball is out of bounds, count this as one way
            if i < 0 or j < 0 or i >= m or j >= n:
                return 1

            # If the result for the current state is already computed, return it
            if dp[move][i][j] != -1:
                return dp[move][i][j]

            # Calculate the total ways to move the ball from the current position
            totalWaysInMove = (
                moveBall(m, n, move - 1, i + 1, j) +
                moveBall(m, n, move - 1, i - 1, j) +
                moveBall(m, n, move - 1, i, j + 1) +
                moveBall(m, n, move - 1, i, j - 1)
            ) % mod

            # Store the result in the DP array and return it
            dp[move][i][j] = totalWaysInMove
            return totalWaysInMove

        # Initialize a 3D DP array with -1 to memoize results
        dp = [[[-1] * n for _ in range(m)] for _ in range(maxMove + 1)]

        # Call the recursive function with initial parameters
        return moveBall(m, n, maxMove, startRow, startColumn) % mod


