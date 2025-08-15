

class Solution:
    def __init__(self):
        self.res = []

    # 主函数，输入一组不重复的数字，返回它们的全排列
    def permute(self, nums):
        # 记录「路径」
        track = []
        # 「路径」中的元素会被标记位true, 避免重复使用
        used = [False] * len(nums)

        self.back_track(nums, track, used)

        return self.res

    # 路径：记录在track中
    # 选择列表：nums中不存在于track的那些元素（used[i]为false）
    # 结束条件：nums中的元素全都在track中出现
    def back_track(self, nums, track, used):
        # 触发结束条件
        if len(track) == len(nums):
            self.res.append(track.copy())
            return

        for i in range(len(nums)):
            # 排除不合法的选择
            if used[i]:
                # nums[i]已经在track中，跳过
                continue
            # 做选择
            track.append(nums[i])
            used[i] = True
            # 进入下一层决策树
            self.back_track(nums, track, used)
            # 取消选择
            track.pop()
            used[i] = False