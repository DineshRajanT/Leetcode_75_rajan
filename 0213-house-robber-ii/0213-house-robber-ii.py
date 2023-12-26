class Solution:
    # T : O(n)
    # S : O(1)
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        # using same logic in HouseRobber 1 building DP arrays...
        def robHelper(nums):
            rob1, rob2 = 0, 0
            for n in nums:
                temp = max(rob1 + n, rob2)
                rob1 = rob2
                rob2 = temp
            return rob2
        return max(robHelper(nums[1:]), robHelper(nums[:-1]))
        # Since it is circular call this func twice one without including the first element and 
        # second call including the first element but exlcuding the last element and yieldind the max of two func calls



# class Solution:
#     # T : O(n)
#     # S : O(n)
#     def rob(self, nums: List[int]) -> int:
#         if not nums:
#             return 0
#         if len(nums) == 1:
#             return nums[0]
#         # using same logic in HouseRobber 1 building DP arrays...
#         def rob_helper(nums):
#             dp = [0] * len(nums)
#             dp[0] = nums[0]
#             dp[1] = max(nums[0], nums[1])

#             for i in range(2, len(nums)):
#                 dp[i] = max(dp[i-1], dp[i-2] + nums[i])

#             return dp[-1]

#         # Two scenarios: rob the first house or don't rob the first house
#         return max(rob_helper(nums[1:]), rob_helper(nums[:-1]))
