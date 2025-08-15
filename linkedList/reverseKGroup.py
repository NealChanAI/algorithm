# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author :
#    @Create Time   : 2024/6/15 21:37
#    @Description   : 25. K个一组反转链表
#
# ===============================================================

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def reverse_k_group(self, head, k):
        """
        递归：
        1. base case: 链表长度小于k，返回子链表的头结点
        2. 函数定义：返回已做好K个一组反转链表的头结点
        3. 反转链表的前b个结点
        :param head:
        :param k:
        :return:
        """
        if not head:
            return

        def reverse_top_n(node, node_b):
            pre, cur = None, node
            while cur != node_b:
                next = cur.next
                cur.next = pre
                pre = cur
                cur = next
            return pre

        a, b = head, head
        for _ in range(k):
            if not b:
                return head
            b = b.next

        new_head = reverse_top_n(a, b)
        a.next = self.reverse_k_group(b, k)
        return new_head


