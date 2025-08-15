# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author :
#    @Create Time   : 2024/7/18 00:50
#    @Description   : 
#
# ===============================================================


class Solution:
    def __init__(self):
        self.res = float("inf")
        self.depth = 0

    def minDepth(self, root):
        """
        遍历
        :param root:
        :return:
        """
        if not root:
            return 0

        def traverse(root):
            if not root:
                return 0

            self.depth += 1
            if not root.left and not root.right:
                self.res = min(self.res, self.depth)

            traverse(root.left)
            traverse(root.right)

            self.depth -= 1

        traverse(root)
        return self.res
