# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author :
#    @Create Time   : 2024/6/30 23:24
#    @Description   : 145. 二叉树的后序遍历
#
# ===============================================================


class Solution:
    def __init__(self):
        self.res = []

    def postorderTraversal(self, root):
        def traverse(root):
            if not root:
                return

            traverse(root.left)
            traverse(root.right)
            self.res.append(root.val)

        traverse(root)
        return self.res