# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author : 
#    @Create Time   : 2024/6/15 11:49
#    @Description   : 82. 删除链表中的重复元素
#
# ===============================================================

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def deleteDuplicates(self, head):
        """
        双指针
        :param head:
        :return:
        """
        if not head:
            return

        dummy = ListNode(-1)
        slow, fast = dummy, head
        while fast:
            if fast.next and fast.next.val == fast.val:
                while fast.next and fast.next.val == fast.val:
                    fast = fast.next
                fast = fast.next
                if not fast:
                    slow.next = fast
            else:
                slow.next = fast
                slow = slow.next
                fast = fast.next

        return dummy.next


