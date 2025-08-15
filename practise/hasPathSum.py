# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Time   : 2024/8/18 11:29
#    @Description   : 
#
# ===============================================================


class Solution:
    def hasPathSum(self, root, targetSum):
        """

        :param root:
        :param targetSum:
        :return:
        """

        if not root:
            return False

        # base case
        if not root.left and not root.right:
            return root.val == targetSum

        return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)
