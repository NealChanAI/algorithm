# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author :
#    @Create Time   : 2024/8/18 10:56
#    @Description   : 
#
# ===============================================================


class Solution:
    def maxDepth(self, root):
        """二叉树的最大深度"""
        if not root:
            return 0

        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        return 1 + max(left, right)