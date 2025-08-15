# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author :
#    @Create Time   : 2024/6/17 12:31
#    @Description   : 
#
# ===============================================================


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def deleteDuplicates(head):
    if not head:
        return

    dummy = ListNode(-1)
    dummy.next = head
    p1, p2 = head, head
    while p2:
        if p2.val != p1.val:
            p1.next = p2
            p1 = p1.next
        p2 = p2.next
    p1.next = None

    return dummy.next

