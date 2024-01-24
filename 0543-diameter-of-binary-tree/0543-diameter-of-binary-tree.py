# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Global variable to store the maximum diameter
        globalHeight = 0
        
        def getHeight(node):
            # It is particularly useful when dealing with nested functions. 
            # If a variable is not found in the local scope, Python will look 
            # for it in the nearest enclosing scope. The nonlocal keyword explicitly
            # tells Python to look for the variable in the nearest enclosing scope and modify it there. 
            nonlocal globalHeight 

            # Base case: If the node is None, return 0 (height of an empty subtree)
            if node is None:
                return 0
            else:
                # Recursive calls to get the heights of left and right subtrees
                lh = getHeight(node.left) 
                rh = getHeight(node.right)
                
                # Update globalHeight with the maximum diameter seen so far
                globalHeight = max(globalHeight, lh + rh)
                
                # Return the height of the current node
                return 1 + max(lh, rh)
            
        # Start the recursive process with the root of the tree
        getHeight(root)
        
        # The globalHeight now contains the diameter of the binary tree
        return globalHeight

# Time Complexity: O(N), where N is the number of nodes in the binary tree.
#   Each node is visited once, and constant time operations are performed at each node.
# Space Complexity: O(H), where H is the height of the binary tree.
#   The maximum depth of the call stack during recursion is equal to the height of the tree.
