# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author : 
#    @Create Time   : 2025-09-05 9:55
#    @Description   : #124
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

    def one_side_sum(self, root):
        if not root:
            return 0
        left_side_sum_max = max(0, self.one_side_sum(root.left))
        right_side_sum_max = max(0, self.one_side_sum(root.right))

        res = root.val + left_side_sum_max + right_side_sum_max
        self.res = max(self.res, res)
        return res + max(left_side_sum_max, right_side_sum_max)

    def maxPathSum(self, root):
        """
        子问题拆解:
            对于每个节点, 计算左子树的最大和右子树的最大和, 然后三者相加, 注意子树的最大和为max(0, one_side_sum)
        """
        if not root:
            return

        self.one_side_sum(root)

        return self.res
