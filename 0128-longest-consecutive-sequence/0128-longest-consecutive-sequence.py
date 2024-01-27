from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Check if the input list is empty
        if not nums:
            return 0

        # Create a set to efficiently check the presence of elements
        numSet = set()
        for eachVal in nums:
            numSet.add(eachVal)

        # Initialize the global count for the longest consecutive sequence
        globalCount = 1

        # Iterate through each unique value in the set
        for val in numSet:
            # Initialize current count for the current consecutive sequence
            currCount = 0

            # Check if the current value minus 1 is present in the set
            if val - 1 in numSet:
                continue  # If present, skip to the next value

            # If the current value minus 1 is not present in the set,
            # it means the current value is the start of a consecutive sequence
            elif val - 1 not in numSet:
                j = val
                # Continue counting the consecutive sequence by incrementing the value
                # until a value is not present in the set
                while j in numSet:
                    currCount += 1
                    j += 1

                # Update the global count with the maximum of the current count and global count
                globalCount = max(globalCount, currCount)

        # Return the final global count representing the longest consecutive sequence
        return globalCount
