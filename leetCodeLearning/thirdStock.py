
#给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。

#设计一个算法来计算你所能获取的最大利润。你最多可以完成两笔交易。
#你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
#[3,3,5,0,0,3,1,4]  6
# [1,2,3,4,5] 4
# [7,6,4,3,1] 0
class Solution(object):
    def maxProfit(self, prices):
        if not prices:
            return 0
        n = len(prices)
        def dfs(index,status,k):
            # 递归终止条件，数组执行到头了，或者交易了两次了
            if index==n or k==2:
                return 0
            # 定义三个变量，分别记录[不动]、[买]、[卖]
            a,b,c = 0,0,0
            # 保持不动
            a = dfs(index+1,status,k)
            if status:
                # 递归处理卖的情况，这里需要将k+1，表示执行了一次交易
                b = dfs(index+1,0,k+1)+prices[index]
            else:
                # 递归处理买的情况
                c = dfs(index+1,1,k)-prices[index]
            # 最终结果就是三个变量中的最大值
            return max(a,b,c)
        return dfs(0,0,0)

