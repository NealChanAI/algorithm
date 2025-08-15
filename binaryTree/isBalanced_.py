# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author :
#    @Create Time   : 2024/7/1 17:04
#    @Description   : 
#
# ===============================================================


class Solution:
    def isBalanced(self, root):
        """
        递归子函数定义：返回左右子树的最大深度
        base case: 节点为none，返回0
        :param root:
        :return:
        """
        res = True

        def is_balanced_helper(root):
            if not root:
                return 0

            left = is_balanced_helper(root.left)
            right = is_balanced_helper(root.right)

            # 更新结果
            global res
            if left - right > 1 or right - left > 1:
                res = False

            return max(left, right) + 1

        is_balanced_helper(root)
        return res


