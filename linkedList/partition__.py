# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author :
#    @Create Time   : 2024/6/15 11:26
#    @Description   : 86. 分隔链表
#
# ===============================================================

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def partition(self, head, x):
        """
        使用大小两个链表以及一个指针
        :param head:
        :param x:
        :return:
        """
        if not head:
            return

        dummy1 = ListNode(-1)
        dummy2 = ListNode(-1)
        p1, p2 = dummy1, dummy2

        while head:
            if head.val < x:
                p1.next = head
                p1 = p1.next
            else:
                p2.next = head
                p2 = p2.next

            tmp = head.next
            head.next = None
            head = tmp

        p1.next = dummy2.next
        return dummy1.next

