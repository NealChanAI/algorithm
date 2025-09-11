# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author : 
#    @Create Time   : 2025-09-05 11:36
#    @Description   : #236
#
# ===============================================================


"""
给你输入一棵不含重复值的二叉树，以及存在于树中的两个节点 p 和 q，请你计算 p 和 q 的最近公共祖先节点。
"""


class Solution:
    def find(self, root, val1, val2):
        if not root:
            return
        if root.val == val1 or root.val == val2:
            return root

        left = self.find(root.left, val1, val2)
        right = self.find(root.right, val1, val2)

        if left and right:
            return root

        return left if left else right

    def lowestCommonAncestor(self, root, p, q):
        if not root:
            return

        return self.find(root, p.val, q.val)
