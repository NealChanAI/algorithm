"""
给定一个已排序的链表的头 head ， 删除所有重复的元素，使每个元素只出现一次 。返回 已排序的链表 。
"""


class ListNode:
    def __int__(self, val):
        self.val = val
        self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        快慢指针
        """
        if not head:
            return head

        s, f = head, head

        while f:
            if s.val != f.val:
                s.next = f
                s = s.next
            f = f.next
        s.next = None

        return head


