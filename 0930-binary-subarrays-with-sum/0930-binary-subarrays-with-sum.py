class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        # Initialize a dictionary to keep track of cumulative sums encountered
        # Key: cumulative sum, Value: count of occurrences
        count = {0: 1}  # Start with 0, since if the sum equals the goal immediately, we have one subarray
        curr_sum = 0  # Initialize current sum to 0
        total_subarrays = 0  # Initialize the count of subarrays with the desired sum

        # Iterate through each element in the nums list
        for num in nums:
            # Update the current sum by adding the current element
            curr_sum += num
            
            # Check if there exists a subarray ending at the current index
            # whose sum equals the goal
            if curr_sum - goal in count:
                # If such a subarray exists, update the count of total_subarrays
                total_subarrays += count[curr_sum - goal]
                
            # Update the count of the current sum in the dictionary
            count[curr_sum] = count.get(curr_sum, 0) + 1

        # Return the total count of subarrays with the desired sum
        return total_subarrays
