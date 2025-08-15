# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author :
#    @Create Time   : 2024/6/6 15:02
#    @Description   :
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

    while l1 and l2:
        if l1.val > l2.val:
            p.next = l2
            l2 = l2.next
        else:
            p.next = l1
            l1 = l1.next
        p = p.next

    if l1:
        p.next = l1
    if l2:
        p.next = l2

    return dummy.next


if __name__ == '__main__':
    pass