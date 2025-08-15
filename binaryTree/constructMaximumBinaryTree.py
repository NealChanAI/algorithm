# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author :
#    @Create Time   : 2024/6/27 15:20
#    @Description   : 654. 最大二叉树
#
# ===============================================================

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def constructMaximumBinaryTree(self, nums):
        """
        递归子函数：左边构造完，右边构造完，行程左右子节点
        :param nums:
        :return:
        """
        def build(nums, low, high):
            if low > high:
                return

            idx, max_num = -1, -float("inf")
            for i in range(low, high + 1):
                if nums[i] > max_num:
                    idx = i
                    max_num = nums[i]

            root = TreeNode(max_num)

            root.left = build(nums, low, idx - 1)
            root.right = build(nums, idx + 1, high)

            return root

        return build(nums, 0, len(nums) - 1)