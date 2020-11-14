#给定一个数组，它的第i 个元素是一支给定股票第n天的价格，
#如果你最多只允许完成一笔交易（即买入和卖出一支股票一次），设定一个算法来计算你所能获取的最大利润
#注意，你不能在买入股票前卖出股票

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        min_price = prices[0]
        a = 0
        for i in range(1, len(prices)):
            min_price = min(prices[i], min_price)
            a = max(a, prices[i] - min_price)
        print(a)
        return a

'''class Solution:
    def maxProfit(self, prices):
        inf = int(1e9)
        minprice = inf
        maxprofit = 0
        for price in prices:
            minprice = min(price, minprice)  #比较次数
            maxprofit = max(price - minprice, maxprofit)
        print(maxprofit)
        return maxprofit'''

'''class Solution:
    def maxProfit(self, prices):
        ans = 0
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):    #比较次数很多
                ans = max(ans, prices[j] - prices[i]) #当前利润, 比较后面的值和当前值之间的利润
        print(ans)
        return ans'''

'''class Solution:
    def maxProfit(self, prices):
        n = len(prices)
        if n == 0:
            return 0 # 边界条件
        dp = [0] * n
        minprice = prices[0]

        for i in range(1, n):
            minprice = min(minprice, prices[i])   #动态规划，比较次数少
            dp[i] = max(dp[i - 1], prices[i] - minprice)
            #print('dpi', dp[i],'prices[i]', prices[i], 'minprice', minprice)
        print(dp[-1])
        return dp[-1]'''

bb = Solution()
aPrice = [7, 1, 5, 3, 6, 4]  #5
bPrice = [7, 6, 4, 3, 1]  #0
cPrice = [1, 2, 3, 4, 5]  #4
bb.maxProfit(aPrice)
bb.maxProfit(bPrice)
bb.maxProfit(cPrice)

#by tifffany
priceArray1 = [7, 1, 6, 3, 4, 5]
aPrice = [7, 1, 5, 3, 6, 4]  #5
bPrice = [7, 6, 4, 3, 1]  #0
cPrice = [1, 2, 3, 4, 5]  #4
def getProfit(arr):
    minPrice = arr[0]
    profit = 0
    for i in range(len(arr)):
        minPrice = min(minPrice, arr[i])
        profit = max(profit, arr[i] - minPrice)
    print(profit, minPrice)

getProfit(aPrice)
getProfit(bPrice)
getProfit(cPrice)