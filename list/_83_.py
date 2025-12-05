# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author : 
#    @Create Time   : 2025-12-05 18:27
#    @Description   : 
#
# ===============================================================



"""
给定一个已排序的链表的头 head ， 删除所有重复的元素，使每个元素只出现一次 。返回 已排序的链表 。
"""


class ListNode:
    def __int__(self, val):
        self.val = val
        self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        1. 非空判断
        2. 快慢指针
        3. 虚拟头结点
        """

        if not head:
            return head

        dummy = ListNode(-1)
        dummy.next = head

        s, f = head, head

        while f:
            if f.val == s.val:
                f = f.next
            else:
                s.next = f
                s = s.next

        s.next = None

        return dummy.next
