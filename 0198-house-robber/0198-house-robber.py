class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0

        dp = [0] * len(nums)
        dp[0] = nums[0]
        print(dp) 
        prevMax = -1
        
        for i in range(1, len(nums)):
            prevMax = max(prevMax, dp[i-2])
            print(f"prevMax at {i}:",prevMax)
            dp[i] = nums[i] + prevMax

        print(dp)
        return max(dp)
        
# Approach
# 1.) Initialization:

# dp is an array used to store the maximum amount of money that can be robbed up to the ith house.
# dp[0] is initialized with the money in the first house (nums[0]), as there is only one house to rob initially.
# 2.) Dynamic Programming Loop:

# We iterate through the houses starting from the second one (for i in range(1, len(nums))).
# For each house, we calculate the maximum amount that can be robbed up to that house without alerting the police.
# prevMax is used to keep track of the maximum amount of money that can be robbed without robbing the adjacent house.
# 3.) Update prevMax:

# prevMax is updated by taking the maximum value between the current prevMax and the amount of money that can be robbed two houses ago (dp[i-2]). This ensures that we skip robbing the adjacent house.
# 4.) Update dp[i]:

# dp[i] is updated by adding the money in the current house (nums[i]) to the calculated prevMax.
# This represents the maximum amount of money that can be robbed up to the current house.
# 5.) Return the Maximum:

# Finally, we return the maximum value in the dp array, which represents the maximum amount of money that can be robbed without alerting the police.
# **** Let's take an example: ****

# Input : nums = [2, 7, 9, 3, 1]

# Initially, dp is [2, 0, 0, 0, 0] (initialized with the money in the first house).

# For the second house, prevMax is updated to 2, and dp[1] is updated to 2 + 7 = 9.

# For the third house, prevMax becomes 2 (maximum between 2 and 0), and dp[2] is updated to 9 + 9 = 18.

# This process continues, and at the end, max(dp) gives the maximum amount of money that can be robbed, which is 12 in this case.

# Complexity
# Time complexity: O(N)
# Space complexity: O(N)











        # firstPt = 0
        # secondPt = 0

        # if len(nums)<=2:
        #     return max(nums) 

        # for i in range(0,len(nums), 2):  
        #     firstPt += nums[i]

        #     if i!= len(nums)-1:
        #         secondPt += nums[i+1]
        
        #     print(firstPt, secondPt)
        # return max(firstPt, secondPt)



        