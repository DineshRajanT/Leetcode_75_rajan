from collections import defaultdict

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        maxLen = 0
        count = 0
        seen = defaultdict(int)
        seen[0] = -1  # Initialize the first occurrence of 0 cumulative sum at index -1

        for i, num in enumerate(nums):
            if num == 0:
                count -= 1
            else:
                count += 1

            if count in seen:
                maxLen = max(maxLen, i - seen[count])
            else:
                seen[count] = i

        return maxLen
