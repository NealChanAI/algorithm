# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author :
#    @Create Time   : 2025-09-01 18:17
#    @Description   : #234
#
# ===============================================================


"""
给你一个单链表的头节点 head ，请你判断该链表是否为回文链表。如果是，返回 true ；否则，返回 false 。
"""


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def isPalindrome(self, head):
        """
        存储到list中, 然后双指针
        """
        if not head:
            return

        lst = []
        while head:
            lst.append(head.val)
            head = head.next

        l, r = 0, len(lst)-1
        while l < r:
            if lst[l] != lst[r]:
                return False
            l += 1
            r -= 1
        return True

