import sys
from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # Initialize the maximum value to negative infinity
        maxValue = float("-inf")

        def getMaxPathSum(node):
            nonlocal maxValue
            # Base case: if the node is None, return 0
            if not node:
                return 0

            # Recursively calculate the maximum path sum for left and right subtrees
            # Ensure negative values are treated as 0 (max(0, ...))
            leftMax = max(getMaxPathSum(node.left), 0)
            rightMax = max(getMaxPathSum(node.right), 0)

            # Calculate the local maximum considering the current node
            localMax = node.val + leftMax + rightMax

            # Update the overall maximum value
            maxValue = max(maxValue, localMax)

            # Return the maximum path sum considering the current node
            return node.val + max(leftMax, rightMax)

        # Call the recursive function to find the maximum path sum
        getMaxPathSum(root)

        # Return the final maximum path sum
        return maxValue

# Time complexity: O(N), where N is the number of nodes in the binary tree.
# Each node is visited once.

# Space complexity: O(H), where H is the height of the binary tree.
# The maximum depth of the call stack during the recursion is the height of the tree.
