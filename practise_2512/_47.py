"""
给你输入一个可包含重复数字的序列 nums，请你写一个算法，返回所有可能的全排列
"""


class Solution:
    def __init__(self):
        self.used = []
        self.res = []
        self.path = []

    def permuteUnique(self, nums):
        """
        构造辅助函数
        """
        if not nums:
            return

        self.used = [False] * len(nums)
        nums.sort()
        self._helper(nums)
        return self.res

    def _helper(self, nums):
        if len(self.path) == len(nums):
            self.res.append(self.path.copy())
            return

        for i in range(len(nums)):
            if self.used[i]:
                continue
            if i > 0 and nums[i] == nums[i-1] and self.used[i-1] is False:
                continue
            self.path.append(nums[i])
            self.used[i] = True
            self._helper(nums)
            self.used[i] = False
            self.path.pop()


if __name__ == '__main__':
    nums = [1, 1, 2]
    a = Solution()
    print(a.permuteUnique(nums))