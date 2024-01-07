from typing import List

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        
        # Initialize variables to keep track of total count, previous count, and current count
        totalSum = 0
        prev = 0
        curr = 0

        # Iterate from the 3rd element to the end of the array
        for i in range(2, len(nums)):
            
            # Check if the current subsequence forms an arithmetic slice
            if (nums[i] - nums[i-1]) == (nums[i-1] - nums[i-2]):
                # If true, update the previous count 
                prev = prev + 1
                
            else:
                # If not, reset the current count to 0
                prev = 0
            
            totalSum += prev

        # Return the total count of arithmetic slices
        return totalSum

# Time Complexity: O(n) - Iterating through the array once
# Space Complexity: O(1) - Constant space, as only a few variables are used, not dependent on the input size



'''
from typing import List

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        
        # Initialize an array to store the count of arithmetic slices ending at each index
        dp = [0] * len(nums)

        # Iterate from the 3rd element to the end of the array
        for i in range(2, len(nums)):
            
            # Check if the current subsequence forms an arithmetic slice
            if (nums[i] - nums[i-1]) == (nums[i-1] - nums[i-2]):
                # If true, extend the arithmetic slice from the previous index
                dp[i] = dp[i-1] + 1
            else:
                # If not, reset the count to 0
                dp[i] = 0
            
        # For debugging purposes, print the dp array
        print(dp)

        # Sum up all counts in the dp array to get the total number of arithmetic slices
        return sum(dp)

# Time Complexity: O(n) - Iterating through the array once
# Space Complexity: O(n) - Using an additional array 'dp' of the same length as the input array


'''