# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def pseudoPalindromicPaths(self, root: Optional[TreeNode]) -> int:
        # Initialize count to keep track of pseudo-palindromic paths
        count = 0

        # Define a recursive helper function to explore the tree and count paths
        def solve(node, path):
            nonlocal count
            
            # If the current node is not None
            if node is not None:
                # Toggle the bit at the position corresponding to the node's value in the path
                # 1 is already there again we add 1 it becomes 0 eventually avoid storing even counts
                # 0 is already there we add 1 to it it becomes 1 eventually counting only odd counts
                path = (path ^ 1 << node.val)

                # If the current node is a leaf node (no children)
                if node.left is None and node.right is None:
                    # Check if the path is a pseudo-palindrome (at most one odd count allowed)
                    if (path & (path - 1)) == 0:
                        count += 1

                # Recursively explore the left and right subtrees
                solve(node.left, path)
                solve(node.right, path)

        # Start the recursive exploration from the root with an initial path of 0
        solve(root, 0)

        # Return the final count of pseudo-palindromic paths
        return count
