#
# @lc app=leetcode.cn id=198 lang=python3
#
# [198] House Robber
#

# @lc code=start
from typing import List


class Solution:
    # def rob(self, nums: List[int]) -> int:
    #     # backtraking (TLE)
    #     # time complexity: O(2^N)
    #     # space complexity: O(N)

    #     def backtracking(step: int, ways: List[int]):
    #         nonlocal max_val
    #         if step >= len(nums):
    #             max_val = max(max_val, sum(ways))
    #             return

    #         for i in range(step, len(nums)):
    #             ways.append(nums[i])
    #             backtracking(i+2, ways)
    #             ways.pop()

    #     max_val = 0
    #     backtracking(0, [])
    #     return max_val

    # def rob(self, nums: List[int]) -> int:
    #     # DP
    #     # time complexity: O(N*N)
    #     # space complexity: O(N)
    #     '''
    #     dp[i] represent the maximum amount when we robbed the i.
    #     '''

    #     dp = []
    #     for i in range(len(nums)):
    #         dp.append(nums[i])

    #         k = i-2
    #         # find the house we can rob
    #         while k >= 0:
    #             dp[i] = max(dp[i], dp[k]+nums[i])
    #             k -= 1
    #     return max(dp)

    # def rob(self, nums: List[int]) -> int:
    #     # Bottom-up DP
    #     # time complexity: O(N)
    #     # space complexity: O(N) can be optimized to O(1) by using variable instead of DP array.
    #     '''
    #     dp[i] represent the maximum amount till i.
    #     dp[i] = max( dp[i-1] , dp[i-2]+nums[i])
    #     dp[i-2]+nums[i] : we rob the i
    #     dp[i-1] : we did't rob the i
    #     '''

    #     n = len(nums)
    #     dp = [0]*(n+2)

    #     for i in range(n):
    #         dp[i] = max(dp[i-1], dp[i-2]+nums[i])
    #     return dp[n-1]

    # def rob(self, nums: List[int]) -> int:
    #     # Bottom-up DP
    #     # time complexity: O(N)
    #     # space complexity: O(1)
    #     '''
    #     rub : represents the maximum amount we will have if last night we robbed
    #     not_rub : represents the amount we will have if last night we did't rob
    #     '''

    #     rub = not_rub = amount = 0

    #     for i in range(len(nums)):
    #         rub, not_rub = max(not_rub+nums[i], rub), rub
    #         amount = max(amount, rub, not_rub)
    #     return amount

    def rob(self, nums: List[int]) -> int:
        # Recursive (top-down DP)
        # time complexity: O(N)
        # space complexity: O(N)
        '''
        dp[i] represent the maximum amount till i.
        '''

        def dp(i: int) -> int:
            if i < 0:
                return 0
            if i in memo:
                return memo[i]

            memo[i] = max(dp(i-2)+nums[i], dp(i-1))
            return memo[i]

        memo = {}
        return dp(len(nums)-1)


# @lc code=end
