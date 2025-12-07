# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author : 
#    @Create Time   : 2025/12/7 20:09
#    @Description   : 
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
        2. 快慢指针
        """
        if not head:
            return

        # 定义虚拟头节点
        dummy = ListNode(-1)
        dummy.next = head
        s, f = dummy, head

        while f:
            if f.next and f.val == f.next.val:
                while f.next and f.val == f.next.val:
                    f = f.next
                f = f.next

                if not f:
                    s.next = f
            else:
                s.next = f
                s = s.next
                f = f.next

        return dummy.next
