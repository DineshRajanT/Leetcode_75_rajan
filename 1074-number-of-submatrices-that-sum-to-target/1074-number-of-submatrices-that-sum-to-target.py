from typing import List

class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        # Get the number of rows and columns in the matrix
        rows = len(matrix)
        cols = len(matrix[0])
        
        # Create a copy of the matrix to store prefix sums
        prefixSumMat = matrix.copy()

        # Calculate prefix sum of the given matrix
        for row in range(rows):
            for col in range(1, cols):
                # Calculate the prefix sum for each column
                # The prefix sum at index 0 will be the element itself
                prefixSumMat[row][col] = prefixSumMat[row][col] + prefixSumMat[row][col - 1]

        # Initialize the count of submatrices with target sum
        ans = 0

        # Iterate over all possible column start points
        for colStart in range(cols):
            # Iterate over all possible column end points starting from colStart
            for colEnd in range(colStart, cols):
                # Initialize the current sum and frequency map for each submatrix
                currSum = 0
                freqMap = {} 
                # Initialize the frequency of 0 sum to 1 
                # Since a prefix sum always contains a zero in the beginning
                freqMap[0] = 1 
                
                # Iterate over all rows to calculate the sum of each submatrix
                for row in range(rows):
                    # Calculate the current sum for the submatrix using prefix sums
                    if colStart:
                        currSum += prefixSumMat[row][colEnd] - prefixSumMat[row][colStart - 1]
                    else:
                        # If colStart is 0, subtract 0 from the prefix sum
                        currSum += prefixSumMat[row][colEnd] - 0

                    # Update the answer by adding the count of submatrices 
                    # with sum equal to target found so far
                    ans += freqMap.get(currSum - target, 0)
                    
                    # Update the frequency map with the current sum
                    freqMap[currSum] = freqMap.get(currSum, 0) + 1

        # Return the total count of submatrices with target sum
        return ans
