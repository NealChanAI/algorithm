# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Time   : 2024/8/19 09:57
#    @Description   : 
#
# ===============================================================


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        """

        :param l1:
        :param l2:
        :return:
        """
        carry = 0
        dummy = ListNode(-1)
        p = dummy

        while l1 or l2:
            n1 = l1.val if l1 else 0
            n2 = l2.val if l2 else 0
            tmp = n1 + n2 + carry
            carry = tmp // 10
            p.next = ListNode(tmp % 10)
            p = p.next
            l1 = l1.next if l1 else l1
            l2 = l2.next if l2 else l2
        if carry:
            p.next = ListNode(1)
            p = p.next
        p.next = None
        return dummy.next

