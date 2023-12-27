class Solution:
    # T : O(n)
    # T : O(n)  because of set
    def lengthOfLongestSubstring(self, s: str) -> int:
        globalMax = 0  # Overall maximum length of substring without repeating characters

        i = 0  # Starting index of current substring
        j = 0  # Ending index of current substring

        char_set = set()  # Set to keep track of unique characters in the current substring

        # Loop through the string
        while j < len(s):
            # If the current character is not in the set, add it and update the maximum length
            if s[j] not in char_set:
                char_set.add(s[j])
                currMax = j - i + 1  # Length of the current substring without repeating characters
                globalMax = max(globalMax, currMax)  # Update overall maximum length
                j += 1  # Move to the next character in the substring
            else:
                # If the current character is already in the set, remove the character at index i
                char_set.remove(s[i])
                i += 1  # Move to the next unique character in the substring

        return globalMax  # Return the overall maximum length of substring without repeating characters


        #rajan: keep on adding the character in the right untill you encounter a duplicate character in the existing set, note that that duplicate char may be present in any part of the left substring, our task is to do a sliding window approach so as to see every possible substrings....so keep poping and incrementing i by 1 if you encounter a duplicate char.
