# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Time   : 2024/8/19 22:07
#    @Description   : 
#
# ===============================================================


class Solution:
    def minSubArrayLen(self, target, nums):
        """滑动指针"""

        res = float('inf')
        sum = 0
        l, r = 0, 0

        while r < len(nums):
            # 扩大窗口
            c = nums[r]
            r += 1

            sum += c

            # 缩小窗口
            while sum >= target and l < r:
                # 更新结果
                if sum >= target:
                    res = min(res, r - l)

                d = nums[l]
                l += 1
                sum -= d

        return res if res != float('inf') else 0


if __name__ == '__main__':
    target = 7
    nums = [2, 3, 1, 2, 4, 3]
    print(Solution().minSubArrayLen(target, nums))

