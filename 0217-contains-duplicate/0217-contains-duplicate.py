class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numSet = set()
        
        for n in nums:
            if n not in numSet:
                numSet.add(n)
            elif n in nums:
                return True
        return False
        