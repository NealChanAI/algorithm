# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Time   : 2024/8/17 17:31
#    @Description   : 
#
# ===============================================================


class Solution:
    def lowestCommonAncestor(self, root, p, q):
        """
        最近公共节点：
            1. 当前节点的值是p或q，则当前节点为最近公共节点
            2. 在左右子树分别找p和q的值，若存在，即当前节点为最近公共节点
        :param root:
        :param p:
        :param q:
        :return:
        """
        if not root:
            return

        def _lowest_common_ancestor(head, val_1, val_2):
            if not head:
                return

            # case1: 当前节点的值是p或q，则当前节点为最近公共节点
            if head.val == val_1 or head.val == val_2:
                return head

            # 在左右子树分别找p和q的值，若都存在，即当前节点为最近公共节点
            left = _lowest_common_ancestor(head.left, val_1, val_2)
            right = _lowest_common_ancestor(head.right, val_1, val_2)
            if left and right:
                return head

            # 结果在左子树或右子树中
            return left if left else right

        return _lowest_common_ancestor(root, p.val, q.val)
