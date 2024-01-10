from collections import deque
from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        # Dictionary to store the adjacency list representation of the tree
        adjacencyList = {}
        # Convert the binary tree to an undirected graph
        self.convertTreeToGraph(root, -1, adjacencyList)

        # Queue for BFS traversal
        q = deque([start])
        # Set to keep track of visited nodes
        visited = set([start])
        # Variable to store the time required to infect the entire tree
        mins = 0

        # Perform BFS traversal
        while q:
            # Size of the current level in BFS
            sizeofLevel = len(q)

            # Process each node in the current level
            for _ in range(sizeofLevel):
                node = q.popleft()

                # Check neighbors and infect uninfected nodes
                for neighbour in adjacencyList[node]:
                    if neighbour not in visited:
                        visited.add(neighbour)
                        q.append(neighbour)

            # If there are nodes in the next level, increment the time counter
            if q:
                mins += 1

        return mins

    def convertTreeToGraph(self, node, parent, adjacencyList):
        # Helper function to convert binary tree to undirected graph
        if node is not None:
            # If the node value is not in the adjacency list, add it
            if node.val not in adjacencyList:
                adjacencyList[node.val] = []

            # Add edges between the current node and its parent
            if parent != -1:
                adjacencyList[node.val].append(parent)
                adjacencyList[parent].append(node.val)

            # Recursively convert left and right subtrees to graph
            self.convertTreeToGraph(node.left, node.val, adjacencyList)
            self.convertTreeToGraph(node.right, node.val, adjacencyList)

# Time Complexity:
# The convertTreeToGraph function takes O(n) time, where n is the number of nodes in the tree.
# The BFS traversal takes O(n + m) time, where m is the number of edges in the graph.
# Therefore, the overall time complexity is O(n + m).

# Space Complexity:
# The space complexity is O(n + m), where n is the number of nodes and m is the number of edges in the graph.
# This includes the space required for the adjacency list, queue, and visited set.
