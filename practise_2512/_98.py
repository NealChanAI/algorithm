# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author : 
#    @Create Time   : 2025-12-25 11:07
#    @Description   : 
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
    def isValidBST(self, root):
        """
        构造辅助函数, 引入min_val和max_val
        """
        if not root:
            return

        return self._helper(root, None, None)

    def _helper(self, root, min, max):
        if min and root.val <= min.val:
            return False

        if max and root.val >= max.val:
            return False

        return self._helper(root.left, min, root) and self._helper(root.right, root, max)

