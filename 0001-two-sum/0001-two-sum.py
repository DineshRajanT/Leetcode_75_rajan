from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Dictionary to store the counts of numbers encountered so far
        countsMap = {}
        # List to store the resulting indices
        res = []
        # Iterate through the list of numbers
        for i in range(len(nums)):
            # Calculate the complement needed to achieve the target
            complement = target - nums[i]

            # Check if the complement is already in the countsMap
            if complement in countsMap:
                # If yes, append the current index and the stored index of the complement to the result list
                res.append(i)
                res.append(countsMap[complement])
                # Return the result since there is only one valid solution
                return res
            
            # Update the countsMap with the current number and its index
            countsMap[nums[i]] = i

        # If no solution is found, an empty list is returned
        return res

# Time Complexity: O(n) - The loop iterates through the list once.
# Space Complexity: O(n) - In the worst case, all elements might be stored in the countsMap.
