class Solution:
    def firstUniqChar(self, s: str) -> int:
        charFreq = {}

        # Count the frequency of each character
        for char in s:
            charFreq[char] = charFreq.get(char, 0) + 1

        # Find the index of the first unique character
        for i, char in enumerate(s):
            if charFreq[char] == 1:
                return i

        return -1  # If no unique character is found

