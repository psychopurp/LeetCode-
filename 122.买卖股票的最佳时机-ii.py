#
# @lc app=leetcode.cn id=122 lang=python3
#
# [122] 买卖股票的最佳时机 II
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        money=0
        for i,k in enumerate(prices):
            if i+1==len(prices):
                break
            if prices[i+1]>prices[i]:
                money=money-prices[i]+prices[i+1]

        return money
# @lc code=end

