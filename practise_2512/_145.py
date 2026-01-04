# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author : 
#    @Create Time   : 2026-01-04 11:23
#    @Description   : 
#
# ===============================================================


"""
二叉树的后序遍历
"""


class Solution:
    def postorderTraversal(self, root):
        if not root:
            return []

        res = []

        def _traverse(root):
            if not root:
                return

            _traverse(root.left)
            _traverse(root.right)

            res.append(root.val)

        _traverse(root)

        return res


