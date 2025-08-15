# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author :
#    @Create Time   : 2023/11/15 15:10
#    @Description   : 重新排列两个链表 leetcode86
#
# ===============================================================


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

def partition(head, x):
    """
    将head链表按照x为区分界，拆分成两个链表，最后将两个链表合并即可
    :param head:
    :param x:
    :return:
    """
    dummy1 = ListNode(-1)  # 存储大于等于x的值
    dummy2 = ListNode(-1)  # 存储小于x的值
    p1 = dummy1
    p2 = dummy2
    p = head
    # 遍历原始链表
    while p:
        if p.val >= x:
            p1.next = p
            p1 = p1.next
        else:
            p2.next = p
            p2 = p2.next
        # 不能直接让 p 指针前进，
        # p = p.next
        # 断开原链表中的每个节点的 next 指针
        temp = p.next
        p.next = None
        p = temp

    # 将两个链表合并
    p2.next = dummy1.next

    return dummy2.next



