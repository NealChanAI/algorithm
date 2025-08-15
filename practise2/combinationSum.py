

class Solution:
    def __init__(self):
        self.res = []
        # 记录回溯的路径
        self.track = []
        # 记录track中的路径和
        self.track_sum = 0

    def combinationSum(self, candidates, target):
        if len(candidates) == 0:
            return self.res
        self.back_track(candidates, 0, target)
        return self.res

    def back_track(self, nums, start, target):
        # base case, 找到目标和，记录结果
        if self.track_sum == target:
            self.res.append(list(self.track))
            return

        # base case，超过目标和，停止向下遍历
        if self.track_sum > target:
            return

        # 回溯算法标准框架
        for i in range(start, len(nums)):
            # 选择nums[i]
            self.track_sum += nums[i]
            self.track.append(nums[i])
            # 递归遍历下一层回溯树
            # 同一元素可重复使用，注意参数
            self.back_track(nums, i, target)
            # 撤销选择 nums[i]
            self.track_sum -= nums[i]
            self.track.pop()