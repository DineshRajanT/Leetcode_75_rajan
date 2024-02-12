from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Boyer-Moore Voting algorithm for finding majority element

        # Initialize count and majorityElement variables
        count = 0
        majorityElement = -1

        # Iterate through the list of numbers
        for ele in nums:
            # If count becomes zero, update majorityElement to the current element
            if count == 0:
                majorityElement = ele

            # If the current element is equal to the majorityElement, increment count
            if ele == majorityElement:
                count += 1
            # If the current element is different from majorityElement, decrement count
            elif ele != majorityElement:
                count -= 1

        # The majorityElement variable should now contain the majority element
        return majorityElement

# Time complexity: O(n) - The algorithm iterates through the list once.
# Space complexity: O(1) - The algorithm uses only a constant amount of extra space.

# FOR OTHER PROBLEMS : 
# check of the condition
# do a for loop , check the freq of the majorityElement in nums and confirm it is more than n/2,
# majorityElement might be a candidate not the final answer itself.