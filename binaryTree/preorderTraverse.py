# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author :
#    @Create Time   : 2023/11/18 16:13
#    @Description   : 二叉树的前序遍历
#
# ===============================================================


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


res = []


def pre_order_traverse(root):
    # 递归的终止条件
    if not root:
        return

    global res
    res.append(root.val)

    pre_order_traverse(root.left)
    pre_order_traverse(root.right)

    return res


