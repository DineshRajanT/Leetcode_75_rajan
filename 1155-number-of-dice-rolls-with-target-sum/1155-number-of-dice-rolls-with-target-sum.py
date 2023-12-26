class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:

        MOD = 10**9 + 7

        # Initialize a 2D array dp to store the number of ways to achieve each target sum
        # dp[i][j] represents the number of ways to get sum j using i dice
        dp = [[0] * (target+1) for i in range(n+1)]

        # Base case : There is one way to get sum 0 with 0 dice
        dp[0][0] = 1

        for dice in range(1, n+1): # Iterate over the number of dice
            for targetVal in range(1, target+1): # Iterate over the target sums
                for diceFacingUp in range(1, k+1): # Iterate over the faces of the die

                    # check if targetVal - diceFacingUp is non-negative to avoid accessing invalid indices.
                    if targetVal - diceFacingUp >=0:

                        # Update the number of ways to achieve the current target sum
                        dp[dice][targetVal] = (dp[dice][targetVal] + 
                                            dp[dice-1][targetVal - diceFacingUp]) % MOD
                                            # Check th eprevious row and take the sum from previous column till first index...
        return dp[n][target]
        