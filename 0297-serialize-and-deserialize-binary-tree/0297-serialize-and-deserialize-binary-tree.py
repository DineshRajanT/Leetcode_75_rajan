# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def preOrder(node, ans):
            # Base case: If the node is None, append '#' to represent None
            if node is None:
                ans.append("#")
                return
            # Append the value of the current node to the result
            ans.append(str(node.val))
            # Recursive call for the left and right subtrees
            preOrder(node.left, ans)
            preOrder(node.right, ans)

        ans = []
        preOrder(root, ans)
        ansAsStr = ",".join(ans)  # Combine the result list into a string
        return ansAsStr


    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def deserializeAsArray(ListOfNodes, index):
            # Base case: If reached the end of the list, return None and the current index
            if index == len(ListOfNodes):
                return None, index

            val = ListOfNodes[index]
            index += 1

            # If the value is '#', it represents None, return None and the updated index
            if val == "#":
                return None, index

            # Create a TreeNode with the current value
            root = TreeNode(int(val))
            # Recursive call for the left and right subtrees
            root.left, index = deserializeAsArray(ListOfNodes, index)
            root.right, index = deserializeAsArray(ListOfNodes, index)
            return root, index

        if not data:
            return None

        ListOfNodes = data.split(",")
        root, _ = deserializeAsArray(ListOfNodes, 0)
        return root

# Time Complexity:
#   - Serialization: O(n), where n is the number of nodes in the binary tree. The function traverses each node once.
#   - Deserialization: O(n), where n is the length of the input string. The function processes each character in the string once.

# Space Complexity:
#   - Serialization: O(n), where n is the number of nodes in the binary tree. The space is used for the result list.
#   - Deserialization: O(n), where n is the length of the input string. The space is used for the list of nodes during the deserialization process.
