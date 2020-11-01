#给定一个数组，它的第i 个元素是一支给定股票第n天的价格，
#设定一个算法来计算你所能获取的最大利润，你可以尽可能地完成更多的交易（多次买卖一支股票）
#注意，你不能同时参与多比交易，必须在再次在买入股票前卖出之前的股票

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 0: return 0 # 边界条件
        dp = [0] * n
        minprice = prices[0]

        for i in range(1, n):
            minprice = min(minprice, prices[i])
            dp[i] = max(dp[i - 1], prices[i] - minprice)

        return dp[-1]

