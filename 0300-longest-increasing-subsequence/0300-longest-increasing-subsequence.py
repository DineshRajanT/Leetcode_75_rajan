class Solution:
    # T : O(n^2)
    # S : O(n)
    # Actually you have a better solution O(nlogn) using binary search
    def lengthOfLIS(self, nums: List[int]) -> int:
        LIS = [1] * len(nums)
        res = 0

        for i in range(len(nums)-1, -1, -1):
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i], 1+LIS[j])
        return max(LIS)

        