from typing import List

class Solution:
    def maxLength(self, arr: List[str]) -> int:
        # Start the recursive process with an empty result string and index 0
        resultStrLen = self.buildMaxString(arr, 0, "")
        return resultStrLen

    def buildMaxString(self, arr, i, resultStr):
        # Check if the current result string has unique characters
        if len(resultStr) != len(set(resultStr)):
            return 0  # If duplicates found, return 0, as this path is invalid

        # Base case: If reached the end of the array, return the length of the result string
        if i == len(arr):
            return len(resultStr)

        currStrLen = len(resultStr)  # Current length of the result string

        # Take the current string and recursively explore with the next element
        currStrLen = max(currStrLen, self.buildMaxString(arr, i + 1, resultStr + arr[i]))
        
        # Do not take the current string and recursively explore with the next element
        currStrLen = max(currStrLen, self.buildMaxString(arr, i + 1, resultStr))

        return currStrLen  # Return the maximum length encountered during exploration
