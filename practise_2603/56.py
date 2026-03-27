# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author : 
#    @Create Time   : 2026-03-27 12:49
#    @Description   : 
#
# ===============================================================


"""
以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [start_i, end_i] 。
请你合并所有重叠的区间，并返回 一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间 。
"""


class Solution:
    def merge(self, intervals):
        """先排序, 再遍历"""
        sorted_intervals = sorted(intervals, key=lambda x: x[0])

        res = []
        res.append(sorted_intervals[0])

        end = sorted_intervals[0][1]

        for i in range(1, len(sorted_intervals)):
            if sorted_intervals[i][0] > end:
                res.append(sorted_intervals[i])
            else:
                if sorted_intervals[i][1] > end:
                    res[-1][1] = sorted_intervals[i][1]

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
