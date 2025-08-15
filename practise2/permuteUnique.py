

class Solution:
    def __init__(self):
        self.res = []
        self.track = []
        self.used = []

    def permuteUnique(self, nums):
        # 先排序，让相同的元素靠在一起
        nums.sort()
        self.used = [False] * len(nums)
        self.back_track(nums)
        return self.res

    def back_track(self, nums):
        if len(self.track) == len(nums):
            self.res.append(self.track[:])
            return

        for i in range(len(nums)):
            if self.used[i]:
                continue
            # 新添加的剪枝逻辑，固定相同的元素在排列中的相对位置
            if i > 0 and nums[i] == num[i-1] and not self.used[i-1]:
                continue
            self.track.append(nums[i])
            self.used[i] = True
            self.back_track(nums)
            self.track.pop()
            self.used[i] = False 