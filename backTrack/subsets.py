# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author :
#    @Create Time   : 2024/6/14 21:41
#    @Description   : 78. 子集
#
# ===============================================================


def subsets(nums):
    """
    回溯算法
    1. 路径、选择、结束条件
    :param nums:
    :return:
    """
    if not nums:
        return

    res = []
    track = []

    def back_track(nums, start):
        # 添加
        global res, track
        res.append(list(track))

        for i in range(start, len(nums)):
            track.append(nums[i])
            back_track(nums, i+1)
            track.pop()

    back_track(nums, 0)
    return res





