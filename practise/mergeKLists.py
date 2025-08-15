# -*- coding: utf-8 -*-
# ===============================================================
#
# ===============================================================


import heapq


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def mergeKLists(self, lists):
        """
        合并K个链表:
            使用heapq堆来获取值最小的链表
        :param lists:
        :return:
        """
        # 非空判断
        if not lists:
            return

        # 定义ListNode的大小比较方式
        ListNode.__lt__ = lambda a, b: a.val < b.val

        pq = heapq()
        # 将所有链表存储倒heapq中
        for lst in lists:
            if lst:
                heapq.heappush(pq, lst)

        # 定义虚拟头节点
        dummy = ListNode(-1)
        p = dummy

        while pq:
            small_node = heapq.heappop(pq)

            if small_node.next:
                heapq.heappush(small_node.next)

            p.next = small_node
            tmp = p.next
            tmp.next = None
            p = tmp

        return dummy.next




