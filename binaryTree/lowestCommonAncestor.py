# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author :
#    @Create Time   : 2024/6/30 22:23
#    @Description   : 236. 二叉树的最近公共祖先
#
# ===============================================================


class Solution:
    def lowestCommonAncestor(self, root, p, q):
        """
        定义helper函数，在子树中查找对应的值
        :param root:
        :param p:
        :param q:
        :return:
        """
        def find(root, val1, val2):
            if not root:
                return

            if root.val == val1 or root.val == val2:
                return root

            left = find(root.left, val1, val2)
            right = find(root.right, val1, val2)

            if left and right:
                return root

            return left if left else right

        return find(root, p.val, q.val)

