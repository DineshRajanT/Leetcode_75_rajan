from typing import List

class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        def solve(i, arr):
            # Base case: If the current index i is beyond the array length,
            # return 0 as there are no elements to consider.
            if i >= n:
                return 0

            # If the result for the current index i is already calculated, return it.
            if dp[i] != -1:
                return dp[i]

            maxVal = 0  # Variable to store the maximum value in the current window.
            ans = 0     # Variable to store the maximum sum.

            # Iterate through the current window of size k or less.
            for j in range(i, min(n, i + k)):
                maxVal = max(maxVal, arr[j])
                # Calculate the sum for the current window and recursively solve for the next index.
                ans = max(ans, (j - i + 1) * maxVal + solve(j + 1, arr))

            # Memoize the result for the current index i.
            dp[i] = ans
            return dp[i]

        # Initialize dp array to store memoized results.
        dp = [-1] * len(arr)
        i = 0
        n = len(arr)

        # Start solving from the first index.
        return solve(i, arr)
