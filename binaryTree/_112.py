# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author : 
#    @Create Time   : 2025-12-08 17:41
#    @Description   : 
#
# ===============================================================


"""
给你二叉树的根节点 root 和一个表示目标和的整数 targetSum 。判断该树中是否存在 根节点到叶子节点 的路径，这条路径上所有节点值相加等于目标和 targetSum 。如果存在，返回 true ；否则，返回 false 。

叶子节点 是指没有子节点的节点。
"""


class Solution:
    def __init__(self):
        self.res = False
        self.sum = 0

    def traverse(self, root, target):
        """遍历"""
        # base case
        if not root:
            return
        # 前序遍历
        self.sum += root.val

        if not root.left and not root.right:
            if self.sum == target:
                self.res = True
                return

        self.traverse(root.left)
        self.traverse(root.right)

        self.sum -= root.val

    def hasPathSum(self, root, target):
        """
        1. 非空判断
        2. 递归遍历
        """
        if not root:
            return

        self.traverse(root, target)

        return self.res
