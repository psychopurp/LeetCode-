#
# @lc app=leetcode.cn id=714 lang=python3
#
# [714] Best Time to Buy and Sell Stock with Transaction Fee
#

# @lc code=start
from typing import List


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        # DP
        # time complexity: O(N)
        # space complexity: O(1)
        '''
        For every day, we've three choices:
        1.Don't do anything : cur_hold=pre_hold, cur_not_hold=pre_not_hold
        2.Sell them for a profit : cur_not_hold=pre_hold+price
        3.Buy new stock : cur_hold=pre_not_hold-price
        '''

        cur_hold, cur_not_hold = float("-inf"), 0

        for price in prices:
            pre_hold, pre_not_hold = cur_hold, cur_not_hold

            cur_hold = max(pre_hold, pre_not_hold-price)
            cur_not_hold = max(pre_not_hold, pre_hold+price-fee)

        return cur_not_hold
# @lc code=end
