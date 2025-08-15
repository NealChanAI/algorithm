# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author :
#    @Create Time   : 2024/6/27 17:57
#    @Description   : 230. 二叉搜索树中的第K小的元素
#
# ===============================================================


class Solution:
    def __init__(self):
        self.res = 0
        self.rank = 0

    def kthSmallest(self, root, k):
        """
        第K小的元素
        中序遍历
        :param root:
        :param k:
        :return:
        """
        if not root:
            return

        def traverse(root, k):
            if not root:
                return

            traverse(root.left, k)
            self.rank += 1
            if self.rank == k:
                self.res = root.val
                return
            traverse(root.right, k)

        traverse(root, k)
        return self.res



