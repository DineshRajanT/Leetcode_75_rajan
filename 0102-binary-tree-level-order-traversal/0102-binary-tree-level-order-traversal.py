# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if root is None:
            return 

        ans = []
        queue = []
        queue.append(root)

        while queue:
            currSize = len(queue)
            currLevel = []
            
            for i in range(currSize):
                nodeInThatLevel = queue.pop(0)
                currLevel.append(nodeInThatLevel.val)

                if nodeInThatLevel.left is not None:
                    queue.append(nodeInThatLevel.left)
                if nodeInThatLevel.right is not None:
                    queue.append(nodeInThatLevel.right)

            ans.append(currLevel)

        return ans



# class Solution:
#     def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
#         # Initialize an empty queue, result list, and temporary list for each level
#         que, res, temp_que = [], [], []
        
#         # Check if the root is None, return an empty list in this case
#         if root is None:
#             return res

#         # Enqueue the root and a marker (None) to indicate the end of each level
#         que.append(root)
#         que.append(None)

#         # Process the tree level by level using BFS
#         while que:
#             # Dequeue the front element
#             curr = que.pop(0)

#             # Check if the current element is the marker indicating the end of a level
#             if curr is None:
#                 # Add the values of the current level to the result
#                 res.append(temp_que.copy())
#                 temp_que = []

#                 # If the queue is not empty, enqueue another marker for the next level
#                 if que:
#                     que.append(None)
#                 continue

#             # Add the value of the current node to the temporary list
#             temp_que.append(curr.val)
            
#             # Enqueue the left and right children of the current node if they exist
#             if curr.left is not None:
#                 que.append(curr.left)
                
#             if curr.right is not None:
#                 que.append(curr.right)
        
#         # Return the final result, which contains the level order traversal
#         return res

# # Time Complexity: O(N) - where N is the number of nodes in the binary tree
# #   (Each node is visited once during the traversal)
# # Space Complexity: O(W) - where W is the maximum width (number of nodes in the widest level) of the tree
# #   (In the worst case, the queue can have all nodes in the widest level)



























        
