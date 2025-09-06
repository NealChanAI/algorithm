# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author : 
#    @Create Time   : 2025-09-05 9:45
#    @Description   : #101
#
# ===============================================================


"""
给你一个二叉树的根节点 root ， 检查它是否轴对称。
"""


class Solution:
    def _is_summetric(self, left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        if left.val != right.val:
            return False
        return self.is_summetric(left.left, right.right) and self._is_summetric(left.right, right.left)

    def is_summetric(self, root):
        """
        递归
        """
        if not root:
            return

        return self._is_summetric(root.left, root.right)
