# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author : 
#    @Create Time   : 2025-09-04 16:37
#    @Description   : #105
#
# ===============================================================


"""
给定两个整数数组 preorder 和 inorder ，其中 preorder 是二叉树的先序遍历，
inorder 是同一棵树的中序遍历，请构造二叉树并返回其根节点。

输入: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
输出: [3,9,20,null,null,15,7]
示例 2:

输入: preorder = [-1], inorder = [-1]
输出: [-1]

preorder 和 inorder 均 无重复 元素
"""


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def construct(self, pre_order, pre_start, pre_end, in_order, in_start, in_end):
        if pre_start > pre_end or in_start > in_end:
            return

        root_val = pre_order[pre_start]
        root = TreeNode(root_val)

        idx = -1
        for i in range(in_start, in_end+1):
            if in_order[i] == root_val:
                idx = i
                break

        left = self.construct(pre_order, pre_start+1, pre_start+idx-in_start, in_order, in_start, idx-1)
        right = self.construct(pre_order, pre_start+idx-in_start+1, pre_end, in_order, idx+1, in_end)

        root.left = left
        root.right = right

        return root

    def build_tree(self, preorder, inorder):
        """
        递归
        """

        root = self.construct(preorder, 0, len(preorder)-1, inorder, 0, len(inorder)-1)
        return root




