# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author : 
#    @Create Time   : 2025/9/7 21:24
#    @Description   : #94
#
# ===============================================================


"""
给定一个二叉树的根节点 root ，返回 它的 中序 遍历 。
"""


class Solution:
    def __init__(self):
        self.res = []

    def inorder_traversal(self, root):
        if not root:
            return

        self.inorder_traversal(root.left)
        self.res.append(root.val)
        self.inorder_traversal(root.right)
