# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        # Helper function to recursively validate a node and its descendants
        def validateNode(root, minVal, maxVal):

            # Base case: If the node is None, it is valid
            if root is None:
                return True

            # Check if the node's value violates the current range [minVal, maxVal]
            if root.val <= minVal or root.val >= maxVal:
                return False    

            # Recursively check the left and right subtrees with updated ranges
            # Left subtree values should be in the range [minVal, root.val]
            # Right subtree values should be in the range [root.val, maxVal]
            return (validateNode(root.left, minVal, root.val) and 
                    validateNode(root.right, root.val, maxVal))

        # Initial ranges for the entire tree
        minVal = float("-inf")
        maxVal = float("inf")

        # Start the validation from the root of the tree
        return validateNode(root, minVal, maxVal)
