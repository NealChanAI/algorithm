# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author :
#    @Create Time   : 2023/11/15 17:08
#    @Description   : 查找链表中环的起点
#
# ===============================================================

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def detect_cycle(head):
    """
    使用快慢双指针，快指针的速度是慢指针的两倍
    :param head:
    :return:
    """
    # 合理性判断
    if not head:
        return

    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        # 当双指针相遇时，
        if slow == fast:
            break

    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next

    return slow