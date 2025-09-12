# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author : 
#    @Create Time   : 2025/9/8 21:05
#    @Description   : #148
#
# ===============================================================


"""
给你链表的头结点 head ，请将其按 升序 排列并返回 排序后的链表 。
"""


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def sortList(self, head):
        """
        递归子函数：
            1. 返回已经排好序的链表，然后将头节点插入到已排好序的链表中
            2. base case：null或只有一个节点，就不需要排序了
        :param head:
        :return:
        """

        def sort_list_helper(head):
            # base case
            if not head:
                return

            if not head.next:
                return head

            # 返回已经排好序的子链表的头结点
            new_head = sort_list_helper(head.next)

            # 将head结点插入到子链表中，使整个链表依然是有序的
            dummy1 = ListNode(-1)
            dummy1.next = new_head
            pre, cur = dummy1, new_head
            while cur and cur.val <= head.val:
                next = cur.next
                pre = cur
                cur = next
            pre.next = head
            head.next = cur
            # print("===" * 10)
            # # self.print_listnode(dummy1.next)
            # print("===" * 10)

            return dummy1.next

        return sort_list_helper(head)