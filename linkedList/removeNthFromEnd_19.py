# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author :
#    @Create Time   : 2025-08-27 15:36
#    @Description   : #19
#
# ===============================================================


class ListNode:
    def __init__(self, val):
        self.val = val


class Solution:
    def remove_nth_from_end(self, head, n):
        """
        double pointers
        """
        dummy = ListNode(-1)
        dummy.next = head

        l, r = dummy, dummy
        for _ in range(n):
            if not r.next:
                return
            r = r.next

        while r and r.next:
            l = l.next
            r = r.next
        l.next = l.next.next

        return dummy.next
