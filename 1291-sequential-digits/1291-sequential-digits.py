from typing import List

class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        res = []

        def build(currNum, low, high):
            # Check if the current number is within the desired range
            if low <= currNum <= high:
                res.append(currNum)

            # Extract the last digit of the current number
            last_digit = currNum % 10

            # If the last digit is less than 9, generate the next sequential number
            if last_digit < 9:
                nextNum = currNum * 10 + (last_digit + 1)
                build(nextNum, low, high)

        # Iterate through possible starting digits (1 to 9)
        for i in range(1, 10):
            # Start building sequences from the current starting digit
            build(i, low, high)

        # Sort the result before returning
        return sorted(res)
