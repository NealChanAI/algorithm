# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author :
#    @Create Time   : 2024/6/27 21:58
#    @Description   : 给你单链表的头指针 head 和两个整数 left 和 right ，其中 left <= right 。请你反转从位置 left 到位置 right 的链表节点，返回 反转后的链表 。
#
# ===============================================================

class ListNode:
    def __init__(self, val):
        self.val = val

class Solution:
    def _reverse(self, a):
        if not a:
            return
        pre, cur = None, a
        while cur:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
        return pre

    def reverseBetween(self, head, left, right):
        """
        1. 双指针分别走到left-1和right的位置，记住right+1的节点
        2. 对left到right的节点进行翻转
        3. 对三段链表进行拼接
        :param head:
        :param left:
        :param right:
        :return:
        """
        # 非空判断
        if not head or left < 0 or right < 0:
            return

        dummy = ListNode(-1)
        dummy.next = head
        p1, p2 = dummy, dummy

        for _ in range(left-1):
            p1 = p1.next

        for _ in range(right):
            p2 = p2.next

        p2_end = p1.next
        p3 = p2.next
        p2.next = None

        sec_p = self._reverse(p1.next)
        p1.next = sec_p
        p2_end.next = p3

        return dummy.next






