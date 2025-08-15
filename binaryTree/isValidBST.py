# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author :
#    @Create Time   : 2024/6/30 21:42
#    @Description   : 98. 验证二叉搜索树
#
# ===============================================================


class Solution:
    def isValidBST(self, root):
        """

        :param root:
        :return:
        """
        def isValidBSTHelper(root, min_node, max_node):
            # base case
            if not root:
                return True

            if min_node and min_node.val >= root.val:
                return False

            if max_node and max_node.val <= root.val:
                return False

            return isValidBSTHelper(root.left, min_node, root) and isValidBSTHelper(root.right, root, max_node)

        return isValidBSTHelper(root, None, None)

