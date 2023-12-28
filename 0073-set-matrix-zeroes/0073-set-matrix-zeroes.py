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
                


