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
            profit = max(gotProfit, currentPrice)  #比较之前利润和当前利润，更新最大利润
            print('currentgotProfit:', gotProfit, 'currentPrice', currentPrice, 'minPrice', minPrice,'max profit',profit)
        print(profit)
        return profit
a = Solution()
aPrice = [7, 1, 5, 3, 6, 4]  #5
bPrice = [7, 6, 4, 3, 1]  #0
cPrice = [1, 2, 3, 4, 5]
a.maxProfit(aPrice)
a.maxProfit(bPrice)
a.maxProfit(cPrice)