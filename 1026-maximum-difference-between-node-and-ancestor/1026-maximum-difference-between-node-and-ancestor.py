# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        # Base case: If the root is None, return 0 as there is no ancestor to compare.
        if root is None:
            return 0
        
        # Initialize the recursive function with the root node and its initial max and min values.
        return self.maxDiff(root, root.val, root.val)

    def maxDiff(self, node, maxValue, minValue) -> int:
        # Base case: If the current node is None, return the difference between max and min values.
        if node is None:
            return maxValue - minValue

        # Update the maxValue and minValue based on the current node's value.
        maxValue = max(maxValue, node.val)
        minValue = min(minValue, node.val)

        # Recursively calculate the max differences for the left and right subtrees.
        leftMax = self.maxDiff(node.left, maxValue, minValue)
        rightMax = self.maxDiff(node.right, maxValue, minValue)

        # Return the maximum of the differences calculated for the left and right subtrees.
        return max(leftMax, rightMax)

# Time Complexity: O(N), where N is the number of nodes in the binary tree.
# Each node is visited once in the recursive solution.
# Space Complexity: O(H), where H is the height of the binary tree.
# The space complexity is determined by the maximum depth of the recursive call stack.
