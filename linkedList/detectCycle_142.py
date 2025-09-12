# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author :
#    @Create Time   : 2025-08-27 16:10
#    @Description   : #142
#
# ===============================================================


"""
给定一个链表的头节点  head ，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。

如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。 为了表示给定链表中的环，评测系统内部使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。如果 pos 是 -1，则在该链表中没有环。注意：pos 不作为参数进行传递，仅仅是为了标识链表的实际情况。

不允许修改 链表。
"""

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def detectCycle(self, head):
        """
        1. 非空判断
        2. 快慢指针
        3. 相遇时, 让快指针从起点开始走, 再次相遇时即可
        """
        if not head:
            return

        s, f = head, head

        while f and f.next:
            f = f.next.next
            s = s.next

            if s == f:
                f = head
                while s != f:
                    s = s.next
                    f = f.next
                return s
        return
