class Solution:
    # T : O(n)
    # S : O(1)
    def canJump(self, nums: List[int]) -> bool:
        maxTravelIndex = 0
        lastIdx = len(nums) - 1

        for i in range(len(nums)):
            # Check if the current index is not reachable
            if i > maxTravelIndex:
                return False
            
            # Update maxIdxTravel to the maximum reachable index
            maxTravelIndex = max(maxTravelIndex, i + nums[i])

            # Check if we have reached or passed the last index
            if maxTravelIndex >= lastIdx:
                return True

        # If we haven't reached or passed the last index after iterating through the array
        return False
'''
1.)Initialization:
* maxIdxTravel is initialized to 0, representing the maximum index that can be reached from the current position.

* lastIdx is set to the index of the last element in the array.
Iteration through the Array:

* The code iterates through each index in the array using the loop for i in range(len(nums)).

2.)Check for Unreachable Index:

* At each step, it checks if the current index i is greater than the maxIdxTravel. If true, it means the current index is not reachable, and the function returns False.

3.)Update maxIdxTravel:

* The code updates maxIdxTravel to the maximum value between the current maxIdxTravel and the index that can be reached from the current position (i + nums[i]).

4.)Check for Last Index Reachability:

* After updating maxIdxTravel, it checks if maxIdxTravel is greater than or equal to the last index (lastIdx). If true, it means we can reach or pass the last index, and the function returns True.

5.)Final Decision:

* If the loop completes without returning True, it means we haven't reached or passed the last index, so the function returns False.

This algorithm effectively checks if it's possible to reach the last index by iteratively updating the maximum reachable index at each step. If at any point, the current index is not reachable, it returns False. If, after iterating through the array, it can reach or pass the last index, it returns True
'''