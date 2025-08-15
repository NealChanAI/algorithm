# -*- coding: utf-8 -*-
# ===============================================================
# ===============================================================


class Solution:
    def merge(self, intervals):
        """
        1. 对数组按照首元素进行排序
        :param intervals:
        :return:
        """
        if not intervals:
            return

        intervals.sort(key=lambda x: x[0])
        res = [intervals[0]]

        for interval in intervals[1:]:
            last = res[-1]
            if interval[0] <= last[1]:
                last[1] = max(last[1], interval[1])
            else:
                res.append(interval)

        return res


