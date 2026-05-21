class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=len(prices)
        if l<2:
            return 0
        profit=0
        j=0
        for i in range(l):
            if prices[i]<prices[j]:
                j=i
            profit=max(profit,prices[i]-prices[j])
        return profit