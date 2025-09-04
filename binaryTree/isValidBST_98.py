# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author : 
#    @Create Time   : 2025-09-04 18:11
#    @Description   : #98
#
# ===============================================================


"""
给你一个二叉树的根节点 root ，判断其是否是一个有效的二叉搜索树。

有效 二叉搜索树定义如下：

节点的左子树只包含 小于 当前节点的数。
节点的右子树只包含 大于 当前节点的数。
所有左子树和右子树自身必须也是二叉搜索树。
"""


class Solution:
    def _is_valid_bst(self, root, min_val, max_val):
        if not root:
            return True

        if min_val and root.val <= min_val:
            return False

        if max_val and root.val >= max_val:
            return False

        return self._is_valid_bst(root.left, min_val, root.val) and self._is_valid_bst(root.right, root.val, max_val)

    def is_valid_BST(self, root):
        if not root:
            return True

        return self._is_valid_bst(root, None, None)
