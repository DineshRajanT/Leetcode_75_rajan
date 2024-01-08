class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # T : O(m * n)
        # S : O(1)
        left, right = 0 , len(matrix[0])
        top, bottom = 0, len(matrix)

        res = []
        # Iterate until all elements are visited
        while (left < right) and (top < bottom):
            # left to right
            # top to down
            # right ot left
            # bottom to top

            # Traverse from left to right in the current row
            for i in range(left, right):
                res.append(matrix[top][i])
            top += 1

            # Traverse from top to bottom in the current column
            for i in range(top, bottom):
                res.append(matrix[i][right - 1])
            right -= 1

            # Check if further traversal is needed
            if not (left < right and top < bottom):
                break

            # Traverse from right to left in the current row
            for i in range(right - 1, left - 1, -1):
                res.append(matrix[bottom - 1][i])
            bottom -= 1

            # Traverse from bottom to top in the current column
            for i in range(bottom - 1, top - 1, -1):
                res.append(matrix[i][left])
            left += 1

        return res



            

        