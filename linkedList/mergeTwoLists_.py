# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author :
#    @Create Time   : 2023/11/15 14:52
#    @Description   : 合并连个有序链表
#
# ===============================================================

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def merge_two_lists(l1, l2):
    """

    :param l1:
    :param l2:
    :return:
    """
    dummy = ListNode(-1)
    p = dummy
    p1, p2 = l1, l2

    while p1 and p2:
        if p1.val > p2:
            p = p2
            p2 = p2.next
        else:
            p = p1
            p1 = p1.next

        tmp = p.next
        p.next = None
        p = tmp

    if p1:
        p.next = p1
    if p2:
        p.next = p2

    return dummy.next

