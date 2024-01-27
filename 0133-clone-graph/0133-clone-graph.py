from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: Optional[Node]) -> Optional[Node]:
        # Check if the input node is None
        if not node:
            return None

        # Dictionary to store the mapping of original nodes to their corresponding clones
        copies = dict()
        # Queue for BFS traversal
        queue = []

        # Create the first node of the cloned graph from the input node
        curr = Node(node.val, None)
        # Add the mapping of the original node to its clone in the dictionary
        copies[node] = curr  # {OLD NODE: NEW NODE}
        # Add the original node to the queue for BFS traversal
        queue.append(node)

        # BFS traversal to clone the graph
        while queue:
            # Pop the current node from the queue
            curr_node = queue.pop(0)

            # Iterate through the neighbors of the current node
            for neighbor_node in curr_node.neighbors:
                # If the neighbor has not been visited (not in the copies dictionary)
                if neighbor_node not in copies:
                    # Create a new node for the neighbor and add it to the mapping
                    new_node = Node(neighbor_node.val, None)
                    copies[neighbor_node] = new_node
                    # Add the neighbor to the queue for further traversal
                    queue.append(neighbor_node)

                # Add the clone of the neighbor to the neighbors of the cloned current node
                copies[curr_node].neighbors.append(copies[neighbor_node])

        # Return the clone of the graph starting from the original node
        return copies[node]

# Time complexity analysis:
# The time complexity is O(V + E), where V is the number of nodes (vertices) and E is the number of edges.
# This is because each node and each edge is processed once during the BFS traversal.

# Space complexity analysis:
# The space complexity is also O(V + E), where V is the number of nodes (vertices) and E is the number of edges.
# This is due to the space used by the copies dictionary and the queue during BFS traversal.
