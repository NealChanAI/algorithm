# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author :
#    @Create Time   : 2024/6/7 10:32
#    @Description   : 141. 环形链表
#
# ===============================================================

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class Sollution:
    def has_cycle(self, head):
        """
        快慢指针
        0. 非空判断
        1. 快慢指针同时从head节点运动，快指针每次走两部，慢指针每次走一步
        2. 若快指针指向null，则没有环；若快慢指针相遇，则有环
        :param head:
        :return:
        """
        if not head:
            return

        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False
