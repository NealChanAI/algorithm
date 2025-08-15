# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author :
#    @Create Time   : 2024/7/1 14:44
#    @Description   : 958. 二叉树的完全性检验
#
# ===============================================================


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def isCompleteTree(self, root):
        """
        :param root:
        :return:
        """