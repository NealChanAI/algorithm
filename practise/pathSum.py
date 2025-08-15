# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Time   : 2024/8/18 16:25
#    @Description   : 
#
# ===============================================================


class Solution:
    def __init__(self):
        self.res = []
        self.track = []
        self.track_sum = 0

    def pathSum(self, root, targetSum):
        """
        回溯算法
        :param root:
        :param targetSum:
        :return:
        """
        if not root:
            return []

        def _back_track(node, target_sum):
            # 非空判断
            if not node:
                return

            self.track.append(node.val)
            self.track_sum += node.val

            # 判断是否叶子结点
            if not node.left and not node.right:
                if self.track_sum == target_sum:
                    self.res.append(self.track.copy())

            _back_track(node.left, target_sum)
            _back_track(node.right, target_sum)

            self.track.pop()
            self.track_sum -= node.val

        _back_track(root, targetSum)
        return self.res




