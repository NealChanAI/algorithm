# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author : 
#    @Create Time   : 2025-09-04 15:55
#    @Description   : #110
#
# ===============================================================


"""
给定一个二叉树，判断它是否是 平衡二叉树
"""


class Solution:
    def __init__(self):
        self.res = True

    def traverse(self, root):
        """
        子函数: 返回节点的最大深度
        """
        if not root:
            return

        left_max = self.traverse(root.left)
        right_max = self.traverse(root.right)

        # 更新结果
        if left_max - right_max > 1 or right_max - left_max > 1:
            self.res = False
            return

        return 1 + max(left_max, right_max)

    def isBalanced(self, root):
        """
        判断左右子树的深度相差是否大于1
        """
        if not root:
            return

        self.traverse(root)

        return self.res