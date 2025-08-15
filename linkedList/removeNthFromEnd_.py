# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author :
#    @Create Time   : 2024/6/6 16:35
#    @Description   : 19. 删除链表的倒数第N个结点
#
# ===============================================================


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def removeNthFromEnd(head, k):
    """
    快慢指针
    1. 非空判断
    2. 定义虚拟头结点
    3. 快慢指针从虚拟头结点出发，快指针先走k步，然后快慢指针同时走；
    4. 当快指针的下一个结点为空时，慢指针进行删除结点操作；
    :param head:
    :param k:
    :return:
    """
    if not head:
        return

    dummy = ListNode(-1)
    dummy.next = head

    fast, slow = dummy, dummy
    for i in range(k):
        if not fast:
            return
        fast = fast.next

    while fast and fast.next:
        slow = slow.next
        fast = fast.next

    slow.next = slow.next.next

    return dummy.next
