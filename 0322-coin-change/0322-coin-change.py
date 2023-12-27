class Solution:
    # T : O(amount * len(coins))
    # S : O(amount)

    def coinChange(self, coins, amount):
        # Initialize an array dp to store the minimum number of coins needed for each amount
        dp = [float('inf')] * (amount + 1) # so it will be [0...amount]
        
        # Base case: It takes 0 coins to make up an amount of 0
        dp[0] = 0

        # Iterate over each amount from 1 to the target amount
        for a in range(1, amount + 1):
            # Iterate over each coin denomination
            for c in coins:
                # Check if subtracting the current coin from the current amount is valid
                if a - c >= 0:
                    # Update dp[a] with the minimum number of coins needed
                    dp[a] = min(dp[a], 1 + dp[a - c])

        # Check if it's possible to make up the target amount
        return dp[amount] if dp[amount] != float('inf') else -1


# *** Example:

# coins = [1, 2, 5]
# amount = 11


# * Initialization of dp array:
#     dp = [float('inf')] * (11 + 1)
#     Initialize dp array with [inf, inf, inf, inf, inf, inf, inf, inf, inf, 
#                                 inf, inf, inf, inf].

# * Base case:
#     dp[0] = 0
#     Set dp[0] to 0.

# * Nested Loop to Populate dp:
# For a = 1:
#     Check each coin (c) in [1, 2, 5].
#     For c = 1: Update dp[1] = min(inf, 1 + dp[1 - 1]) = 1.
#     For c = 2: Update dp[1] = min(1, inf) = 1.
#     For c = 5: Update dp[1] = min(1, inf) = 1.
# For a = 2:
#     Check each coin (c) in [1, 2, 5].
#     For c = 1: Update dp[2] = min(inf, 1 + dp[2 - 1]) = 2.
#     For c = 2: Update dp[2] = min(2, 1 + dp[2 - 2]) = 1.
#     For c = 5: Update dp[2] = min(1, inf) = 1.
#     Similarly, continue for a = 3, 4, ... up to a = 11.

# * Final Result:
#     return dp[11] if dp[11] != float('inf') else -1
    
# * The function returns dp[11], which is 3. The fewest number of coins needed to make up the amount 11 is 3 (5 + 5 + 1).