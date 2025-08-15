# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author :
#    @Create Time   : 2024/6/15 10:53
#    @Description   : 
#
# ===============================================================

class ListNode:
    def __int__(self, val):
        self.val = val
        self.next = None

class Solution:
    def mergeTwoLists(self, list1, list2):
        """
        双指针
        :param list1:
        :param list2:
        :return:
        """
        if not list1 and not list2:
            return

        dummy = ListNode(-1)
        p = dummy
        p1, p2 = list1, list2
        while p1 and p2:
            if p1.val >= p2.val:
                p.next = p2
                p2 = p2.next
            else:
                p.next = p1
                p1 = p1.next

            tmp = p.next
            tmp.next = None
            p = tmp

        if p1:
            p.next = p1
        if p2:
            p.next = p2

        return dummy.next


