# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author : 
#    @Create Time   : 2025-12-15 17:47
#    @Description   : 
#
# ===============================================================


"""
二叉树中的 路径 被定义为一条节点序列，序列中每对相邻节点之间都存在一条边。同一个节点在一条路径序列中 至多出现一次 。该路径 至少包含一个 节点，且不一定经过根节点。

路径和 是路径中各节点值的总和。

给你一个二叉树的根节点 root ，返回其 最大路径和 。
"""

class Solution:
    def __init__(self):
        self.res = -float('inf')

    def maxPathSum(self, root):
        """
        递归计算最大单边和
        """

        if not root:
            return 0

        self.one_side_sum(root)
        return self.res

    def one_side_sum(self, root):
        """计算最大单边和"""
        if not root:
            return 0

        left_sum = max(self.one_side_sum(root.left), 0)
        right_sum = max(self.one_side_sum(root.right), 0)

        total_sum = left_sum + right_sum + root.val
        self.res = max(self.res, total_sum)

        return max(left_sum, right_sum) + root.val
