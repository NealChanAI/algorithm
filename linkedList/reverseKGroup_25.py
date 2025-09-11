# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author : chenyongming
#    @Create Time   : 2025-09-01 19:43
#    @Description   : #25
#
# ===============================================================


"""
给你链表的头节点 head ，每 k 个节点一组进行翻转，请你返回修改后的链表。

k 是一个正整数，它的值小于或等于链表的长度。如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。

你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。
"""


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def reverse_top_n(self, node_a, node_b):
        """
        反转前N个节点
        """
        if not node_a and not node_b:
            return node_a

        pre, cur = None, node_a
        while cur != node_b:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next

        return pre

    def reverseKGroup(self, head, k):
        """
        递归思路
        """
        if not head:
            return

        p1, p2 = head, head
        for _ in range(k):
            if not p2:
                return head
            p2 = p2.next

        new_head = self.reverse_top_n(head, p2)
        p1.next = self.reverseKGroup(p2, k)

        return new_head


if __name__ == '__main__':
    lst = [1, 2, 3, 4, 5]
    lst = [1, 2]
    head = ListNode(lst[0])
    node = head
    for i in range(1, len(lst)):
        node.next = ListNode(lst[i])
        node = node.next
    node.next = None

    linked_lst = []
    p = head
    while p:
        linked_lst.append(p.val)
        p = p.next
    print(linked_lst)

    res = Solution().reverseKGroup(head, 2)
    res_lst = []
    while res:
        res_lst.append(res.val)
        res = res.next
    print(res_lst)






