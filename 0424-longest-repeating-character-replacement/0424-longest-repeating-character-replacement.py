class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Dictionary to store the count of characters in the current window
        counts = {}
        # Variable to store the result (length of the longest substring with repeating characters)
        res = 0
        # Left pointer of the sliding window
        l = 0
        # Maximum frequency of any character in the current window
        maxFreq = 0

        # Iterate through the string using a sliding window
        for r in range(len(s)):
            # Update the count of the current character in the window
            counts[s[r]] = counts.get(s[r], 0) + 1
            # Update the maximum frequency of any character in the current window
            maxFreq = max(maxFreq, counts[s[r]])

            # Check if the number of characters to be replaced (window size - maxFreq) exceeds k
            while (r - l + 1) - maxFreq > k:
                # Move the left pointer to shrink the window
                counts[s[l]] -= 1
                l += 1

            # Update the result with the length of the current valid substring
            res = max(res, (r - l + 1))

        # Return the final result
        return res
