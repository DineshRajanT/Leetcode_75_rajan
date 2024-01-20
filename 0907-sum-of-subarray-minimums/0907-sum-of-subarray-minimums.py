from typing import List

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        modulo = 10**9 + 7
        stack = []
        ans = 0

        # Iterate through each element in the array
        for i, num in enumerate(arr):
            # For each element, pop elements from the stack until the top is less than the current element
            # print("NUMS:", num)
            while stack and arr[stack[-1]] > num:
                # print(f"Inside : {i} ", stack, stack[-1],arr[stack[-1]] )
                j = stack.pop()
                k = stack[-1] if stack else -1
                # Calculate the contribution of the popped element to the final sum
                ans += arr[j] * (i - j) * (j - k)

            stack.append(i)  # Push the current element index onto the stack
        # print("STACK : ", stack)
        # Process any remaining elements in the stack
        while stack:
            j = stack.pop()
            k = stack[-1] if stack else -1
            ans += arr[j] * (len(arr) - j) * (j - k)

        return ans % modulo

