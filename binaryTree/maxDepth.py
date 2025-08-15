# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author :
#    @Create Time   : 2023/11/18 16:06
#    @Description   : 二叉树的最大深度
#
# ===============================================================


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def max_depth(root):
    """
    分解算法
    先求左子树的最大层数，再求右子树的最大层数，取较大值后加1即可；
    :param root:
    :return:
    """
    if not root:
        return 0

    left_max = max_depth(root.left)
    right_max = max_depth(root.right)

    res = max(left_max, right_max) + 1

    return res


def _max_depth(root):
    """
    遍历算法
    :param root:
    :return:
    """

    res = 0
    dep = 0

    def _traverse(root):
        # 合理性判断
        if not root:
            return

        global res, dep
        # 前序位置
        dep += 1
        # 判断是否属于叶子节点
        if not root.left and not root.right:
            res = max(res, dep)

        _traverse(root.left)
        _traverse(root.right)

        dep -= 1

    return res
