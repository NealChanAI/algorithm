# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author : 
#    @Create Time   : 2025/9/2 21:58
#    @Description   : #144
#
# ===============================================================


"""
给你二叉树的根节点 root ，返回它节点值的 前序 遍历。
"""


class Solution:
    def __init__(self):
        self.res = []

    def traverse(self, node):
        if not node:
            return

        self.res.append(node.val)
        self.traverse(node.left)
        self.traverse(node.right)

    def preorder_traversal(self, root):
        self.traverse(root)

        return self.res



