# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Time   : 2024/8/19 20:37
#    @Description   : 
#
# ===============================================================


class Solution:
    def rand10(self):
        """

        :return:
        """
        while True:
            num = (rand7() - 1) * 7 + rand7()  # 等概率生成1， 49范围的随机数
            if nums <= 40:
                return num % 10 + 1
