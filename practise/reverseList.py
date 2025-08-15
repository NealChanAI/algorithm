# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Time   : 2024/7/16 17:38
#    @Description   : 
#
# ===============================================================


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def reverseList(self, head):
        """

        :param head:
        :return:
        """
        if not head:
            return head

        pre, cur = None, head
        while cur:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
        return pre
