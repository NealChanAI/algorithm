# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author :
#    @Create Time   : 2024/6/30 23:18
#    @Description   : 110. 平衡二叉树
#
# ===============================================================


class Sollution:
    def __init__(self):
        self.res = True

    def isBalanced(self, root):
        """
        递归子函数：返回子树的最大深度
        :param root:
        :return:
        """
        def traverse(root):
            if not root:
                return 0

            left = traverse(root.left)
            right = traverse(root.right)

            if left - right > 1 or right - left > 1:
                self.res = False

            return max(left, right) + 1

        traverse(root)
        return self.res
