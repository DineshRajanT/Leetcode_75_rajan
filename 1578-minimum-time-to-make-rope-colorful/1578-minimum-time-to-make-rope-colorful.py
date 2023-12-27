class Solution:
    # T : O(n)
    # S: O(1)
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        totalTime = 0
        left = 0
        right = 1
        
        while right < len(colors):
            if colors[left] == colors[right]:
                # if both color of ballons matches, then check the minimum neededtime between them,
                # and add the min to totalTime and keep moving...
                if neededTime[left] < neededTime[right]:
                    totalTime += neededTime[left] 
                    left = right
                    right+=1
                else:
                    # else add the right since it is the minimum and keep moving right
                    totalTime += neededTime[right]
                    right+=1
            else:
                # if both the colors don't match keep incrementing...
                left = right
                right+=1
        return totalTime



# class Solution:
#     def minCost(self, colors: str, neededTime: List[int]) -> int:
#         answer = 0 
        
#         n = len ( colors )
        
#         index1 = 0
#         index2 = 1
        
#         while ( index2 < n ) :
#             if ( colors [ index1 ] == colors [ index2 ] ) :
#                 if neededTime [ index1 ] <= neededTime [ index2 ] :
#                     answer += neededTime [ index1 ]
#                     index1 = index2
#                     index2 += 1
#                 else :
#                     answer += neededTime [ index2 ]
#                     index2 += 1
                
#             else :
#                 index1 = index2
#                 index2 += 1 
                                    
#         return answer