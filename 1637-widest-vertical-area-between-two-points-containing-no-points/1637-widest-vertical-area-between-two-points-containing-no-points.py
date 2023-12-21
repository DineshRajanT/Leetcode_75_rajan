class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        maxArea = 0
        x_coordinate=[]
        for point in points:
            x,y = point
            x_coordinate.append(x)
        x_coordinate.sort()
        
        for i in range(len(x_coordinate)-1):
            if abs(x_coordinate[i] - x_coordinate[i+1]) > maxArea:
                maxArea = abs(x_coordinate[i] - x_coordinate[i+1])
                
        return maxArea
            
        