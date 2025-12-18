"""
给定一个已排序的链表的头 head ， 删除原始链表中所有重复数字的节点，
只留下不同的数字 。返回 已排序的链表 。
"""


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def deleteDuplicates(self, head):
        """
        左右指针
        """
        if not head:
            return

        dummy = ListNode(-1)
        dummy.next = head
        s, f = dummy, head

        while f:
            if f.next and f.val == f.next.val:
                while f.next and f.val == f.next.val:
                    f = f.next
                f = f.next

                if not f:
                    s.next = None
            else:
                s.next = f
                f = f.next
                s = s.next

        return dummy.next

