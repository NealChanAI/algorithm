# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author :
#    @Create Time   : 2023/11/24 10:43
#    @Description   : 
#
# ===============================================================


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def reverse(head):
    """
    定义：输入一个单链表头节点，将该链表反转，返回新的头结点
    :param head:
    :return:
    """
    # base case
    if head.next is None or head.next.next is None:
        return head

    last = reverse(head.next)
    head.next.next = head
    head.next = None
    return last

