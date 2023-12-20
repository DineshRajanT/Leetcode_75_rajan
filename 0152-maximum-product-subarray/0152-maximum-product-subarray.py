class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        globalMax = max(nums)
        currMaxProd, currMinProd = 1, 1
        if len(nums)==1:
            return globalMax
        for n in nums:
            if n == 0:
                currMaxProd, currMinProd = 1, 1
            else:
                temp = n * currMaxProd
                currMaxProd = max(n, n * currMaxProd, n * currMinProd )
                currMinProd = min(n, temp , n * currMinProd )
                globalMax = max(globalMax, currMaxProd)

        return globalMax

