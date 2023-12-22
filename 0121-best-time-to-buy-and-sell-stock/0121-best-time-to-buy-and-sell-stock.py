class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # T:O(N) 
        # S:O(N)

        # maxProfit = 0
        # rightMax = prices[-1]
        # maxSell = [0] * len(prices)

        # for i in reversed(range(0,len(prices)-1)):
        #     if prices[i] > rightMax:
        #         rightMax = prices[i]
        #     maxSell[i] = rightMax

        # for i in range(len(prices)):
        #     maxProfit = max(maxProfit, maxSell[i]-prices[i])
        # return maxProfit
        #***************************************#

        # T:O(N) 
        # S:O(1)
        maxProfit = 0
        rightMax = prices[-1]
        maxSell = [0] * len(prices)

        for i in reversed(range(0,len(prices)-1)):
            if prices[i] > rightMax:
                rightMax = prices[i]
            maxSell[i] = rightMax
            maxProfit = max(maxProfit, maxSell[i]-prices[i])

        return maxProfit


        