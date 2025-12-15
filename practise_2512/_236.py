# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author : 
#    @Create Time   : 2025/12/14 19:47
#    @Description   : 
#
# ===============================================================


"""
给你输入一棵不含重复值的二叉树，以及存在于树中的两个节点 p 和 q，请你计算 p 和 q 的最近公共祖先节点。
"""


class Solution:
    def lowestCommonAncestor(self, root, p, q):
        """
        非空判断
        """
        if not root:
            return

        if root.val == p.val or root.val == q.val:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root

        return left if left else right