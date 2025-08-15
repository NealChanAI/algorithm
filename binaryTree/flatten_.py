# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author :
#    @Create Time   : 2024/7/1 17:54
#    @Description   : 
#
# ===============================================================


class Solution:
    def flatten(self, root):
        if not root:
            return

        self.flatten(root.left)
        self.flatten(root.right)

        left = root.left
        right = root.right

        root.left = None
        root.right = left
        p = root
        while p and p.right:
            p = p.right
        p.right = right
