class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currMax = float("-inf")
        globalMax = float("-inf")
        for i in range(len(nums)):
            currMax = max(nums[i], currMax + nums[i])
            globalMax = max(currMax,globalMax)
        return globalMax


        