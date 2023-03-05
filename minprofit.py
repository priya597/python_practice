

def maxProfit(self, prices):
    
    sellProfit = 0;
    minBuyDay = prices[0];
    for i in range(1,len(prices)):
        if minBuyDay < prices[i]:
            profit = prices[i] - minBuyDay;
            sellProfit = max(sellProfit, profit)
        else:
            minBuyDay = prices[i]
            
    return sellProfit

print(maxProfit('self',[7,1,5,3,6,4]))
