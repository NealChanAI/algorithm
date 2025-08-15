# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Time   : 2024/8/17 16:56
#    @Description   : 
#
# ===============================================================


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def reverseBetween(self, head, left, right):
        """
        反转链表
        1. 先找到left, right两个节点
        2.
        :param head:
        :param left:
        :param right:
        :return:
        """
        if not head:
            return

        def _reverse(node_a, node_b):
            pre, cur = None, node_a
            while cur != node_b:
                next = cur.next
                cur.next = pre
                pre = cur
                cur = next
            return pre

        dummy = ListNode(-1)
        dummy.next = head
        p = dummy

        for i in range(left-1):
            p = p.next
        first_tail = p  # left节点的前一个节点
        node_a = p.next # left节点
        for i in range(right - left + 1):
            p = p.next
        node_b = p  # right节点
        third_head = node_b.next

        # 反转中间链表
        second_head = _reverse(node_a, third_head)

        # 将三段拼接起来
        first_tail.next = second_head
        node_a.next = third_head

        return dummy.next






