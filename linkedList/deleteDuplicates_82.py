# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author :
#    @Create Time   : 2025-09-01 17:44
#    @Description   : #82
#
# ===============================================================


"""
给定一个已排序的链表的头 head ， 删除原始链表中所有重复数字的节点，
只留下不同的数字 。返回 已排序的链表 。
"""


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        1. 非空判断
        2. fast/slow pointers
        """
        # 非空判断
        if not head:
            return

        dummy = ListNode(-1)
        dummy.next = head

        slow, fast = dummy, head
        while fast:
            if fast.next and fast.val == fast.next.val:
                while fast.next and fast.val == fast.next.val:
                    fast = fast.next
                fast = fast.next
            else:
                slow.next = fast
                slow = slow.next
                fast = fast.next
        return dummy.next
