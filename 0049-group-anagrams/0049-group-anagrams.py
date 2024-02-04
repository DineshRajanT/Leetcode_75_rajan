from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Initialize a defaultdict to store anagrams grouped by their character counts
        res = defaultdict(list)

        # Iterate through each string in the input list
        for s in strs:
            # Create an array to store the counts of each character in the current string
            counts = [0] * 26

            # Count the occurrences of each character in the current string
            for ch in s:
                counts[ord(ch) - ord('a')] += 1

            # Use a tuple of counts as the key to group anagrams
            res[tuple(counts)].append(s)

        # Return the values (groups of anagrams) from the defaultdict
        return res.values()

# Time complexity: O(N * K), where N is the number of strings in the input list and K is the maximum length of a string
# Space complexity: O(N * K), where N is the number of strings in the input list and K is the maximum length of a string
