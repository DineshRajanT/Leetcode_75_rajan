class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # we can run a single loop to locate the target but that is not needed here,
        # we need something in O(log N)
        
        leftPt = 0
        rightPt = len(nums) - 1

        while leftPt <= rightPt:

            middlePt = (leftPt + rightPt) // 2

            if nums[middlePt] == target:
                return middlePt

            # first find out where is middlePt at
            if nums[leftPt] <= nums[middlePt]:
                # middlePt is at left part of the array 
                if target < nums[middlePt] and target >= nums[leftPt]:
                    rightPt = middlePt - 1
                else:
                    leftPt = middlePt + 1

            else:
                # middlePt is at right part of the array 
                if target > nums[middlePt] and target <= nums[rightPt]:
                    leftPt = middlePt + 1
                else:
                    rightPt = middlePt - 1
        return -1








        