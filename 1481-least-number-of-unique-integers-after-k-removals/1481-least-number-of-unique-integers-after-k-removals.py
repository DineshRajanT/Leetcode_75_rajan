from typing import List

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        # Step 1: Count the occurrences of each element in the array
        counts = {}
        for ele in arr:
            counts[ele] = counts.get(ele, 0) + 1

        # Step 2: Sort the counts dictionary based on the frequency of each element
        sorted_counts = dict(sorted(counts.items(), key=lambda item: item[1]))

        # Step 3: Iterate through the sorted_counts to determine the least number of unique integers
        for key, val in list(sorted_counts.items()):
            if val > k:
                # If the count is greater than k, reduce the count by k
                sorted_counts[key] = val - k
                k = 0
            else:
                # If the count is less than or equal to k, set the count to 0 and reduce k accordingly
                k -= val
                sorted_counts[key] = 0
        print(sorted_counts)
        # Step 4: Count the number of unique integers with non-zero counts
        res = [K for K, V in sorted_counts.items() if V != 0]

        # Step 5: Return the length of the result, which represents the least number of unique integers
        return len(res)


