class Solution:
    def numSquares(self, n: int) -> int:

        # Recursive function to find the minimum number of perfect squares
        # that sum up to n
        def solve(n):
            # Base case: if n is non-positive, the answer is 0
            if n <= 0:
                return 0

            # If the solution for n has been computed previously, return it
            if dp[n] != -1:
                return dp[n]

            # Initialize result to n, as n can be expressed as n 1x1 squares
            res = n

            # Iterate through perfect squares up to the square root of n
            for i in range(1, int(n**0.5) + 1):
                square = i * i
                # Update result by considering the current perfect square
                res = min(res, 1 + solve(n - square))

            # Memoize the result for n and return it
            dp[n] = res
            return res

        # Initialize an array to memoize solutions for subproblems
        dp = [-1] * (n + 1)

        # Time Complexity: O(n * sqrt(n))
        # In the worst case, each value from 1 to n needs to be computed,
        # and for each value, we iterate up to the square root of n.

        # Call the recursive function to find the solution for n
        return solve(n)

# Space Complexity: O(n)
# The space complexity is dominated by the memoization array of size n + 1.
