# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Base case: if the root is None, return None (no common ancestor)
        if root is None:
            return None

        # Check if the current root is either p or q
        if root.val == p.val or root.val == q.val:
            return root

        # Recursively search for p and q in the left and right subtrees
        presentInLeftSubTree = self.lowestCommonAncestor(root.left, p, q)
        presentInRightSubTree = self.lowestCommonAncestor(root.right, p, q)

        # If both p and q are present in different subtrees, the current root is the common ancestor
        if presentInLeftSubTree and presentInRightSubTree:
            return root

        # Return the non-None result (either p or q) if found, otherwise return None
        return presentInLeftSubTree if presentInLeftSubTree is not None else presentInRightSubTree

# Time complexity: O(N), where N is the number of nodes in the binary tree
# Space complexity: O(H), where H is the height of the binary tree (due to recursive call stack)
