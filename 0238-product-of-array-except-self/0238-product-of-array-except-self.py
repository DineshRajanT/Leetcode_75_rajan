class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        resArr = [1] * len(nums)
        prefix, postfix = 1, 1

        for i in range(len(nums)):
            resArr[i] = prefix
            prefix = prefix * nums[i]

        for i in range(len(nums)-1, -1,-1):
            resArr[i] = resArr[i] * postfix
            postfix = postfix * nums[i]
        print(resArr)
        print("")
        return resArr
        