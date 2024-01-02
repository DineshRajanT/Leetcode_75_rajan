class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        
        lastSeen = {}
        counts = {}
        globalMax = currMax = 0
        
        if len(set(nums)) == len(nums):
            return [nums]

        for ele in nums:
            counts[ele] = counts.get(ele,0) + 1
            currMax = counts[ele]
            globalMax = max(currMax, globalMax)
            
        print(globalMax) # get the maximum number of duplicates to allocate the size of the output matrix
        matrix = [[] * len(nums) for _ in range(globalMax)]

        for ele in nums:
            if ele not in lastSeen:
                lastSeen[ele] = 0
                matrix[lastSeen[ele]].append(ele)
            else:
                matrix[lastSeen[ele]+1].append(ele)
                lastSeen[ele] += 1

        return matrix
             