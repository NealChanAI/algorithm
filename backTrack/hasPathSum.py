# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author :
#    @Create Time   : 2024/7/17 21:21
#    @Description   : 112. 路径总和
#
# ===============================================================


class Solution:
    def hasPathSum(self, root, targetSum):
        """
        dfs
        :param root:
        :param targetSum:
        :return:
        """
        # 非空判断
        if not root:
            return False
        # base case
        if not root.left and not root.right:
            return root.val == targetSum

        return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)

