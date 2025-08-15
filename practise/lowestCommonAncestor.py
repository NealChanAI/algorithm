# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Time   : 2024/7/16 20:55
#    @Description   : 
#
# ===============================================================


class Solution:
    def lowestCommonAncestor(self, root, p, q):
        """

        :param root:
        :return:
        """
        if not root:
            return

        def find_helper(root, val1, val2):
            if not root:
                return

            if root.val == val1 or root.val == val2:
                return root

            left = find_helper(root.left, val1, val2)
            right = find_helper(root.right, val1, val2)

            if left and right:
                return root

            return left if left else right

        return find_helper(root, p.val, q.val)
