# -*- coding: utf-8 -*-
# ===============================================================

#    @Description   : 三数之和
#
# ===============================================================


class Solution:
    def three_sum(self, nums):
        """
        先试试two，然后再遍历处理
        :param nums:
        :return:
        """
        if not nums:
            return

        def two_sum(_nums, target):
            res = []  # 可能会有多个结果
            l, r = 0, len(_nums) - 1
            while l < r:
                _sum = _nums[l] + _nums[r]
                if _sum > target:
                    r -= 1
                elif _sum < target:
                    l += 1
                else:
                    res.append([_nums[l], _nums[r]])
                    while l < r and _nums[l] == _nums[l+1]:
                        l += 1
                    l += 1
                    while l < r and _nums[r] == _nums[r-1]:
                        r -= 1
                    r -= 1
            return res

        fin_res = []
        nums.sort()

        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            tmp_res = two_sum(nums[i+1:], 0 - nums[i])
            for j in tmp_res:
                if j:
                    fin_res.append([nums[i], j[0], j[1]])

        return fin_res


if __name__ == '__main__':
    nums = [-1, 0, 1, 2, -1, -4]
    print(Solution().three_sum(nums))
    print([0] * 3)



