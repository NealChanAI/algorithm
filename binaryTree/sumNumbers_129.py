# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author : 
#    @Create Time   : 2025-09-04 20:38
#    @Description   : #129
#
# ===============================================================


"""
给你一个二叉树的根节点 root ，树中每个节点都存放有一个 0 到 9 之间的数字。
每条从根节点到叶节点的路径都代表一个数字：

例如，从根节点到叶节点的路径 1 -> 2 -> 3 表示数字 123 。
计算从根节点到叶节点生成的 所有数字之和 。

叶节点 是指没有子节点的节点。
"""


class Solution:
    def __init__(self):
        self.path = ''
        self.res = 0

    def traverse(self, root):
        if not root:
            return

        # 前序遍历
        self.path += str(root.val)

        # 若为叶子节点
        if not root.left and not root.right:
            self.res += int(self.path)

        self.traverse(root.left)
        self.traverse(root.right)

        self.path.pop()

    def sum_numbers(self, root):
        self.traverse(root)
        return self.res
