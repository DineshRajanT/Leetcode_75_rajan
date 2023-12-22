class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        rightMax = prices[-1]
        maxSell = [0] * len(prices)

        for i in reversed(range(0,len(prices)-1)):
            if prices[i] > rightMax:
                rightMax = prices[i]
            maxSell[i] = rightMax

        maxProfit = 0
        for i in range(len(prices)):
            maxProfit = max(maxProfit, maxSell[i]-prices[i])
        return maxProfit

        