# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author : 
#    @Create Time   : 2026-03-27 12:48
#    @Description   : 
#
# ===============================================================


"""
给你输入一棵不含重复值的二叉树，以及存在于树中的两个节点 p 和 q，请你计算 p 和 q 的最近公共祖先节点。
"""


class Solution:
    def lowestCommonAncestor(self, root, p, q):
        if not root:
            return

        if root.val == p or root.val == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root

        return left if left else right