# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author :
#    @Create Time   : 2024/7/1 14:52
#    @Description   : 
#
# ===============================================================


class Solution:
    def lowestCommonAncestor(self, root, p, q):
        """
        1. 若可以分别在左右子树中找到p, q，则当前结点为最近公共祖先
        2. 若当前结点为p或q，则当前结点为最近公共祖先
        :param root:
        :param p:
        :param q:
        :return:
        """
        def find(root, p, q):
            # 合理性判断
            if not root:
                return

            # 满足定义2
            if root.val == p.val or root.val == q.val:
                return root

            left = find(root.left, p, q)
            right = find(root.left, p, q)

            if left and right:
                return root

            return left if left else right

