# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author :
#    @Create Time   : 2025-08-27 14:45
#    @Description   : #23
#
# ===============================================================


"""
给你一个链表数组，每个链表都已经按升序排列。

请你将所有链表合并到一个升序链表中，返回合并后的链表。
"""

import heapq


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists):
        """
        heapq最小堆获取几个list中的最小节点
        """
        if not lists:
            return

        # 定义ListNode的大小比较方式
        ListNode.__lt__ = lambda a, b: a.val < b.val

        pq = []
        for head in lists:
            if not head:
                continue
            heapq.heappush(pq, head)

        dummy = ListNode(-1)
        p = dummy

        while pq:
            node = heapq.heappop(pq)
            p.next = node

            if node.next:
                heapq.heappush(pq, node.next)

            p = p.next

        return dummy.next


import heapq


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        类似于合并两个升序列表，多个指针指向多个链表，使用优先级队列来获取最小值以及对应的链表
        :param lists:
        :return:
        """
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

        pq = []
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
                heapq.heappush(pq, small_node.next)

            p.next = small_node
            tmp = p.next
            tmp.next = None
            p = tmp

        return dummy.next
