from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Count the occurrences of each number in the input array
        counts = {}
        for n in nums:
            counts[n] = counts.get(n, 0) + 1

        # Step 2: Create a frequency array where each index stores numbers with the same frequency
        freq = [[] for _ in range(len(nums) + 1)]

        # Step 3: Populate the frequency array based on the counts
        for num, count in counts.items():
            freq[count].append(num)

        # Step 4: Iterate over the frequency array in reverse order to get the top k frequent elements
        res = []
        for i in range(len(nums), 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res

# Time Complexity:O(N)
# Space Complexity: O(N)

# Using Heap we can finish in O(nlogk) , add everything to heap and pop k times. 
