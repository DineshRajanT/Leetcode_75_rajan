from typing import List

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        # Dictionary to cache computed values for optimization
        cache = {}

        # Recursive function to find the minimum falling path sum
        def findSum(i, j):
            # Check if the result for this (i, j) pair is already in the cache
            if (i, j) in cache:
                return cache[(i, j)]

            # Base case: if we reached the last row, return 0
            if i == len(matrix):
                return 0

            # Base case: if the column index is out of bounds, return positive infinity
            if j < 0 or j >= len(matrix[0]):
                return float("inf")

            # Recursive calls for right, up, and left directions
            right = findSum(i + 1, j + 1)
            up = findSum(i + 1, j)
            left = findSum(i + 1, j - 1)

            # Compute the current falling path sum and update the cache
            cache[(i, j)] = matrix[i][j] + min(right, up, left)

            return cache[(i, j)]

        # Initialize a variable to track the minimum falling path sum over all starting columns
        global_min = float("inf")

        # Iterate through all possible starting columns in the first row
        for j in range(len(matrix[0])):
            # Update the global minimum with the minimum falling path sum for the current starting column
            global_min = min(global_min, findSum(0, j))

        # Return the overall minimum falling path sum
        return global_min

# Time Complexity: O(m * n) - where m is the number of rows and n is the number of columns in the matrix
# Space Complexity: O(m * n) - due to the cache dictionary storing results for each (i, j) pair
