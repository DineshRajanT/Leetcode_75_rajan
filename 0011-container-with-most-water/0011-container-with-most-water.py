class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Initialize two pointers, l, r
        # find the area between them and update max respectively
        # move the pointer in such a way that the area must be maiximized,
        # so move the pointer(i.e) index with min height.
        
        left = 0
        right = len(height) - 1
        resArea = 0

        while left < right:
            length = min(height[left], height[right])
            breadth = right - left
            currArea = length * breadth
            resArea = max(currArea, resArea)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1 

        return resArea

        
        