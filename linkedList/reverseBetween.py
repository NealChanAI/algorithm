# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author :
#    @Create Time   : 2024/6/15 20:25
#    @Description   : 92. 反转链表
#
# ===============================================================

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class Sollution:
    def reverseBetween(self, head, left, right):
        """
        迭代思路
        1. 双指针分别指向left-1、right+1的结点
        2. 记住left和right结点，让left到right这段链表断开
        3. 对left到right这段链表反转
        4. 将三段链表连接起来
        :param head:
        :param left:
        :param right:
        :return:
        """
        if not head:
            return

        def reverse(node):
            if not node or not node.next:
                return node
            _pre, cur = None, node
            while cur:
                next = cur.next
                cur.next = pre
                pre = cur
                cur = next
            return pre

        dummy = ListNode(-1)
        dummy.next = head

        pre, succ = dummy, dummy
        for _ in range(left - 1):
            pre = pre.next

        for _ in range(right):
            succ = succ.next  # right_p

        third_p = succ.next  # 有可能是None
        left_p = pre.next

        # 断开连接
        succ.next = None
        pre.next = None

        #
        sub_head = reverse(left_p)
        pre.next = sub_head
        succ.next = third_p

        return dummy.next
