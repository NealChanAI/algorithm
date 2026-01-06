"""
给你一个无重复元素的整数数组 candidates 和一个目标和 target，
找出 candidates 中可以使数字和为目标数 target 的所有组合。candidates 中的每个数字可以无限制重复被选取。
"""


class Solution:
    def __init__(self):
        self.res = []
        self.path = []
        self.sum = 0

    def combinationSum(self, nums, target):
        """
        backTrack
        """
        self._combination_sum_helper(nums, 0, target)
        return self.res

    def _combination_sum_helper(self, nums, start, target):

        if self.sum == target:
            self.res.append(self.path.copy())
            return

        if self.sum > target:
            return

        for i in range(start, len(nums)):
            self.path.append(nums[i])
            self.sum += nums[i]
            self._combination_sum_helper(nums, i, target)
            self.sum -= nums[i]
            self.path.pop()


if __name__ == '__main__':
    a = Solution()
    target = 5
    candidates = [1, 2, 3]

    print(a.combinationSum(candidates, target))