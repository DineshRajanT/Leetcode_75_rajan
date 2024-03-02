from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n  # Initialize the result array with zeros
        l = 0  # Left pointer starting from the beginning of the array
        r = n - 1  # Right pointer starting from the end of the array
        idx = n - 1  # Index to fill the result array, starting from the end

        while l <= r:  # Continue until the left pointer crosses the right pointer
            l_sqrd = nums[l] ** 2  # Square the value at the left pointer
            r_sqrd = nums[r] ** 2  # Square the value at the right pointer

            if l_sqrd >= r_sqrd:
                result[idx] = l_sqrd  # Assign the squared value to the result array
                l += 1  # Move the left pointer to the right
            else:
                result[idx] = r_sqrd  # Assign the squared value to the result array
                r -= 1  # Move the right pointer to the left

            idx -= 1  # Move the result array index to the left

        return result  # Return the sorted array of squared values
