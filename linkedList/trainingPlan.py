# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author :
#    @Create Time   : 2024/6/15 23:44
#    @Description   : LCR 140
#
# ===============================================================

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def trainingPlan(self, head, cnt):
        """
        给定一个头节点为 head 的链表用于记录一系列核心肌群训练项目编号，请查找并返回倒数第 cnt 个训练项目编号。
        :param head:
        :param cnt:
        :return:
        """
        if not head:
            return

        dummy = ListNode(-1)
        dummy.next = head
        slow, fast = dummy, dummy

        for _ in range(cnt):
            if fast:
                fast = fast.next
            else:
                return []

        while fast:
            fast = fast.next
            slow = slow.next

        return [slow.val]
