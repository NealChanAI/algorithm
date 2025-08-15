# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author :
#    @Create Time   : 2023/11/15 16:26
#    @Description   : 单链表的中间节点
#
# ===============================================================

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

def middle_node(head):
    # 快慢指针初始化指向 head
    slow = head
    fast = head

    # 快指针走到末尾时停止
    while fast and fast.next:
        # 慢指针走一步，快指针走两步
        slow = slow.next
        fast = fast.next.next
    # 慢指针指向中点
    return slow