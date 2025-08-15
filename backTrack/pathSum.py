# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author :
#    @Create Time   : 2024/7/17 21:33
#    @Description   : 113. 路径总和
#
# ===============================================================


class Solution:
    def __init__(self):
        self.path = []
        self.res = []

    def pathSum(self, root, targetSum):
        """
        back_track algo.

        :param root:
        :param targetSum:
        :return:
        """
        if not root:
            return self.res

        def back_track(node, target):
            # 判断非空
            if not node:
                return

            # 添加节点
            self.path.append(node.val)
            target -= node.val

            # 判断是否为叶子结点
            if not node.left and not node.right:
                if target == 0:
                    self.res.append(self.path.copy())
                # return  #  注意：没有return

            # 递归
            back_track(node.left, target)
            back_track(node.right, target)

            # 回溯
            self.path.pop()
            target += node.val

        back_track(root, targetSum)
        return self.res


# for i in range(3):
    xx.append(x)
    back_track()
    pop()

