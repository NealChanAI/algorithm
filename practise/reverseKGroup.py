# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Time   : 2024/7/16 17:52
#    @Description   : 
#
# ===============================================================


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head, k):
        """
        递归：
           1. 函数定义：返回已经排好序子链表，将前K个链表进行翻转后，拼接子链表
           2. base case: 子链表长度小于K，则直接返回子链表
        :param head:
        :return:
        """

        if not head:
            return

        def reverse_head_k(node_a, node_b):
            """
            翻转链表
            :param node_a:
            :param node_b:
            :return:
            """
            pre, cur = None, node_a
            while cur != node_b:
                next = cur.next
                cur.next = pre
                pre = cur
                cur = next
            return pre

        a, b = head, head
        for i in range(k):
            if not b:
                return head
            b = b.next

        # 翻转头k个结点
        new_head = reverse_head_k(a, b)
        a.next = self.reverseKGroup(b, k)

        return new_head

