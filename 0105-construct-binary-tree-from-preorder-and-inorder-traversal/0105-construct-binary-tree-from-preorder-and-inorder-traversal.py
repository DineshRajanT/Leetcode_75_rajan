# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        # Initialize variables
        preOrderIdx = 0  # Keep track of the current index in the preorder list
        mapInOrder = {}  # A map to store the index of each value in the inorder list

        # Populate the map for quick lookup of indices in the inorder list
        for i in range(len(inorder)):
            mapInOrder[inorder[i]] = i
        
        # Recursive function to construct the binary tree
        def constructTree(preorder, inorder, inorderSt, inorderEnd):

            nonlocal preOrderIdx  # Access the variable from the outer function
            nonlocal mapInOrder  # Access the variable from the outer function

            # Base case: If the start index is greater than the end index, return None
            if inorderSt > inorderEnd:
                return None

            # Create a new TreeNode with the current value from preorder
            root = TreeNode(preorder[preOrderIdx])
            preOrderIdx += 1  # Move to the next index in preorder

            # If the start index is equal to the end index, it is a leaf node, return the root
            if inorderSt == inorderEnd:
                return root

            # Find the index of the current root value in the inorder list
            i = mapInOrder[root.val]

            # Recursively construct the left and right subtrees
            root.left = constructTree(preorder, inorder, inorderSt, i - 1)
            root.right = constructTree(preorder, inorder, i + 1, inorderEnd)

            # Return the root of the current subtree
            return root

        # Start the construction of the tree from the entire range of inorder list
        return constructTree(preorder, inorder, 0, len(inorder) - 1)
