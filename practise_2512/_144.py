# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author : 
#    @Create Time   : 2025-12-19 17:58
#    @Description   : 
#
# ===============================================================


"""
给你二叉树的根节点 root ，返回它节点值的 前序 遍历。
"""


class Solution:
    def __init__(self):
        self.res = []

    def preorderTraversal(self, root):
        """递归实现"""
        if not root:
            return

        self.res.append(root.val)
        self.preorderTraversal(root.left)
        self.preorderTraversal(root.right)

        return self.res