class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # Initialize the output list to store merged intervals
        output = []

        # Initialize the start and end of the new interval
        lastStart = newInterval[0]
        lastEnd = newInterval[1]

        # Iterate through existing intervals
        for start, end in intervals:
            # Case 1: The current interval is completely before the new interval
            if end < lastStart:
                # Add the current interval to the output
                output.append([start, end])
            # Case 2: The current interval is completely after the new interval
            elif start > lastEnd:
                # Add the merged or new interval to the output
                output.append([lastStart, lastEnd])
                # Update lastStart and lastEnd to the current interval
                lastStart, lastEnd = start, end
            # Case 3: There is an overlap between the current interval and the new interval
            else:
                # Merge the current interval with the new interval
                lastStart = min(lastStart, start)
                lastEnd = max(lastEnd, end)

        # Add the last merged or new interval to the output
        output.append([lastStart, lastEnd])

        return output
        
# T : O(n)
# S : O(1)