"""
给你链表的头结点 head ，请将其按 升序 排列并返回 排序后的链表 。
"""


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def sortList(self, head):
        """
        快排
        """
        if not head:
            return

        lst = []
        while head:
            lst.append(head.val)
            head = head.next

        lst.sort()

        dummy = ListNode(-1)
        p = dummy
        for i in range(len(lst)):
            p.next = ListNode(lst[i])

        p.next = None

        return dummy.next
