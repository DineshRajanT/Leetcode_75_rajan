class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        res = []

        def dfs(i, currCombination, currTotal):
            # Inga oru oru index layum currTotal check panuven, if matches the target then curr combination is a potential answer to be         appended.....
            if currTotal == target:
                res.append(currCombination.copy())
                return

            # base case to break the recursion loop
            if i >= len(candidates) or currTotal > target:
                return
            
            # Two Ways now :
        
            # Two decisions to be made to avoid getting duplicate combinations.
            # one is to include the curr value to form a psooible combination and 
            # other is not to include the curr value in the combination and try with other elements in the list.
            # with candidates[i]
            currCombination.append(candidates[i])
            dfs(i, currCombination, currTotal+candidates[i])

            # without candidates[i] 
            currCombination.pop() # pop the previosuly appended value from the combiantion list
            # increment the i , so as the not include the curr value and moving to other possible values
            dfs(i+1, currCombination, currTotal)


        dfs(0, [], 0)
        return res

