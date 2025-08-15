# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Time   : 2024/8/17 22:26
#    @Description   : 
#
# ===============================================================


class ListNode:
    def __init__(self, val):
        self.val = val


class Solution:
    def removeNthFromEnd(self, head, k):
        """快慢指针，虚拟头节点"""
        if not head:
            return

        dummy = ListNode(-1)
        dummy.next = head
        slow, fast = dummy, dummy
        for _ in range(k):
            fast = fast.next  # 应该不用做非空判断

        while fast.next:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next

        return dummy.next