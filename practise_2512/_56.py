# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author : 
#    @Create Time   : 2025-12-15 16:52
#    @Description   : 
#
# ===============================================================


"""
以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [start_i, end_i] 。
请你合并所有重叠的区间，并返回 一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间 。
"""


class Solution:
    def merge(self, intervals):
        """
        先对数组进行排序
        """

        if not intervals:
            return

        intervals = sorted(intervals, key=lambda x: x[0])

        res = [intervals[0]]
        end = intervals[0][1]

        for i in range(1, len(intervals)):
            head = intervals[i][0]
            tail = intervals[i][1]

            if head <= end:
                res[-1][1] = max(tail, end)
            else:
                res.append(intervals[i])

            end = res[-1][1]

        return res


if __name__ == '__main__':
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    # [[1, 6], [8, 10], [15, 18]]

    intervals = [[1, 4], [4, 5]]
    # 输出：[[1, 5]]

    intervals = [[4, 7], [1, 4]]
    # 输出：[[1, 7]]
    # 解释：区间[1, 4]
    # 和[4, 7]
    # 可被视为重叠区间。

    a = Solution()
    res = a.merge(intervals)
    print(res)
