# LC PREMIUM : Alien Dictionary - Topological Sort - Leetcode 269 - Python

from typing import List

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        # Step 1: Create an adjacency list for the characters
        adj = {c: set() for w in words for c in w}

        # Step 2: Build the adjacency list based on character comparisons between consecutive words
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            minLen = min(len(w1), len(w2))
            
            # If a shorter word is a prefix of a longer word, the order is invalid
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            
            # Compare characters and update adjacency list
            for j in range(minLen):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break

        # Step 3: DFS traversal to check for cycles and build the result
        visit = {}  # False: visited, True: current path
        res = []

        def dfs(c):
            if c in visit:
                return visit[c]
            visit[c] = True

            for nei in adj[c]:
                if dfs(nei):
                    return True

            visit[c] = False
            res.append(c)

        # Step 4: Apply DFS to all nodes in the adjacency list
        for c in adj:
            if dfs(c):
                return ""
        
        # Step 5: Reverse the result list and return as a string
        res.reverse()
        return "".join(res)

# Space Complexity:
# The space complexity is O(N), where N is the total number of characters in the input words.

# Time Complexity:
# The time complexity is O(C), where C is the total number of unique characters in the input words.
# This is because each character is visited once during the DFS traversal.





----------------------------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------------------------
# LC PREMIUM : Graph Valid Tree - Leetcode 261 - Python
# Check for loops in the graph 
# check if no.of.nodes == no.of.visited nodes


def validTree(self, n, edges):
    # Check if n is 0 (empty graph), return True as it is considered a valid tree.
    if not n:
        return True
    
    # Create an adjacency list representation of the graph.
    # Initialize an empty list for each node.
    adj = {i: [] for i in range(n)}
    
    # Populate the adjacency list based on the given edges.
    for n1, n2 in edges:
        adj[n1].append(n2)
        adj[n2].append(n1)
    
    # Set to keep track of visited nodes during DFS.
    visit = set()
    
    # Depth-First Search (DFS) function to traverse the graph and check for cycles.
    def dfs(i, prev):
        # If the current node is already visited, there is a cycle, return False.
        if i in visit:
            return False
        
        # Mark the current node as visited.
        visit.add(i)
        
        # Traverse the neighbors of the current node.
        for j in adj[i]:
            # Skip the neighbor that is the parent (prev) of the current node.
            if j == prev:
                continue
            
            # Recursively call DFS for the neighbor.
            if not dfs(j, i):
                return False
        
        # If DFS completes without detecting a cycle, return True.
        return True
    
    # Start DFS from node 0, with a dummy parent (-1) to initiate the traversal.
    # Check if the number of visited nodes equals the total number of nodes (n).
    return dfs(0, -1) and n == len(visit)

# Time Complexity: O(V + E), where V is the number of vertices (nodes) and E is the number of edges in the graph.
# Space Complexity: O(V), for storing the adjacency list and the set of visited nodes.




----------------------------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------------------------
# Number of Connected Components in an Undirected Graph - Union Find - Leetcode 323 - Python
# Union Find : LC 547 (Almost similar problem)

from typing import List

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Initialization: Each node is initially its own parent,
        # and each node has a rank of 1 (used for union-by-rank).
        par = [i for i in range(n)]
        rank = [1] * n

        # Find function: Implements path compression for efficient find operation.
        def find(n1):
            res = n1
            while res != par[res]:
                par[res] = par[par[res]]
                res = par[res]
            return res

        # Union function: Joins two components (sets) and returns 1 if a union occurred, 0 otherwise.
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            
            # If the nodes have the same parent, they are already in the same set.
            if p1 == p2:
                return 0

            # Union-by-rank: Attach the shorter rank tree to the root of the taller rank tree.
            if rank[p2] > rank[p1]:
                par[p1] = p2
                rank[p2] += rank[p1]
            else:
                par[p2] = p1
                rank[p1] += rank[p2]
                
            return 1

        # Initialize the result as the total number of nodes.
        res = n

        # Iterate through the edges and perform unions.
        for n1, n2 in edges:
            res -= union(n1, n2)

        # The final result is the number of connected components.
        return res

# Time Complexity: O(N + E), where N is the number of nodes and E is the number of edges.
# The find operation has an amortized time complexity of O(log N) due to path compression,
# and the union operation has an amortized time complexity of O(1) due to union-by-rank.

# Space Complexity: O(N), where N is the number of nodes.
# The space complexity is dominated by the parent and rank arrays.




----------------------------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------------------------
# Meeting Rooms - Leetcode 252 - Python
# Definition of Interval class

'''

class Interval (object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
'''

class Solution:
    def canAttendMeetings(self, intervals):
        # Sort intervals based on the start time
        intervals.sort(key=lambda i: i.start)
        
        # Iterate through the sorted intervals
        for i in range(1, len(intervals)):
            # Previous interval
            il = intervals[i - 1]
            # Current interval
            i2 = intervals[i]
            
            # Check for overlap between intervals
            if il.end > i2.start:
                # If overlap exists, return False (cannot attend meetings)
                return False
        
        # If no overlap found, return True (can attend meetings)
        return True

# Time Complexity: O(n log n) - Sorting the intervals takes O(n log n) time.
# Space Complexity: O(1) - The algorithm uses constant space as it does not use any additional data structures.




------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Meeting Rooms II - Leetcode 253 - Python

'''

class Interval (object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
'''

class Solution:
    
    def minMeetingRooms(self, intervals):
        # Sorting the start and end times separately
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])
        
        # Initialize variables for result, count of ongoing meetings, and pointers for start and end times
        res, count = 0, 0
        s, e = 0, 0
        
        # Traverse through the sorted start times
        while s < len(intervals):
            # If the current meeting starts before the current ongoing meeting ends, a new room is required
            if start[s] < end[e]:
                s += 1
                count += 1
            # If the current meeting starts after the current ongoing meeting ends, decrease ongoing meetings count
            else:
                e += 1
                count -= 1
            # Update the maximum number of ongoing meetings
            res = max(res, count)
        
        return res


# Time Complexity: O(n log n) - Sorting the intervals takes O(n log n) time.
# Space Complexity: O(n) - The algorithm uses constant space as it does not use any additional data structures.



------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Encode and Decode Strings - Leetcode 271 - Python

def encode(self, strs):
    """
    Encode a list of strings into a single string.

    Time Complexity: O(n), where n is the total number of characters in all strings.
    Space Complexity: O(1), excluding the input and output.

    :param strs: List of strings to be encoded.
    :return: Encoded string.
    """
    res = ""
    for s in strs:
        # Append the length of the string and '#' as a separator
        res += str(len(s)) + '#' + s
    
    return res

def decode(self, s):
    """
    Decode an encoded string back into a list of strings.

    Time Complexity: O(n), where n is the total number of characters in the encoded string.
    Space Complexity: O(m), where m is the number of strings in the encoded string.

    :param s: Encoded string.
    :return: List of decoded strings.
    """
    res, i = [], 0
    while i < len(s):
        j = i
        while s[j] != "#":
            j += 1
        # Extract the length of the current string
        length = int(s[i:j])
        # Append the decoded string to the result list
        res.append(s[j + 1: j + 1 + length])
        i = j + 1 + length

    return res

