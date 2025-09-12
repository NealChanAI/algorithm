# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author : 
#    @Create Time   : 2025-09-05 10:07
#    @Description   : #112
#
# ===============================================================


"""
给你二叉树的根节点 root 和一个表示目标和的整数 targetSum 。判断该树中是否存在 根节点到叶子节点 的路径，这条路径上所有节点值相加等于目标和 targetSum 。如果存在，返回 true ；否则，返回 false 。

叶子节点 是指没有子节点的节点。
"""


class Solution:
    def __init__(self):
        self.sum = 0
        self.res = False

    def traverse(self, root, target):
        if not root:
            return

        # 前序遍历
        self.sum += root.val

        # 当前节点为叶子结点
        if not root.left and not root.right:
            if self.sum == target:
                self.res = True
                return

        self.traverse(root.left, target)
        self.traverse(root.right, target)

        # 离开节点
        self.sum -= root.val

    def hasPathSum(self, root, target):
        """
        遍历
        """
        if not root:
            return False

        self.traverse(root, target)

        return self.res
