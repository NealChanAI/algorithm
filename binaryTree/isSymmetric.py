# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author :
#    @Create Time   : 2024/7/1 14:11
#    @Description   : 101. 对称二叉树
#
# ===============================================================


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        1. 相同的根结点
        2. 左子树和右子树镜像对称
        :param root:
        :return:
        """
        if not root:
            return

        def is_symmetric_helper(node1, node2):
            if not node1 and not node2:
                return True

            if not node1 or not node2:
                return False

            return (node1.val == node2.val) & is_symmetric_helper(node1.left, node2.right) \
                & is_symmetric_helper(node1.right, node2.left)

        return is_symmetric_helper(root, root)


