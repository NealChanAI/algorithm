# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Time   : 2024/8/17 22:23
#    @Description   : 
#
# ===============================================================


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def deleteDuplicates(self, head):
        """删除排序链表中的重复元素（快慢指针）"""
        if not head:
            return

        dummy = ListNode(-1)
        # dummy.next = head
        slow, fast = dummy, head

        while fast:
            if fast.next and fast.val == fast.next.val:
                while fast.next and fast.val == fast.next.val:
                    fast = fast.next
                fast = fast.next
                if not fast:
                    slow.next = fast
            else:
                slow.next = fast
                slow = slow.next
                fast = fast.next

        return dummy.next








