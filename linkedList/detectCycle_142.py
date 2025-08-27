# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author :
#    @Create Time   : 2025-08-27 16:10
#    @Description   : #142
#
# ===============================================================


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def detect_cycle(self, head):
        """
        1. 非空判断
        2. 快慢指针
        3. 相遇时, 让快指针从起点开始走, 再次相遇时即可
        """
        if not head:
            return

        s, f = head, head

        while f and f.next:
            f = f.next.next
            s = s.next

            if s == f:
                f = head
                while s != f:
                    s = s.next
                    f = f.next
                return s
        return False
