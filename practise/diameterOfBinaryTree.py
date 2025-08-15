# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Time   : 2024/8/18 11:13
#    @Description   : 
#
# ===============================================================


class Solution:
    def diameterOfBinaryTree(self, root):
        """二叉树的直径"""
        """求最大深度"""
        if not root:
            return 0

        global res
        res = -1

        def _diameter_of_binary_tree(node):
            if not node:
                return 0

            left = _diameter_of_binary_tree(node.left)
            right = _diameter_of_binary_tree(node.right)

            global res
            res = max(res, left + right)

            return 1 + max(left, right)

        _diameter_of_binary_tree(root)
        return res

