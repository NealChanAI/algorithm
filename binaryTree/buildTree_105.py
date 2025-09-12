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
    def buildTree(self, preorder, inorder):
        """
        递归构造：
            1. 前序的第一个结点为头结点
            2. 在中序列表中找到头节点的位置，则左边为左子树的列表，右边为右子树

        :param preorder:
        :param inorder:
        :return:
        """
        if not preorder or not inorder:
            return

        def _builder(pre_order, pre_start, pre_end, in_order, in_start, in_end):
            """"""
            # base case
            if pre_start > pre_end:
                return
            # 头结点位置
            head = pre_order[pre_start]
            # 在中序列表中找到head结点的位置
            head_idx = 0
            for i in range(in_start, in_end + 1):
                if in_order[i] == head:
                    head_idx = i
                    break

            root = TreeNode(head)
            root.left = _builder(pre_order, pre_start+1, pre_start+(head_idx-in_start), in_order, in_start, head_idx-1)
            root.right = _builder(pre_order, pre_start+(head_idx-in_start)+1, pre_end, in_order, head_idx+1, in_end)

            return root

        return _builder(preorder, 0, len(preorder)-1, inorder, 0, len(inorder)-1)





