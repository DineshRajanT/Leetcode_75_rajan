from collections import defaultdict

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # Initialize dictionaries to keep track of in-degrees and out-degrees
        in_degree = defaultdict(int)
        out_degree = defaultdict(int)

        # Iterate through the trust list to update degrees
        for t in trust:
            a, b = t[0], t[1]
            out_degree[a] += 1  # Increase out-degree for person 'a'
            in_degree[b] += 1   # Increase in-degree for person 'b'

        # Print in-degrees and out-degrees for debugging
        print("In-degrees:", in_degree)
        print("Out-degrees:", out_degree)

        # Check for the potential judge based on in-degrees and out-degrees
        for i in range(1, n + 1):
            if in_degree[i] == n - 1 and out_degree[i] == 0:
                return i  # Found the judge

        return -1  # No judge found

# Time Complexity: O(E + V), where E is the number of trust relationships and V is the number of people
# Space Complexity: O(V), where V is the number of people
