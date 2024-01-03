from typing import List

class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        # Initialize the total number of beams
        totalBeams = 0
        # Get the number of rows and columns in the bank
        rows = len(bank)
        cols = len(bank[0])
        # Initialize pointers for two consecutive rows
        first = 0
        second = 1

        # Loop through the rows of the bank
        while second < rows:
            # Count the number of '1's in the current and next row
            C1 = bank[first].count('1')
            C2 = bank[second].count('1')

            # Check if both rows have at least one '1'
            if C1 and C2:
                # Increment the total beams count by the product of '1's in the two rows
                totalBeams += C1 * C2
                # Move to the next pair of rows
                first += 1
                second += 1

            else:
                # If the first row has no '1's, move to the next row
                if C1 == 0:
                    first += 1
                # If the second row has no '1's, move to the next row
                if C2 == 0:
                    second += 1
                # If both pointers point to the same row, move the second pointer to the next row
                if first == second:
                    second += 1

        # Return the total number of beams
        return totalBeams
