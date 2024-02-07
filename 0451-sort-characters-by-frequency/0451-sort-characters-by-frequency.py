class Solution:
    def frequencySort(self, s: str) -> str:
        # Create a dictionary to store the frequency of each character in the input string
        freq = {}
        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1

        # Sort the dictionary items by frequency in descending order
        sorted_freq = dict(sorted(freq.items(), key=lambda x: x[1], reverse=True))

        # Construct the output string by repeating each character based on its frequency
        outStr = ""
        for k, v in sorted_freq.items():
            outStr += k * v

        # Return the final sorted string
        return outStr

# Time complexity: O(N log N), where N is the length of the input string s
#   - Sorting the dictionary items takes O(N log N) time
# Space complexity: O(N), where N is the length of the input string s
#   - The space required to store the frequency dictionary
#   - The space required for the sorted_freq dictionary
#   - The space required for the output string outStr
