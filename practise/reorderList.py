# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Time   : 2024/8/17 21:42
#    @Description   : 
#
# ===============================================================


class ListNode:
    def __init__(self, val):
        self.val = val


class Solution:
    def reorderList(self, head):
        """
        1. 找中点
        2. 翻转链表
        3. 合并链表
        :param head:
        :return:
        """
        if not head:
            return

        def _find_middle(node):
            """找链表的中点(快慢指针实现)"""
            if not node:
                return

            slow, fast = node, node
            while fast and fast.next:
                fast = fast.next.next
                slow = slow.next

            return slow

        def _reverse_linkedlist(node):
            """翻转链表"""
            if not node:
                return

            pre, cur = None, node
            while cur:
                next = cur.next
                cur.next = pre
                pre = cur
                cur = next
            return pre

        # 找到链表中点后拆分为两个链表
        middle_node = _find_middle(head)
        second_head = middle_node.next
        middle_node.next = None

        # 翻转第二个链表
        new_second_head = _reverse_linkedlist(second_head)
        # 原地修改两个链表
        while head and new_second_head:
            p1 = head.next
            p2 = new_second_head.next

            head.next = new_second_head
            new_second_head.next = p1

            head = p1
            new_second_head = p2








