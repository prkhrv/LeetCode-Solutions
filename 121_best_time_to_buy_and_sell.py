class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = min(prices)
        max_price = max(prices)
        min_index = prices.index(min_price)
        max_index = prices.index(max_price)
        
        if max_index > min_index:
            return max_price - min_price
        else:
            buy = 0
            sell = 0
            profit = [0]
            for i,p in enumerate(prices):
                
                if p < prices[buy]:
                    buy = i
                elif p > prices[sell] or buy > sell:
                    sell = i
                    profit.append(prices[sell] - prices[buy])
                
            return max(profit)
                
