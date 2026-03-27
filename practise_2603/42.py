# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author : 
#    @Create Time   : 2026-03-27 12:49
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
        每个柱子能接到最多的水等于min(左柱最高, 右柱最高) - 柱子高度
        """

        res = 0

        for i in range(1, len(height)):
            # 遍历查看左边柱子最高的
            l_max = 0
            for l in range(i+1):
                l_max = max(l_max, height[l])

            # 遍历查看右边柱子最高的
            r_max = 0
            for r in range(i, len(height)):
                r_max = max(r_max, height[r])

            res += min(l_max, r_max) - height[i]

        return res


if __name__ == '__main__':
    a = Solution()
    height = [4,2,0,3,2,5]
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]

    print(a.trap(height))
