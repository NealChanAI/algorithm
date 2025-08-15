# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Time   : 2024/8/17 17:15
#    @Description   : 
#
# ===============================================================


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def reverseKGroup(self, head, k):
        """
        递归：
            子函数定义：返回已经翻转好的子链表，将前K个元素反转好后拼接起来
            base case: 子链表长度不足K
        :param head:
        :param k:
        :return:
        """
        if not head:
            return

        # dummy = ListNode(-1)
        # dummy.next = head

        a, b = head, head
        # base case
        for _ in range(k):
            if a:
                a = a.next
            else:
                return head

        def _reverse_between(node_a, node_b):
            """翻转两个节点之间的链表"""
            pre, cur = None, node_a
            while cur != node_b:
                next = cur.next
                cur.next = pre
                pre = cur
                cur = next
            return pre

        tail_node = _reverse_between(b, a)
        sub_list_node = self.reverseKGroup(a, k)
        b.next = sub_list_node
        return tail_node








