from typing import List

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        # Initialize the maximum perimeter
        MaxPerimeter = -1
        # Sort the input array in ascending order
        nums.sort()
        # Initialize a variable to store the prefix sum of the first two elements
        prefixSum = nums[0] + nums[1]

        # Iterate through the array starting from the third element
        for i in range(2, len(nums)):
            # Check if the current element can be part of a valid triangle
            if nums[i] < prefixSum:
                # Update the maximum perimeter if a valid triangle is found
                MaxPerimeter = max(MaxPerimeter, prefixSum + nums[i])
            
            # Update the prefix sum with the current element
            prefixSum += nums[i]

        return MaxPerimeter
# T : O(NlogN)
# S : O(1)