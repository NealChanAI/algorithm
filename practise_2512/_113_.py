# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author : 
#    @Create Time   : 2026-01-05 14:15
#    @Description   : 
#
# ===============================================================


"""
给你二叉树的根节点 root 和一个整数目标和 targetSum ，找出所有 从根节点到叶子节点 路径总和等于给定目标和的路径。

叶子节点 是指没有子节点的节点。
"""


class Test:
    def __init__(self):
        self.res = []
        self.path = []
        self.sum = 0

    def pathSum(self, root, targetSum):
        self._back_track(root, targetSum)

        return self.res

    def _back_track(self, root, target):
        # base case
        if not root:
            return

        self.sum += root.val
        self.path.append(str(root.val))

        if not root.left and not root.right:
            if self.sum == target:
                self.res.append(self.path.copy())

        self._back_track(root.left, target)
        self._back_track(root.right, target)

        self.path.pop()
        self.sum -= root.val