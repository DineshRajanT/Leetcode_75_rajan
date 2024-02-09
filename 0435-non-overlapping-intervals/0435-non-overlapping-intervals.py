class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # Check for empty intervals or single interval case
        if not intervals or len(intervals) == 1:
            return 0

        # Initialize the variable to count the number of overlapping intervals
        res = 0

        # Sort intervals based on the start time of each interval
        intervals.sort(key=lambda x: x[0])

        # Initialize the end time of the first interval
        lastEnd = intervals[0][-1]

        # Iterate through the sorted intervals
        for start, end in intervals[1:]:
            # Check for overlapping intervals
            if start < lastEnd:
                # Overlapping interval found, choose the one with a smaller end time to minimize impact
                res += 1
                lastEnd = min(lastEnd, end)
            else:
                # No overlap, update lastEnd with the end time of the current interval
                lastEnd = end

        # Return the count of overlapping intervals
        return res
