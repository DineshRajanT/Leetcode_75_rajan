# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        # Check if the root is None, return None in this case
        if not root:
            return None

        # Initialize leftVal to None
        leftVal = None

        # Create a queue to perform level order traversal
        queue = [root]

        # Loop until the queue is empty
        while queue:
            # Get the number of nodes at the current level
            size = len(queue)

            # Iterate through nodes at the current level
            for i in range(size):
                # Pop the front node from the queue
                node = queue.pop(0)

                # If it's the first node in the current level, update leftVal
                if i == 0:
                    leftVal = node.val

                # Add left and right children to the queue if they exist
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        # Return the leftmost value at the bottom level of the binary tree
        return leftVal
