# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Time   : 2024/8/18 10:58
#    @Description   : 
#
# ===============================================================


class Solution:
    def isBalanced(self, root):
        """平衡二叉树"""

        global res
        res = True

        def _is_balanced_helper(root):
            if not root:
                return 0

            left = _is_balanced_helper(root.left)
            right = _is_balanced_helper(root.right)

            global res
            if left - right > 1 or right - left > 1:
                res = False

            return 1 + max(left, right)

        _is_balanced_helper(root)
        return res

