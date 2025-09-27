# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author : 
#    @Create Time   : 2025/9/22 18:59
#    @Description   : 
#
# ===============================================================


"""
banner, 有两个属性，int level, double weight, level的取值有1～4，weight没有限制
    输入是banner的list，作一个rerank的函数，
        1. 所有level 1的排在前面
        2. 所有level 4的排在最后面
        3. 所有level2和level3中的banner top2，

"""


class Solution:
    def rarank(self, banner_lst):
        """
        1. 非空判断
        2. 遍历一遍
            获取level1和level4的banner
            获取level2或level3的前两个
        3. 组合
        """
        if not banner_lst:
            return

        level1, level4 = [], []
        level_mid = []

        for i, banner in enumerate(banner_lst):
            level, weight = banner
            # level1
            if level == '1':
                level1.append(banner)
            elif level == '4':
                level4.append(banner)
            else:
                level_mid.append(banner)

        level1_sorted = sorted(level1, key=lambda x: x[1][1])
        level4_sorted = sorted(level1, key=lambda x: x[1][1])

        min = -float('inf')
        max_idx = -1
        for i in range(len(level_mid)):
            if level_mid[i][1] > min:
                min = level_mid[i][1]
                max_idx = i
        level_mid_top = level_mid.pop(max_idx)

        min = -float('inf')
        max_idx = -1
        for i in range(len(level_mid)):
            if level_mid[i][1] > min:
                min = level_mid[i][1]
                max_idx = i
        level_mid_sec_top = level_mid.pop(max_idx)

        return level1_sorted + [level_mid_top, level_mid_sec_top] + level4_sorted




