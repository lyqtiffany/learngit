#122 给定一个数组，它的第i 个元素是一支给定股票第n天的价格，
#设定一个算法来计算你所能获取的最大利润，你可以尽可能地完成更多的交易（多次买卖一支股票）
#注意，你不能同时参与多比交易，必须在再次在买入股票前卖出之前的股票

class Solution:

    def maxProfit(self, prices) -> int:
        n = len(prices)
        if n <= 1: return 0
        profit = 0
        for i in range(1, n):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]
        return profit


if __name__ == '__main__':
    print(Solution().maxProfit([7,1,5,3,6,4])) #7
    print(Solution().maxProfit([1,2,3,4,5])) #4
    print(Solution().maxProfit([7,6,4,3,1])) #0

