# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Time   : 2024/8/18 10:20
#    @Description   : 
#
# ===============================================================


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def trainingPlan(self, head, cnt):
        """链表的倒数第K个结点，快慢指针"""
        if not head or cnt <= 0:
            return

        dummy = ListNode(-1)
        dummy.next = head
        slow, fast = dummy, dummy

        for _ in range(cnt):
            if fast:
                fast = fast.next
            else:
                return

        while fast:
            fast = fast.next
            slow = slow.next

        return slow

