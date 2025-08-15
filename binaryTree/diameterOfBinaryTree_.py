# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author :
#    @Create Time   : 2024/6/12 23:27
#    @Description   : 
#
# ===============================================================

res = 0
def diameter_of_binary_tree(root):
    """
    子函数定义：返回子树的最大深度
    :param root:
    :return:
    """
    def traverse(root):
        if not root:
            return 0

        left_max = traverse(root.left)
        right_max = traverse(root.right)

        # 更新结果
        global res
        res = max(res, left_max + right_max)

        return 1 + max(left_max, right_max)
