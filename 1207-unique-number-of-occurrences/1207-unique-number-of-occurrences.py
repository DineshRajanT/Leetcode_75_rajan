class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count_arr={}
        for ele in arr:
            count_arr[ele] = count_arr.get(ele,0) + 1
        
        if len(count_arr) == len(set(count_arr.values())):
            return True
        return False