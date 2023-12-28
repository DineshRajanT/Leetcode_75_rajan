class Solution:
    
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        rows = len(matrix)
        cols = len(matrix[0])

        def replaceNums(matrix, i, j ,num):
            # FILL COLUMNS
            for idx in range(len(matrix)):
                if matrix[idx][j]!=0:
                    matrix[idx][j] = num

            # FILL ROWS
            for idx in range(len(matrix[0])):
                if matrix[i][idx]!=0:
                    matrix[i][idx] = num

            return matrix

        # Replace with same huge number first and then filter them and replace it with zeros.
        # to avoid confusion between actual existing zeros and filled zeros 
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    matrix = replaceNums(matrix, i, j, float("-inf"))

        # Just printing
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == float("-inf"):
                    matrix[i][j] = 0
                    print(matrix[i][j], end=" ")
            print()
                
'''
To further reduce the time complexity, we can eliminate the need for marking and traversing entire rows and columns. Instead, we can use the first row and first column of the matrix to store information about the presence of zeros in the respective rows and columns. This will reduce the time complexity to O(rows * cols):'''

'''
from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])

        # Use the first row and first column as markers
        first_row_has_zero = any(matrix[0][j] == 0 for j in range(cols))
        first_col_has_zero = any(matrix[i][0] == 0 for i in range(rows))

        # Mark the first row and first column based on the rest of the matrix
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0

        # Set zeros based on the markers in the first row and first column
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # Set zeros for the first row and first column if needed
        if first_row_has_zero:
            for j in range(cols):
                matrix[0][j] = 0
        if first_col_has_zero:
            for i in range(rows):
                matrix[i][0] = 0

'''