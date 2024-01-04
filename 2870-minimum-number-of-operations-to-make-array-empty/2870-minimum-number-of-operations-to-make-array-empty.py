class Solution:
    def minOperations(self, nums: List[int]) -> int:
        # T : O(N)
        # S : O(N)
        numFreq = {}  # Dictionary to store the frequency of each element
        res = 0  # Variable to store the result (minimum operations)

        # Count the frequency of each element in the input array
        for ele in nums:
            numFreq[ele] = numFreq.get(ele, 0) + 1

        # Iterate through the frequency dictionary
        for k, v in numFreq.items():
            if v % 3 == 0:
                # If frequency is divisible by 3, add the required operations
                res += v // 3

            elif v % 3 == 1 and numFreq.get(k, 0) >= 2:
                # If frequency leaves a remainder of 1 when divided by 3,
                # and there are at least 2 elements with the next higher value,
                # add the required operations
                res += (v + 2) // 3

            elif v % 3 == 2 and numFreq.get(k, 0) >= 1:
                # If frequency leaves a remainder of 2 when divided by 3,
                # and there is at least 1 element with the next higher value,
                # add the required operations
                res += (v + 1) // 3
                
            else:
                # If none of the conditions are met, it's not possible to make the array empty
                return -1

        return res