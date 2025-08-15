# -*- coding: utf-8 -*-
# ===============================================================
#

#
# ===============================================================


def three_sum(nums):
    """
    穷举法，遍历每个数，转化为twosum问题
    :param nums:
    :return:
    """
    if not nums:
        return

    def two_sum(_nums, target):
        """
        1. 对数组进行排序
        2. 左右指针
        :param _nums:
        :param target:
        :return:
        """
        if not _nums:
            return

        nums.sort()
        left, right = 0, len(_nums)-1
        res = []
        while left < right:
            _sum = _nums[left] + _nums[right]
            a, b = _nums[left], _nums[right]
            if _sum > target:
                while right > left and _nums[right] == b:
                    right -= 1
            elif _sum < target:
                while right > left and _nums[left] == a:
                    left += 1
            else:
                res.append([a, b])
                while right > left and _nums[right] == b:
                    right -= 1
                while right > left and _nums[left] == a:
                    left += 1
        return res

    three_res = []
    nums.sort()
    i = 0
    while i < len(nums) - 2:
        c = nums[i]
        _res = two_sum(nums[i+1:], -c)

        for two_sum_res in _res:
            if two_sum_res:
                three_res.append([c, two_sum_res[0], two_sum_res[1]])
        while i < len(nums) - 2 and nums[i] == c:
            i += 1
    return three_res


if __name__ == '__main__':
    nums = [-1,0,1,2,-1,-4]
    # nums = [0,1,1]
    # nums = [0,0,0]
    print(three_sum(nums))
