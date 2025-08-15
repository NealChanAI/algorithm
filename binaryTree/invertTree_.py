# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author :
#    @Create Time   : 2024/7/1 17:31
#    @Description   : 
#
# ===============================================================


class Solution:
    def invertTree(self, root):
        """
        递归子函数：返回翻转好的左/右子树
        :param root:
        :return:
        """
        if not root:
            return root

        def invert(root):
            if not root:
                return

            left = invert(root.left)
            right = invert(root.right)

            root.left = right
            root.right = left

            return root

        return invert(root)
