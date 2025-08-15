

class Solution:
    def __init__(self):
        self.res = []
        # 记录回溯算法的递归路径
        self.track = []

    def subsets(self, nums):
        self.back_track(nums, 0)
        return self.res

    def back_track(self, nums, start):
        # 前序位置，每个节点的值都是一个子集
        self.res.append(list(self.track))

        # 回溯算法标准框架
        for i in range(start, len(nums)):
            # 做选择
            self.track.append(nums[i])
            # 通过start参数控制树枝的遍历，避免产生重复的子集
            self.back_track(nums, i+1)
            # 撤销选择
            self.track.pop()