class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Sort intervals based on the start of each interval
        intervals.sort(key=lambda ele: ele[0])

        # Initialize the output list with the first interval
        output = [intervals[0]]

        # Iterate through the sorted intervals
        for start, end in intervals[1:]:
            lastEnd = output[-1][1]  # End of the last interval in the output list

            # Check for overlap between the current interval and the last interval in the output list
            if start <= lastEnd:
                # Merge the overlapping intervals by updating the end of the last interval in the output list
                output[-1][1] = max(lastEnd, end)
            else:
                # If no overlap, add the current interval to the output list
                output.append([start, end])

        return output






'''
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        intervals.sort()
        outIntervals = [intervals[0]]

        for i in range(1, len(intervals)):
            a, b = outIntervals[-1]
            c, d = intervals[i]

            if b >= c:
                outIntervals[-1] = [min(a, c), max(b, d)]
            else:
                outIntervals.append([c, d])

        return outIntervals
'''