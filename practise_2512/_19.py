"""
给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。
"""

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def removeNthFromEnd(self, head, n):
        """快慢指针"""
        if not head:
            return

        dummy = ListNode(-1)
        dummy.next = head

        s, f = dummy, dummy
        for _ in range(n):
            if not f:
                return
            f = f.next

        while f and f.next:
            s = s.next
            f = f.next

        s.next = s.next.next

        return dummy.next

