from typing import List

class Solution:
    # T O(n^2 * d)
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        # Base case: If the number of jobs is less than the number of days, it's impossible.
        if len(jobDifficulty) < d:
            return -1

        # Cache to store already computed results for optimization.
        cache = {}

        # Recursive function to explore different possibilities.
        def dfs(i, d, currMax):
            # If the result for the current state is already in the cache, return it.
            if (i, d, currMax) in cache:
                return cache[(i, d, currMax)]

            # Base case: If all jobs are completed.
            if i == len(jobDifficulty):
                return 0 if d == 0 else float("inf")

            # Base case: If no more days are available.
            if d == 0:
                return float("inf")

            # Update the current maximum difficulty with the maximum of the current job and currMax.
            currMax = max(currMax, jobDifficulty[i])

            # Explore two options:
            # 1. Finishing the current job and moving forward.
            # 2. Stopping with the current job and starting a new day.
            res = min(
                dfs(i+1, d, currMax),          # Option 1
                currMax + dfs(i+1, d-1, -1)    # Option 2
            )

            # Memoize the result in the cache.
            cache[(i, d, currMax)] = res

            return res

        # Start the recursive exploration from the first job.
        return dfs(0, d, -1)



'''
1.) Initialization:
jobDifficulty: The list of difficulty values for each job.
d: The maximum number of days to complete all jobs.

2.) Base Cases:
If the length of jobDifficulty is less than d, return -1 since it's not possible to complete the jobs in the given number of days.

3.)Dynamic Programming:
The main function minDifficulty initializes a cache to store already computed results.
It defines a recursive helper function dfs(i, d, currMax) to explore different possibilities.

4.)Recursive Exploration:
The function explores two options:
dfs(i+1, d, currMax): Finishing the current job and moving forward to the next one.
currMax + dfs(i+1, d-1, -1): Stopping with the current job and starting a new day with a new job.

5.)Base Cases inside Recursive Function:
If (i, d, currMax) is already in the cache, return the cached result.
If i has reached the end of jobDifficulty, return 0 if d == 0 (no more days left) or float("inf") if d > 0 (not enough days to finish all jobs).
If d is 0 (no more days left), return float("inf") as it's not a valid solution.

6.)Update Current Maximum:
Update currMax with the maximum of the current job difficulty and the current currMax.

7.)Calculate Minimum Difficulty:
Calculate the result as the minimum of the two explored options.

8.)Memoization:
Store the result in the cache for future reference.

9.)Return Result:
Return the final result of the recursive exploration starting from the first job.

'''
