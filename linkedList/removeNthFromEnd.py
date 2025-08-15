# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author :
#    @Create Time   : 2024/6/7 11:42
#    @Description   : 
#
# ===============================================================

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def remove_nth_from_end(head, k):
    """
    快慢指针
    :param head:
    :param k:
    :return:
    """
    if not head:
        return

    dummy = ListNode(-1)
    dummy.next = head

    f, s = dummy, dummy

    for i in range(k):
        if not f.next:
            return
        f = f.next

    while f and f.next:
        f = f.next.next
        s = s.next

    s.next = s.next.next

    return dummy.next
