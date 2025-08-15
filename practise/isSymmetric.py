# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Time   : 2024/8/18 10:51
#    @Description   : 
#
# ===============================================================


class Solution:
    def isSymmetric(self, root):
        """
        1. 相同的根结点

        :param root:
        :return:

        """
        if not root:
            return

        def _is_symmetric_helper(node1, node2):
            # 两者都不存在
            if not node1 and not node2:
                return True

            # 任一方不存在
            if not node1 or not node2:
                return False

            # 值不相同
            if node1.val != node2.val:
                return False

            return (node1.val == node2.val) and (_is_symmetric_helper(node1.left, node2.right)) and (_is_symmetric_helper(node1.right, node2.left))

        return _is_symmetric_helper(root.left, root.right)