# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author :
#    @Create Time   : 2023/11/15 16:36
#    @Description   : 判断链表是否包含环
#
# ===============================================================


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

def has_cycle(head):
    """
    使用快慢指针，快指针是慢指针的两倍速，若双指针相遇，则有环
    :param head: 链表
    :return: True or False
    """
    if not head:
        return

    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False

