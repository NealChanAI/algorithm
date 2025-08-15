# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author :
#    @Create Time   : 2024/6/14 16:25
#    @Description   : 46. 全排列 给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。
#
# ===============================================================


def permute(nums):
    """
    回溯-暴力穷举
    1.
    :param nums:
    :return:
    """
    if not nums:
        return

    track = []
    used = [False] * len(nums)
    res = []

    def back_track(nums, track, used):
        if len(track) == len(nums):
            global res
            res.append(track.copy())
            return

        for i in range(len(nums)):
            if used[i]:
                continue

            used[i] = True
            track.append(nums[i])

            back_track(nums, track, used)

            used[i] = False
            track.pop()

    return back_track(nums, track, used)
