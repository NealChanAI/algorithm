"""
给你一个整数数组 nums，请你将该数组升序排列。

你必须在 不使用任何内置函数 的情况下解决问题，时间复杂度为 O(nlog(n))，并且空间复杂度尽可能小。
"""


class Solution:
    def sortArray(self, nums):
        """
        归并排序
        """
        if not nums:
            return

        return self._helper(nums, 0, len(nums) - 1)

    def _helper(self, nums, l, r):
        if l == r:
            return [nums[l]]

        if l > r:
            return []

        mid = l + (r - l) // 2
        left = self._helper(nums, l, mid)
        right = self._helper(nums, mid+1, r)

        return self.merge(left, right)

    def merge(self, lst1, lst2):
        """合并两个升序数组"""
        if not lst1 and not lst2:
            return []

        p1, p2 = 0, 0
        res = []
        while p1 < len(lst1) and p2 < len(lst2):
            if lst1[p1] <= lst2[p2]:
                res.append(lst1[p1])
                p1 += 1
            else:
                res.append(lst2[p2])
                p2 += 1

        if p1 < len(lst1):
            res.extend(lst1[p1:])

        if p2 < len(lst2):
            res.extend(lst2[p2:])

        return res


if __name__ == '__main__':
    a = Solution()
    nums = [5, 2, 3, 1]

    nums = [5,1,1,2,0,0]
    print(a.sortArray(nums))
