# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author :
#    @Create Time   : 2024/6/16 00:17
#    @Description   : 24. 两两交换链表中的节点
#
# ===============================================================

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def swapPairs(self, head):
        """
        递归:
            子函数定义：返回交换好的子链表的head节点
            base case: 剩下一个或0个节点
        :param head:
        :return:
        """
        if not head or not head.next:
            return head

        a, b = head, head.next
        new_head = self.swapPairs(head.next.next)
        b.next = a
        a.next = new_head
        return b


