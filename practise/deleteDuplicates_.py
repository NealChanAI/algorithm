# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Time   : 2024/8/18 11:40
#    @Description   : 
#
# ===============================================================


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def deleteDuplicates(self, head):
        """原地修改"""
        if not head:
            return

        s, f = head, head
        while f:
            if f.val != s.val:
                s.next = f
                s = s.next

            f = f.next
        s.next = None

