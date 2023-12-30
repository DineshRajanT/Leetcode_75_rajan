from typing import List

class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        # Check if there is only one word in the list
        if len(words) == 1:
            return True
        
        # Dictionary to store character counts
        counts = {}
        
        # Count the occurrences of each character in all words
        for i in range(len(words)):
            for char in words[i]:
                counts[char] = counts.get(char, 0) + 1
        # Check if each character count is a multiple of the total number of words
        for v in counts.values():
            if v % len(words) != 0:
                # If any character count is not divisible, return False
                return False

        # If all character counts are divisible, return True
        return True
