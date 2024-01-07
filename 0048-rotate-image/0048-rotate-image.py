from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # Define left and right indices for the current layer of the matrix
        l = 0
        r = len(matrix) - 1

        # Iterate through each layer of the matrix
        while l < r:
            # Iterate through each element in the current layer
            for i in range(r - l):
                top, bottom = l, r

                # Save the top left element
                topLeftVal = matrix[top][l + i]

                # Move elements clockwise in the current layer
                matrix[top][l + i] = matrix[bottom - i][l]
                matrix[bottom - i][l] = matrix[bottom][r - i]
                matrix[bottom][r - i] = matrix[top + i][r]
                matrix[top + i][r] = topLeftVal

            # Move to the next layer by adjusting left and right indices
            l += 1
            r -= 1

        """
        Time Complexity:
            - The time complexity is O(N^2), where N is the number of rows (or columns) in the matrix.
              This is because we visit each element in the matrix once, and each operation within the loop is constant time.

        Space Complexity:
            - The space complexity is O(1) as we use a constant amount of extra space for variables regardless of the input size.
        """
