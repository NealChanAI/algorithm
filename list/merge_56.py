# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author : 
#    @Create Time   : 2025/9/8 21:37
#    @Description   : #56
#
# ===============================================================


"""
以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi] 。
请你合并所有重叠的区间，并返回 一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间 。
"""


class Solution:
    def merge(self, intervals):
        """

        """
        if not intervals:
            return

        res = []
        nums = sorted(intervals, key=lambda x: x[0])
        if len(nums) == 1:
            return nums
        start, end = nums[0][0], nums[0][1]
        for i in range(1, len(nums)):
            if nums[i][0] <= end:
                end = max(nums[i][1], end)
            else:
                res.append([start, end])
                start = nums[i][0]
                end = nums[i][1]
        # if start <= res[-1][1]:
        res.append([start, end])

        return res


if __name__ == '__main__':
    intervals = [[1,3],[2,6],[8,10],[15,18]]
    intervals = [[1,4],[2,3]]
    res = Solution().merge(intervals)
    print(res)