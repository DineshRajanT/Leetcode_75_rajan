# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Base case: if the subtree is empty, it matches any tree
        if not subRoot:
            return True
        # Base case: if the main tree is empty, there is no match
        if not root: 
            return False

        # Check if the current subtree rooted at 'root' is the same as 'subRoot'
        if self.isSameTree(root, subRoot):
            return True
        
        # Recursively check in the left and right subtrees
        return (self.isSubtree(root.left, subRoot) or
                self.isSubtree(root.right, subRoot))


    def isSameTree(self, p, q) -> bool:
        # Base case: both nodes are None, indicating an empty tree, so they match
        if p is None and q is None:
            return True 
        # Check if nodes are not None and have the same value
        if p and q and p.val == q.val:
            # Recursively check the left and right subtrees
            return (self.isSameTree(p.left, q.left) and
                    self.isSameTree(p.right, q.right))
        # Nodes are either not both None or have different values
        return False
