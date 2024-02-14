class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positives = []
        negatives = []
        res = []

        for ele in nums:
            if ele > 0:
                positives.append(ele)
            else:
                negatives.append(ele)
            
        for i in range(len(nums)//2):
            res.append(positives[i])
            res.append(negatives[i])

        return res

        