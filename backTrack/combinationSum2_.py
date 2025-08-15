# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author :
#    @Create Time   : 2024/7/17 23:05
#    @Description   : 
#
# ===============================================================


class Solution:
    def __init__(self):
        self.res = []
        self.sum = 0
        self.path = []

    def combinationSum2(self, candidates, target):
        """
        back track algo

        :param candidates:
        :param target:
        :return:
        """
        if not candidates:
            return

        candidates.sort()
        self.back_track(candidates, 0, target)
        return self.res

    def back_track(self, candidates, start, target):

        # 判断数值大小
        if self.sum > target:
            return

        if self.sum == target:
            self.res.append(self.path.copy())
            return

        for i in range(start, len(candidates)):
            # 判断是否与前一个数相同
            if i > start and candidates[i] == candidates[i - 1]:
                continue

            # 添加节点
            self.path.append(candidates[i])
            self.sum += candidates[i]

            # 递归
            self.back_track(candidates, i + 1, target)

            # 剔除节点
            self.path.pop()
            self.sum -= candidates[i]


if __name__ == '__main__':
    nums = [10,1,2,7,6,1,5]
    print(Solution().combinationSum2(nums, 8))





