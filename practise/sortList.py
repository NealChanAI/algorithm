# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Time   : 2024/8/18 09:29
#    @Description   : 
#
# ===============================================================


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def sortList(self, head):
        """
        排序链表
            递归子函数定义：返回已经排好序的子链表，将head结点插入到合适的位置中
            base case: 子链表长度为0或1时，直接返回子链表

        """
        # base case
        if not head or not head.next:
            return head

        def _insert_listnode(node, sub_head):
            """将结点插入到已经排好序的链表中，返回排好序的新链表的头节点"""
            if not node or not sub_head:
                return

            dummy = ListNode(-1)
            dummy.next = sub_head
            pre, cur = dummy, sub_head
            while cur and cur.val <= node.val:
                next = cur.next
                pre = cur
                cur = next
            pre.next = node
            node.next = cur
            return dummy.next

        new_head = self.sortList(head.next)
        return _insert_listnode(head, new_head)






