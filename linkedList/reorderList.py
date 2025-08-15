# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author :
#    @Create Time   : 2024/6/15 22:52
#    @Description   : 143. 重排链表
#
# ===============================================================

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def reorder_list(self, head):
        """
        1. 找到链表中点，拆分成两个链表
        2. 对后链表进行反转
        3. 双指针拼接新链表
        :param head:
        :return:
        """
        # 非空判断
        if not head:
            return

        def find_middle(node):
            """返回链表的中点"""
            slow, fast = node, node
            while fast and fast.next:
                fast = fast.next.next
                slow = slow.next
            return slow

        def reverse(node):
            """对链表进行反转"""
            pre, cur = None, node
            while cur:
                next = cur.next
                cur.next = pre
                pre = cur
                cur = next
            return pre

        middle = find_middle(head)
        later_head = reverse(middle.next)
        middle.next = None

        while head and later_head:
            p1 = head.next
            p2 = later_head.next

            head.next = later_head
            later_head.next = p1

            head = p1
            later_head = p2
