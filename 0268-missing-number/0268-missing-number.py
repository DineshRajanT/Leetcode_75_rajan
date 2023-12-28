from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # Create a list of all numbers from 0 to len(nums)
        visited = set(range(len(nums) + 1))

        # Remove each number in nums from the set
        for num in nums:
            visited.discard(num)

        # The remaining element in the set is the missing number
        return next(iter(visited))
