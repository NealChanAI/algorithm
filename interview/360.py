# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author : 
#    @Create Time   : 2025/9/10 19:00
#    @Description   : 
#
# ===============================================================


"""
搜索推荐场景： query=淘宝 item_list=[淘宝网首页官网，淘宝网登录入口，淘宝读书，淘宝官网入口，淘宝闪送] item_score=[0.9，0.8，0.7，0.6，0.5]
1. 构造相似度函数，实现字符级别相似度计算，提示：动态规划 举例：sim(淘宝, 淘宝读书)=0.5
2. 根据mmr算法实现重排，提示：mmr_score = max(λ * sim(item_i, query) - (1 - λ) * sim(item_i, item_j))
"""


class Solution:
    def sim(self, s1, s2):
        """
        编辑距离
        """
        if not s1 or not s2:
            return 0

        def dp(i, j):
            if i < 0:
                return j + 1
            if j < 0:
                return i + 1
            if s1[i] == s2[j]:
                return dp(i-1, j-1)

            return 1 + min(
                dp(i-1, j),
                dp(i-1, j-1),
                dp(i, j-1)
            )

        _res = dp(len(s1)-1, len(s2)-1)
        return 1/_res if _res != 0 else 0

    def mmr(self, query, item_lst, lambd):
        """
        query: 搜索词
        item_lst: item列表
        mmr_score = max(λ * sim(item_i, query) - (1 - λ) * sim(item_i, item_j))
        """
        # 非空判断
        if not query or not item_lst:
            return []
        res = []  # 存储最终结果

        seq = [item_lst[0]]

        # 循环迭代
        while len(seq) < len(item_lst):
            idx = len(seq)
            min_val = float('inf')
            for i in range(idx):
                items_sim = (1 - lambd) * self.sim(item_lst[idx], item_lst[i])
                min_val = min(min_val, items_sim)
            mmr_score = lambd * self.sim(query, item_lst[idx]) - min_val
            res.append(mmr_score)
            seq.append(item_lst[idx])

        res.sort()
        return res


if __name__ == '__main__':
    a = Solution()
    s1 = '淘宝'
    s2 = '淘宝读书'
    # s2 = '淘宝'
    res = a.sim(s1, s2)
    print(res)

    query = '淘宝'
    item_list = ['淘宝网首页官网', '淘宝网登录入口', '淘宝读书', '淘宝官网入口', '淘宝闪送']
    l = 0.8
    mmr_lst = a.mmr(query, item_list, l)
    print(mmr_lst)
