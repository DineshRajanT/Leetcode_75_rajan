class Solution:
    def findMin(self, nums: List[int]) -> int:
        leftPt = 0
        rightPt = len(nums) - 1
        gloablMin = float("inf")
        
        while leftPt <= rightPt:

            middlePt = (leftPt + rightPt) // 2

            # there has to be a global min or atleast a min number in a given list
            if nums[middlePt] <= gloablMin:
                gloablMin = nums[middlePt]
                

            # first find out where is middlePt at
            if nums[leftPt] <= nums[middlePt]:
                # middlePt is at left part of the array 
                if nums[rightPt] <= nums[leftPt]:
                    leftPt = middlePt + 1
                else:
                    rightPt = middlePt - 1
                
            else:
                # middlePt is at right part of the array 
                if nums[middlePt] <= nums[rightPt]:
                    rightPt = middlePt - 1
                    
                else:
                    leftPt = middlePt + 1
                    
        return gloablMin
        