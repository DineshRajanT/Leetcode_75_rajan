from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Initialize pointers, starting position, and minimum length
        i = 0
        j = 0
        minStart = 0
        minLength = float("inf")
        n = len(s)

        # Create a defaultdict to store the frequency of characters in string t
        t_mapFreq = defaultdict(int)
        for char in t:
            t_mapFreq[char] += 1

        # Initialize a count to keep track of the remaining characters to find
        count = len(t)

        # Sliding window approach
        while j < n:
            # Update count and t_mapFreq for the current character at position j
            if t_mapFreq[s[j]] > 0:
                count -= 1
            t_mapFreq[s[j]] -= 1
            j += 1

            # Check if all characters are found, and update the minimum length
            while count == 0:
                if j - i < minLength:
                    minStart = i
                    minLength = j - i

                # Move the window by updating t_mapFreq and count for the character at position i
                t_mapFreq[s[i]] += 1
                if t_mapFreq[s[i]] > 0:
                    count += 1

                i += 1

        # Return the minimum window substring
        return s[minStart: minStart + minLength] if minLength != float("inf") else ""

# Time complexity: O(n + m), where n is the length of the input string s, where m is the length of the input string t 
# Space complexity: O(26) = O(1) for the t_mapFreq defaultdict
