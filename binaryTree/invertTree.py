# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author :
#    @Create Time   : 2024/6/27 11:15
#    @Description   : 226. 翻转二叉树
#
# ===============================================================

class Solution:
    def invertTree(self, root):
        """
        递归子函数：左右子树分别翻转，然后翻转当前子树
        :param root:
        :return:
        """
        if not root:
            return

        self.invertTree(root.left)
        self.invertTree(root.right)

        tmp = root.left
        root.left = root.right
        root.right = tmp

        return root
