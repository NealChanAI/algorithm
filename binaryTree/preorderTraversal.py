# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author :
#    @Create Time   : 2024/6/30 23:15
#    @Description   : 144. 二叉树的前序遍历
#
# ===============================================================


class Solution:
    def __init__(self):
        self.res = []

    def preorderTraversal(self, root):
        def traverse(root):
            if not root:
                return

            self.res.append(root.val)
            traverse(root.left)
            traverse(root.right)

        traverse(root)
        return self.res
