# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author : 
#    @Create Time   : 2025-09-05 10:21
#    @Description   : #113
#
# ===============================================================


"""
给你二叉树的根节点 root 和一个整数目标和 targetSum ，找出所有 从根节点到叶子节点 路径总和等于给定目标和的路径。

叶子节点 是指没有子节点的节点。
"""


class Solution:
    def __init__(self):
        self.res = []
        self.path = []
        self.sum = 0

    def traverse(self, root, target):
        if not root:
            return

        # 前序
        self.sum += root.val
        self.path.append(root.val)

        # 叶子节点时
        if not root.left and not root.right:
            if self.sum == target:
                self.res.append(self.path.copy())

        self.traverse(root.left, target)
        self.traverse(root.right, target)

        # 后序
        self.sum -= root.val
        self.path.pop()

    def pathSum(self, root, target):
        if not root:
            return self.res

        self.traverse(root, target)

        return self.res

