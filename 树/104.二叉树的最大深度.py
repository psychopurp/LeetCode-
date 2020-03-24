#
# @lc app=leetcode.cn id=104 lang=python3
#
# [104] 二叉树的最大深度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        left_hegiht = self.maxDepth(root.left)
        right_hegight = self.maxDepth(root.right)
        return max(left_hegiht, right_hegight)+1


# @lc code=end
