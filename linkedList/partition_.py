# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author :
#    @Create Time   : 2024/6/6 15:32
#    @Description   : 
#
# ===============================================================


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = next

def partition(head, x):
    """

    :param head:
    :param x:
    :return:
    """
    dummy1 = ListNode(-1)
    dummy2 = ListNode(-1)
    p1 = dummy1
    p2 = dummy2

    while head:
        if head.val >= x:
            p2.next = head
            p2 = p2.next
        else:
            p1.next = head
            p1 = p1.next

        tmp = head.next
        head.next = None
        head = tmp

    p1.next = dummy2.next

    return dummy1.next