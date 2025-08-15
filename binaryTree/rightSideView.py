# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author :
#    @Create Time   : 2024/6/30 23:42
#    @Description   : 199. 二叉树的右视图
#
# ===============================================================


class Solution:
    def rightSideView(self, root):
        res = []

        def traverse(root, depth):
            if not root:
                return

            if depth == len(res):
                res.append(root.val)

            traverse(root.left, depth + 1)
            traverse(root.right, depth + 1)

        traverse()

        return res
