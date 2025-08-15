# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author :
#    @Create Time   : 2024/7/1 16:56
#    @Description   : 
#
# ===============================================================


class Solution:
    def isSymmetric(self, root):
        """
        对称二叉树
            1. 左右子树的结点值相等
            2. 左子树的右结点和右子树的左结点相等，反之亦然
        :param root:
        :return:
        """
        if not root:
            return False

        def is_symetric_helper(node1, node2):
            # 两个结点都为空，返回True
            if not node1 and not node2:
                return True

            # 其中一个结点为空
            if not node1 or not node2:
                return False

            return node1.val == node2.val & is_symetric_helper(node1.left, node2.right) & is_symetric_helper(node1.right, node2.left)

        is_symetric_helper(root, root)
