class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        # Check if all characters are unique, in which case there are no equal characters
        if len(set(s)) == len(s):
            return -1  # Return -1 for the case where there are no equal characters

        # Dictionary to store the last index of each character
        char_index = {}

        # Variable to store the global maximum distance between equal characters
        globalMax = 0

        # Iterate through each character and its index in the string
        for i, char in enumerate(s):
            if char in char_index:
                # Calculate the distance between equal characters
                currMax = i - char_index[char] - 1
                # Update the global maximum distance
                globalMax = max(globalMax, currMax)
            else:
                # If the character is not in the dictionary, store its index
                char_index[char] = i

        # Return the maximum distance between equal characters
        return globalMax




        



        # if len(set(s)) == 1:
        #     return 0
        # currMax = globalMax = 0
        # for i in range(len(s)):
        #     for j in range(i+1, len(s)):
        #         if s[i] == s[j]:
        #             currMax = len(s[i+1:j])
        #             globalMax = max(globalMax, currMax)
        # return globalMax if globalMax else -1
        