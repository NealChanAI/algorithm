# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Time   : 2024/8/17 17:11
#    @Description   : 
#
# ===============================================================


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def hasCycle(self, head):
        """快慢指针"""
        if not head:
            return

        dummy = ListNode(-1)
        dummy.next = head
        slow, fast = dummy, dummy

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if slow == fast:
                return True

        return False

