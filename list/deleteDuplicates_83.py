# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author :
#    @Create Time   : 2025-08-27 17:07
#    @Description   : #83
#
# ===============================================================


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def delete_duplicates(self, head):
        """
        1. 非空判断
        2. 快慢指针
        """
        if not head:
            return

        dummy = ListNode(-1)
        dummy.next = head

        s, f = head, head
        while f:
            if f.val != s.val:
                s.next = f
                s = s.next
            f = f.next
        s.next = None

        return dummy.next

