"""
给你输入一个无重复元素的数组 nums，其中每个元素最多使用一次，请你返回 nums 的所有子集。
"""


class Solution:
    def __init__(self):
        self.path = []
        self.res = []

    def subsets(self, nums):
        """backTrack"""
        self._subsets_helper(nums, 0)
        return self.res

    def _subsets_helper(self, nums, start):
        # base case
        # if len(self.path) > len(nums):
        if start > len(nums):
            return

        # 添加元素
        self.res.append(self.path.copy())

        for i in range(start, len(nums)):
            self.path.append(nums[i])
            self._subsets_helper(nums, i+1)
            self.path.pop()


if __name__ == '__main__':
    a = Solution()
    nums = [1, 2, 3]
    res = a.subsets(nums)
    print(res)