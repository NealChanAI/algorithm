# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author :
#    @Create Time   : 2024/6/12 23:38
#    @Description   : 
#
# ===============================================================

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.right = right
        self.left = left


res = -float('inf')


def max_path_sum(root):
    """
    递归函数定义：返回子树的最大单边路径
    :param root:
    :return:
    """
    if not root:
        return 0
    global res

    left_max = max(max_path_sum(root.left), 0)
    right_max = max(max_path_sum(root.right), 0)
    tmp_max = root.val + left_max + right_max
    res = max(res, tmp_max)

    return root.val + max(left_max, right_max)
