class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Time Complexity: O(m * n)
        # Space Complexity: O(m * n)
        
        #Initialize a 2D matrix dp_mat of size m x n filled with zeros. 
        #This matrix will be used to store the number of unique paths to reach each cell.
        dp_mat = [[0] * n for i in range(m)]
        #dp_mat = [[0] * cols for i in range(rows)]

        #Two nested loops iterate over each cell in reverse order. 

        
        for i in reversed(range(m)):
            for j in reversed(range(n)):

                # If the cell is in the last row (i == m-1) or the last column (j == n-1), 
                # set dp_mat[i][j] to 1, as there is only one way to reach the bottom-right corner from these cells. 

                if i == m-1 or j == n-1:
                    dp_mat[i][j] = 1
                else:
                    # Otherwise, update dp_mat[i][j] with the sum of the values to the right (dp_mat[i][j+1]) and below (dp_mat[i+1][j]).
                    dp_mat[i][j] = dp_mat[i][j+1] + dp_mat[i+1][j]
                
        
        # PRINT
#         for i in range(m):
#             for j in range(n):
#                 print(dp_mat[i][j], end=" ")
#             print("")
            
        return dp_mat[0][0]

#         10 6 3 1 
#         4 3 2 1 
#         1 1 1 1 
        '''
        This dynamic programming approach efficiently calculates the number of unique paths by filling in the matrix with the cumulative sum of paths from the bottom-right corner to the top-left corner. The final result is obtained from dp_mat[0][0].
        '''
        