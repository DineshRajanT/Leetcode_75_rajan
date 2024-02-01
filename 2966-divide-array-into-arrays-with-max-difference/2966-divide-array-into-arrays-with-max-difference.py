from typing import List

class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        # Sort the input array
        nums.sort()

        # Initialize a list of lists to store the divided arrays
        combArr = [[] for _ in range(len(nums)//3)]

        # Initialize index j to keep track of subarray indices
        j = -1
        for i, val in enumerate(nums):
            # Distribute elements into subarrays of size 3
            if i % 3 == 0:
                j += 1
            combArr[j].append(val)

        # Initialize the result array
        res = []

        # Iterate through subarrays and check the condition
        for comb in combArr:
            # Check if the difference between the maximum and minimum element in the subarray is less than or equal to k
            if max(comb) - min(comb) <= k:
                res.append(comb)
            else:
                return []  # If the condition is not met, return an empty list

        return res

# Time Complexity: O(N log N), where N is the length of the input array 'nums'. Sorting the array dominates the time complexity.
# Space Complexity: O(N), where N is the length of the input array 'nums'. The space required for 'combArr' is proportional to the size of the input array.

