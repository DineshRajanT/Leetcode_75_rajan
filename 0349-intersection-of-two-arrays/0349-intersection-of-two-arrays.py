class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        # print(set(nums1) & set(nums2)) # common elements
        # print(set(nums1) | set(nums2)) # union elements

        return list(set(nums1) & set(nums2))

        