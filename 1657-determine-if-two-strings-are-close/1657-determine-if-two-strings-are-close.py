class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # Time Complexity: O(m + n), where m and n are the lengths of word1 and word2
        # Space Complexity: O(max(m, n)), where m and n are the lengths of word1 and word2

        # Initialize dictionaries to store character frequencies for each word
        freq_word1 = {}
        freq_word2 = {}

        # Populate the frequency dictionary for string word1
        for char in word1:
            freq_word1[char] = freq_word1.get(char, 0) + 1

        # Populate the frequency dictionary for string word2
        for char in word2:
            freq_word2[char] = freq_word2.get(char, 0) + 1

        # Check if the sets of characters are the same
        if set(freq_word1.keys()) != set(freq_word2.keys()):
            # If the sets of characters are different, the words cannot be close
            return False

        # Check if the sets of frequencies are the same after sorting
        # Sorting is done to compare the frequencies in a consistent order
        # Time Complexity: O(max(m, n) * log(max(m, n))), where m and n are the lengths of word1 and word2
        return sorted(freq_word1.values()) == sorted(freq_word2.values())

