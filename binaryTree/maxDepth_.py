# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author :
#    @Create Time   : 2024/6/12 22:38
#    @Description   : 
#
# ===============================================================

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def maxDepth(root):
    """
    子函数定义：返回子树的最大深度，即分别返回左右子树的最大深度，对比后 + 1
    base case: none, 0

    :param root:
    :return:
    """

    if not root:
        return 0

    left_max = maxDepth(root.left)
    right_max = maxDepth(root.right)

    return 1 + max(left_max, right_max)
