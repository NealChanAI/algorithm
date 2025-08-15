# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Time   : 2024/8/17 16:20
#    @Description   : 
#
# ===============================================================


class Solution:
    def reverseList(self, head):
        """反转链表"""
        if not head:
            return
        pre, cur = None, head
        while cur:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
        return pre