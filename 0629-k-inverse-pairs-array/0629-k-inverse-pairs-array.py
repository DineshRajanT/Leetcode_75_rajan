class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        MOD = 10**9 + 7

        # 2D array to store intermediate results
        dp = [[0] * (k + 1) for _ in range(n + 1)]

        # Dynamic Programming: Bottom-up approach
        for i in range(1, n + 1):
            for j in range(k + 1):
                # Base case: There is only one way to have 0 inverse pairs, which is the identity permutation
                if j == 0:
                    dp[i][j] = 1
                else:
                    # Calculate the number of permutations with i elements and j inverse pairs
                    # by subtracting the permutations with (i-1) elements and (j-i) inverse pairs
                    val = (dp[i - 1][j] % MOD - (dp[i - 1][j - i] if j - i >= 0 else 0)) % MOD

                    # Update the current cell with the cumulative number of permutations
                    dp[i][j] = (dp[i][j - 1] + val) % MOD

        # Calculate the final result, considering modulo and adjusting for the last element
        result = (dp[n][k] + MOD - (dp[n][k - 1] if k > 0 else 0)) % MOD

        return result

# Time complexity: O(n * k) - The nested loops iterate over each element in the dp array once
# Space complexity: O(n * k) - The 2D array 'dp' is used to store intermediate results





        '''

        # TOP DOWN APPROACH 
        # Helper function to solve the problem using dynamic programming
        def solve(n, k):
            count = 0

            # Base case: If k is 0, there is only one way (identity permutation)
            if k == 0:
                return 1

            # Base case: If n is 0, no permutations are possible
            if n == 0:
                return 0

            # If the subproblem has already been solved, return the cached result
            if dp[n][k] != -1:
                return dp[n][k]

            # Iterate through possible values for the last element in the permutation
            for i in range(min(k, n - 1) + 1):
                count = (count + solve(n - 1, k - i)) % mod

            # Cache the result for future use
            dp[n][k] = count

            return dp[n][k]

        # Modulo value to handle overflow
        mod = 10**9 + 7

        # 2D array to store results of subproblems
        dp = [[-1] * (k + 1) for _ in range(n + 1)]

        # Call the solve function to get the final result
        return solve(n, k)

# Time complexity: O(n * k^2) - Each subproblem is solved once, and each solution takes O(k) time
# Space complexity: O(n * k) - The 2D array 'dp' is used to store solutions to subproblems

'''