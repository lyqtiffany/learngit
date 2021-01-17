# 121. 买卖股票的最佳时机
#给定一个数组，它的第i 个元素是一支给定股票第n天的价格，
#如果你最多只允许完成一笔交易（即买入和卖出一支股票一次），设定一个算法来计算你所能获取的最大利润
#注意，你不能在买入股票前卖出股票

class Solution(object):
    def maxProfit(self, prices):
        n = len(prices)
        if n == 0:
            return 0
        #动态规划，用两个变量，一个存储当前的最小值，一个存储当前的最大利益。用当前卖出的价值，减去前面的最小值，即为当前收益。
        #随着遍历更新最大收益和最小值，
        profit = 0  #假定最大利润为0
        minPrice = prices[0]  #假定第一个值为最小值
        for i in range(1,len(prices)):
            currentPrice = prices[i]  #当前价格
            minPrice = min(currentPrice, minPrice)  #比较之前的最小值和当前值，更新最小值
            gotProfit = currentPrice - minPrice  #当前利润
            profit = max(gotProfit, profit)  #比较之前利润和当前利润，更新最大利润
            #print('currentgotProfit:', gotProfit, 'currentPrice', currentPrice, 'minPrice', minPrice,'max profit',profit)
        # print(profit)
        return profit

    def maxProfitB(self, prices) :  #B写法更简洁
        inf = int(1e9)
        minprice = inf
        maxprofit = 0
        for price in prices:
            maxprofit = max(price - minprice, maxprofit)
            minprice = min(price, minprice)
        return maxprofit

    def maxProfitC(self, prices) : #动态规划
        n = len(prices)
        if n == 0: return 0 # 边界条件
        dp = [0] * n
        minprice = prices[0]
        for i in range(1, n):
            minprice = min(minprice, prices[i])
            dp[i] = max(dp[i - 1], prices[i] - minprice)
        return dp[-1]

if __name__ == '__main__':
    a = Solution()
    aPrice = [7, 1, 5, 3, 6, 4]  #5
    bPrice = [7, 6, 4, 3, 1]  #0
    cPrice = [1, 2, 3, 4, 5] #4
    print(a.maxProfit(aPrice))
    print(a.maxProfit(bPrice))
    print(a.maxProfit(cPrice))
    print(a.maxProfitB(aPrice))
    print(a.maxProfitB(bPrice))
    print(a.maxProfitB(cPrice))
    print(a.maxProfitC(aPrice))
    print(a.maxProfitC(bPrice))
    print(a.maxProfitC(cPrice))