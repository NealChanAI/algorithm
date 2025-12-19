# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author : 
#    @Create Time   : 2025-12-19 18:09
#    @Description   : 
#
# ===============================================================


"""
给你一个单链表的头节点 head ，请你判断该链表是否为回文链表。如果是，返回 true ；否则，返回 false 。
"""


class Solution:
    def isPalindrome(self, head):
        """
        连转成列表, 然后再判断
        """
        lst = []
        while head:
            lst.append(head.val)
            head = head.next

        l, r = 0, len(lst) - 1
        while l < r:
            if lst[l] != lst[r]:
                return False
            l += 1
            r -= 1

        return True