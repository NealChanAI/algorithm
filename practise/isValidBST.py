# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Time   : 2024/8/18 11:19
#    @Description   : 
#
# ===============================================================


class Solution:
    def isValidBST(self, root):
        """

        :param root:
        :return:
        """
        def _is_valid_BST(root, min_node, max_node):
            # base case
            if not root:
                return True

            if min_node and min_node.val >= root.val:
                return False

            if max_node and max_node.val <= root.val:
                return False

            return _is_valid_BST(root.left, min_node, root) and _is_valid_BST(root.right, root, max_node)

        return _is_valid_BST(root, None, None)
