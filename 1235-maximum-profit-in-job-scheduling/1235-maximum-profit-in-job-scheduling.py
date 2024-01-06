from typing import List
import bisect  # Importing bisect module for binary search

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:

        # Combine start time, end time, and profit into intervals and sort by start time
        intervals = sorted(zip(startTime, endTime, profit))
        
        # Dictionary for memoization to store computed results for each index
        cache = {}
        
        # Variable to store the final result
        rss = 0

        # Recursive function to find the maximum profit
        def dfs(i):
            # If we reach the end of intervals, return 0 (base case)
            if i == len(intervals):
                return 0
            
            # Check if the result for the current index is already computed
            if i in cache:
                return cache[i]
            
            # Not include the current index, move to the next index
            res = dfs(i+1)
            
            # Include the current index and find the next non-overlapping job using binary search
            j = bisect.bisect(intervals, (intervals[i][1], -1, -1))
            
            # Update the result with the maximum profit considering both cases
            res = max(res, intervals[i][2] + dfs(j))
            
            # Memoize the result for the current index
            cache[i] = res
            
            return res

        # Start the recursive function from the first index (index 0)
        return dfs(0)

# Time Complexity: O(n log n) - Sorting the intervals takes O(n log n) time, where n is the number of jobs.
# Recursive function is called for each job, but memoization avoids redundant calculations.
# Space Complexity: O(n) - The space used for the intervals list, memoization cache, and recursive call stack.
