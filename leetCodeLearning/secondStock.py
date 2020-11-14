#给定一个数组，它的第i 个元素是一支给定股票第n天的价格，
#设定一个算法来计算你所能获取的最大利润，你可以尽可能地完成更多的交易（多次买卖一支股票）
#注意，你不能同时参与多比交易，必须在再次在买入股票前卖出之前的股票
from typing import List


'''class Solution:
    def maxProfit(self, prices):
        n = len(prices)
        if n == 0:
            return 0 # 边界条件
        dp = [0] * n
        minprice = prices[0]

        for i in range(1, n):
            minprice = min(minprice, prices[i])
            dp[i] = max(dp[i - 1], prices[i] - minprice)  #动态规划, only 1 trade allowed
            print('dpi', dp[i],'prices[i]', prices[i], 'minprice', minprice)
        print(dp[-1])
        return dp[-1]'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:  #multiple trade allowed
                ans += prices[i] - prices[i-1]  #第二种方法：贪心算法，一次遍历，只要今天价格小于明天价格就在今天买入然后明天卖出，时间复杂度O(n)
                #print(ans, prices[i], prices[i-1])
        print(ans)
        return ans

#：DP动态规划，第i天只有两种状态，不持有或持有股票，当天不持有股票的状态可能来自昨天卖出或者昨天也不持有，
# 同理，当天持有股票的状态可能来自昨天买入或者昨天也持有中，取最后一天的不持有股票状态就是问题的解
'''class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        n = len(prices)
        dp = [[0]*2 for _ in range(n)]
        # dp[i][0]表示第i天不持有股票, dp[i][1]表示第i天持有股票
        dp[0][0], dp[0][1] = 0, - prices[0]
        for i in range(1, n):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])
        print(dp[n-1][0])
        return dp[n-1][0]'''

'''class Solution(object):
    def maxProfit(self, prices):
        profit = 0
        for day in range(len(prices)-1):
            differ = prices[day+1] - prices[day] #最大利润就是所有大于0的差值之和。现实中就是吃到了每一波上涨的全部涨幅，且不受每一波下跌的影响。
            if differ > 0:
                profit += differ
                #print(profit, differ)
        print(profit)
        return profit'''

bb = Solution()
aPrice = [7, 1, 5, 3, 6, 4, 5]  #7
bPrice = [7, 6, 4, 3, 1]  #0
cPrice = [1, 2, 3, 4, 5]  #4
bb.maxProfit(aPrice)
bb.maxProfit(bPrice)
bb.maxProfit(cPrice)


#by tiffany
def maxProfit(arr):
    profit = 0
    #minPrice = arr[0]
    for i in range(1,len(arr)):
        if arr[i] > arr[i-1]:
            profit += arr[i] - arr[i-1]
        #print(i, profit, arr[i], arr[i-1])
    print(profit)
stockPrice = [7, 1, 6, 3, 4, 9]
maxProfit(stockPrice)
aPrice = [7, 1, 5, 3, 6, 4, 5]  #7
bPrice = [7, 6, 4, 3, 1]  #0
cPrice = [1, 2, 3, 4, 5]  #4
maxProfit(aPrice)
maxProfit(bPrice)
maxProfit(cPrice)