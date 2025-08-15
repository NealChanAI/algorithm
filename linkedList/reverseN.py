# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author :
#    @Create Time   : 2023/11/24 10:52
#    @Description   : 递归
#
# ===============================================================


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


succesor = None


def reverse_n(head, n):
    """
    定义递归函数：
        定义：对以head开头的n的结点进行反转，并返回反转后的头结点
        反转以 head 为起点的 n 个节点，返回新的头节点

    :param head:
    :return:
    """
    global succesor
    # base case
    if n == 1:
        head.next = succesor
        return head

    last = reverse_n(head.next, n-1)
    head.next.next = head
    head.next = succesor
    return last
