# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author :
#    @Create Time   : 2024/6/27 11:39
#    @Description   : 114. 二叉树展开为链表
#
# ===============================================================

class Solution:
    def flatten(self, root):
        """
        子函数定义：左右子树分别拉直成一条链表，然后将起拼接起来
        :param root:
        :return:
        """
        if not root:
            return

        self.flatten(root.left)
        self.flatten(root.right)

        left = root.left
        right = root.right

        root.left = None
        root.right = left
        p = root
        while p and p.right:
            p = p.right
        p.right = right


