class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        # Initialize an array to store the length of the largest divisible subset ending at each index
        LIS_len = [1] * len(nums)
        # Initialize an array to store the index of the previous element in the largest divisible subset
        prevIndex = [-1] * len(nums)
        # Initialize variables to keep track of the maximum length and its corresponding index
        maxLen = 0
        maxLenIndex = 0

        # If there is only one element, it's the largest divisible subset
        if len(nums) == 1:
            return nums
        # Sort the input array for efficient traversal
        nums.sort()

        # SINCE it is sorted it is enough to check if nums[i] is divisible by nums[j], previousindexes : (j: 0 to i-1)
        # Iterate through each element in the sorted array
        for i in range(0, len(nums)):
            # Iterate in reverse order through the elements before the current element
            for j in reversed(range(0, i)):
                # go back and check from i-1 till 0th index
                # Check if the current element is divisible by the previous element
                # and if extending the subset from the previous element is longer than the current subset
                if nums[i] % nums[j] == 0 and (1 + LIS_len[j]) > LIS_len[i]:
                    # Update the length and previous index arrays
                    LIS_len[i] = 1 + LIS_len[j]
                    prevIndex[i] = j 
            
            # Update the maximum length and its corresponding index
            if LIS_len[i] > maxLen:
                maxLen = LIS_len[i]
                maxLenIndex = i

        # Reconstruct the largest divisible subset using the previous index array
        res = []
        while maxLenIndex != -1:
            res.append(nums[maxLenIndex])
            maxLenIndex = prevIndex[maxLenIndex]

        # Return the result in reverse order to get the correct order
        return res

# Time complexity: O(n^2) - nested loops iterate through all pairs of elements
# Space complexity: O(n) - additional arrays to store lengths and previous indices
