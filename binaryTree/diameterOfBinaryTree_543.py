# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author : 
#    @Create Time   : 2025/9/2 22:06
#    @Description   : #543
#
# ===============================================================


"""
给你一棵二叉树的根节点，返回该树的 直径 。

二叉树的 直径 是指树中任意两个节点之间最长路径的 长度 。这条路径可能经过也可能不经过根节点 root 。

两节点之间路径的 长度 由它们之间边数表示。
"""


class Solution:
    def __init__(self):
        self.res = 0

    def traverse(self, node):
        if not node:
            return 0

        left_max = self.traverse(node.left)
        right_max = self.traverse(node.right)

        # 后序位置，顺便计算最大直径
        myDiameter = left_max + right_max
        self.res = max(self.res, myDiameter)

        return 1 + max(left_max, right_max)

    def diameter_of_binary_tree(self, root):
        """
        左子数的最大深度 + 右子树的最大深度
        """
        if not root:
            return

        return self.traverse(root)
