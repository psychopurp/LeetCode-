#
# @lc app=leetcode.cn id=860 lang=python3
#
# [860] 柠檬水找零
#

# @lc code=start


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        # 优先用掉10
        five = ten = 0

        for x in bills:
            if x == 5:
                five += 1
            elif x == 10:
                if five == 0:
                    return False
                five -= 1
                ten += 1
            else:
                if ten > 0 and five > 0:
                    ten -= 1
                    five -= 1
                elif five > 3:
                    five -= 3
                else:
                    return False
        return True


# @lc code=end
