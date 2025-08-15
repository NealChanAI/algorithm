# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author :
#    @Create Time   : 2024/6/30 23:11
#    @Description   : 94. 二叉树的中序遍历
#
# ===============================================================


class Solution:
    def __init__(self):
        self.res = []

    def inorderTraversal(self, root):
        """
        递归子函数：遍历左子树，再遍历root，最后遍历右子树；base case为null
        :param root:
        :return:
        """
        def traverse(root):
            if not root:
                return

            traverse(root.left)
            self.res.append(root.val)
            traverse(root.right)

        traverse(root)
        return self.res

