# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # down engayo oru node imabalance ah irundhale we return, start from the bottom and compute the if each node is balanced or not
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        # Helper function to check if a node and its subtrees are balanced
        def isNodeBalanced(node):
            # Base case: If the node is None, it is balanced with height 0
            if node is None:
                return 0
            
            # Recursively check the height of the left subtree
            lh = isNodeBalanced(node.left)
            
            # If the left subtree is not balanced, propagate the unbalanced state up
            if lh == -1:
                return -1
            
            # Recursively check the height of the right subtree
            rh = isNodeBalanced(node.right)
            
            # If the right subtree is not balanced, propagate the unbalanced state up
            if rh == -1:
                return -1
            
            # Check if the current node is balanced by comparing the heights of left and right subtrees
            if abs(lh - rh) > 1:
                return -1
            
            # Return the height of the current subtree (maximum of left and right subtrees) plus 1
            return max(lh, rh) + 1
        
        # Start checking the balance from the root, if the root is unbalanced, the entire tree is unbalanced
        if isNodeBalanced(root) == -1:
            return False
        return True

# Time Complexity: O(N) - where N is the number of nodes in the binary tree
#   (Each node is visited once during the traversal)
# Space Complexity: O(H) - where H is the height of the binary tree
#   (The maximum depth of the recursive call stack, which is equal to the height of the tree)