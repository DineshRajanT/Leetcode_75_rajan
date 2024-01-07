from typing import List

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        res = 0
        freqDiff = [dict() for _ in range(len(nums))]  # Array of hashmap, like a hashmap for each index in the list
        print(freqDiff)

        # Iterate over each index in the array
        for i in range(len(nums)):
            freqDiff[i] = {}  # Dictionary for each index
            # Iterate over previous indices
            for j in range(i):
                # Calculate the difference between the current and previous elements
                diff = nums[j] - nums[i]

                # Get the count of occurrences of the difference at the previous index
                prevIdx = freqDiff[j].get(diff, 0)
                # Increment the result by the count of occurrences at the previous index
                res += prevIdx

                # Update the count of occurrences for the current index and difference
                freqDiff[i][diff] = freqDiff[i].get(diff, 0) + prevIdx + 1

        print(freqDiff)

        return res


'''
Initialization:

freqDiff is initially an array of empty dictionaries.

* Iteration (i=0):
freqDiff[0] is an empty dictionary.
No previous indices, so nothing is updated.

* Iteration (i=1):
freqDiff[1] is an empty dictionary.
Calculate differences: diff = 1 - 2 = -1.
No previous indices, so nothing is updated.

* Iteration (i=2):
freqDiff[2] is an empty dictionary.
Calculate differences: diff = 1 - 3 = -2, diff = 2 - 3 = -1.
At j=1, freqDiff[1][-1] = 0 (no entry), so prevIdx = 0.
Update result: res += 0.
Update freqDiff[2][-2] = 0 + 0 + 1 = 1, freqDiff[2][-1] = 0 + 0 + 1 = 1.

* Iteration (i=3):
freqDiff[3] is an empty dictionary.
Calculate differences: diff = 1 - 4 = -3, diff = 2 - 4 = -2, diff = 3 - 4 = -1.
At j=2, freqDiff[2][-2] = 1, so prevIdx = 1.
Update result: res += 1.
At j=1, freqDiff[1][-1] = 0, so prevIdx = 0.
Update result: res += 0.
Update freqDiff[3][-3] = 0 + 0 + 1 = 1, freqDiff[3][-2] = 0 + 1 + 1 = 2, freqDiff[3][-1] = 0 + 0 + 1 = 1.

* Iteration (i=4):
freqDiff[4] is an empty dictionary.
Calculate differences: diff = 1 - 5 = -4, diff = 2 - 5 = -3, diff = 3 - 5 = -2, diff = 4 - 5 = -1.
At j=3, freqDiff[3][-3] = 2, so prevIdx = 2.
Update result: res += 2.
At j=2, freqDiff[2][-2] = 1, so prevIdx = 1.
Update result: res += 1.
At j=1, freqDiff[1][-1] = 0, so prevIdx = 0.
Update result: res += 0.
Update freqDiff[4][-4] = 0 + 0 + 1 = 1, freqDiff[4][-3] = 0 + 2 + 1 = 3, freqDiff[4][-2] = 0 + 1 + 1 = 2, freqDiff[4][-1] = 0 + 0 + 1 = 1.

* Final Result:
The final result is printed, and the freqDiff array shows the count of occurrences for each index and difference.

'''