class Solution:

    # Solution 2:
    # T : O(nlogn)
    # S : O(n)
    # Actually you have a better solution O(nlogn) using binary search
    def lengthOfLIS(self, nums: List[int]) -> int:
        ans_arr = []
        ans_arr.append(nums[0])

        for i in range(1, len(nums)):
            if nums[i] > ans_arr[-1]:
                # If the current number is greater
                # than the last element of the answer
                # list, it means we have found a
                # longer increasing subsequence.
                # Hence, we append the current number
                # to the answer list.
                ans_arr.append(nums[i])
            else:
                # If the current number is not
                # greater than the last element of
                # the answer list, we perform
                # a binary search to find the smallest
                # element in the answer list that
                # is greater than or equal to the
                # current number.
                low = 0
                high = len(ans_arr)

                while low < high:
                    mid = low + (high - low)//2
                    if ans_arr[mid] < nums[i]:
                        low = mid + 1
                    else:
                        high = mid
                ans_arr[low] = nums[i]
        print(ans_arr)
        return len(ans_arr)

       

    # Solution 1  :  
    # # T : O(n^2)
    # # S : O(n)
    # # Actually you have a better solution O(nlogn) using binary search

    # def lengthOfLIS(self, nums: List[int]) -> int:
    #     LIS = [1] * len(nums)
    #     res = 0
    #     for i in range(len(nums)-1, -1, -1):
    #         for j in range(i+1, len(nums)): 
    #             if nums[i] < nums[j]:
    #                 LIS[i] = max(LIS[i], 1+LIS[j])

    #     return max(LIS)

        