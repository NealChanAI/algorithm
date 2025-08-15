# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Time   : 2024/8/18 11:48
#    @Description   : 
#
# ===============================================================


class Solution:
    def invertTree(self, root):
        if not root:
            return

        root.left = self.invertTree(root.left)
        root.right = self.invertTree(root.left)

        return root
