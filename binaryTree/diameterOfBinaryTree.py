# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author :
#    @Create Time   : 2023/11/19 11:44
#    @Description   : 二叉树的直径
#
# ===============================================================


def diameterOfBinaryTree(root):
    """
    二叉树的直径：等于左子树 + 右子数 总结点的最大值
    :param root:
    :return:
    """
    res = 0

    def _diameter_of_binary_tree(node):

        if not node:
            return 0

        global res

        left_count = _diameter_of_binary_tree(node.left)
        right_count = _diameter_of_binary_tree(node.right)

        res = max(res, left_count + right_count)

        return 1 + max(left_count, right_count)

    return _diameter_of_binary_tree(root)


