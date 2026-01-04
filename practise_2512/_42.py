# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author : 
#    @Create Time   : 2026-01-04 10:29
#    @Description   : 
#
# ===============================================================


"""
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。

示例 1：



输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
输出：6
解释：上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。
示例 2：

输入：height = [4,2,0,3,2,5]
输出：9
"""


class Solution:
    def trap(self, height):
        """
        暴力搜索
        索引位置i能够装的水为：
            min(左边柱子的最高， 右边柱子的最高) - height[i]
        """

        res = 0
        n = len(height)

        for i in range(1, n):
            left_max, right_max = 0, 0
            for j in range(i+1):
                left_max = max(left_max, height[j])

            for k in range(i, n):
                right_max = max(right_max, height[k])

            res = res + min(left_max, right_max) - height[i]

        return res

    def trap_with_memo(self, height):
        """带备忘录的遍历"""
        res = 0
        n = len(height)

        l_max = [height[0]] * n
        r_max = [height[-1]] * n

        for i in range(1, n):
            l_max[i] = max(l_max[i-1], height[i])

        for j in range(n-2, -1, -1):
            r_max[j] = max(r_max[j+1], height[j])

        for i in range(1, n):
            res = res + min(l_max[i], r_max[i]) - height[i]

        return res


if __name__ == '__main__':
    a = Solution()
    height = [4,2,0,3,2,5]
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]

    print(a.trap(height))

    print('=' * 20)

    print(a.trap_with_memo(height))
