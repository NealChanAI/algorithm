# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author :
#    @Create Time   : 2024/6/15 22:31
#    @Description   : 234. 回文链表
#
# ===============================================================

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def is_palindrome(self, head):
        if not head:
            return

        lst = []
        while head:
            lst.append(head.val)
            head = head.next

        l, r = 0, len(lst) - 1
        while l <= r:
            if lst[l] != lst[r]:
                return False
            l += 1
            r -= 1
        return True
