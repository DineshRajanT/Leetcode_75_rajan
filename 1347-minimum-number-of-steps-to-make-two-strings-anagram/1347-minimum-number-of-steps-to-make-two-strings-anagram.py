class Solution:
    def minSteps(self, s: str, t: str) -> int:
        # Initialize a variable to store the total count of steps needed to make the two strings anagrams
        totalCount = 0
        
        # Create dictionaries to store the frequency of each character in strings s and t
        freq_s = {}
        freq_t = {}

        # Populate the frequency dictionary for string s
        for char in s:
            freq_s[char] = freq_s.get(char, 0) + 1

        # Populate the frequency dictionary for string t
        for char in t:
            freq_t[char] = freq_t.get(char, 0) + 1

        # Iterate over each character and its frequency in string t
        for char, freq_val in freq_t.items():
            # Check if the character is present in the frequency dictionary of string s
            if char in freq_s:
                # Calculate the difference in frequency between the two strings for the current character
                diff = freq_t[char] - freq_s[char]
            else:
                # If the character is not present in string s, consider all occurrences in string t
                diff = freq_t[char]

            # Accumulate the maximum difference (or 0 if there's no difference) in the total count
            totalCount += max(diff, 0)

        # Return the total count of steps needed to make the two strings anagrams
        return totalCount
