from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Initialize an empty list to store the result
        res = []
        # Set the target sum to 0
        target = 0
        # Sort the input list for easier handling of duplicates and to optimize searching
        nums.sort()

        # Iterate through the sorted list, considering each element as the potential first element of the triplet
        for i in range(len(nums)-2):
            # Avoid duplicate elements by skipping identical values
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            # Initialize two pointers, one at the element after the current 'i' and one at the end of the list
            l = i + 1
            r = len(nums) - 1

            # Use two pointers approach to find pairs that sum up to the target
            while l < r:
                currSum = nums[i] + nums[l] + nums[r]
                
                # If the current triplet sums up to the target, add it to the result
                if currSum == target:
                    res.append([nums[i], nums[l], nums[r]])

                    # Avoid duplicate elements by moving the pointers past identical values
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1

                    # Move both pointers to explore other potential triplets
                    l += 1
                    r -= 1

                # If the sum is less than the target, move the left pointer to a larger value
                elif currSum < target:
                    l += 1
                # If the sum is greater than the target, move the right pointer to a smaller value
                elif currSum > target:
                    r -= 1

        return res

# Time complexity: O(n^2) - The main loop runs in O(n), and the two-pointer approach inside also takes O(n) in the worst case.
# Sorting the array initially takes O(n log n), but it doesn't dominate the overall time complexity.
# Space complexity: O(1) - The space used is only for the result list, and it doesn't depend on the input size.
