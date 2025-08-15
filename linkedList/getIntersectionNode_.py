# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author :
#    @Create Time   : 2024/6/15 10:10
#    @Description   : 160. 相交链表
#
# ===============================================================

class ListNode:
    def __int__(self, val):
        self.val = val
        self.next

class Solution:
    def getIntersectionNode(self, head1, head2):
        """
        双指针
        0. 非空判断
        1. 双指针分别从两条链表的head节点开始遍历
        2. 若遍历完，则接着另一条链表开始遍历
        3. 直到找到相同的节点为止
        :param head1:
        :param head2:
        :return:
        """
        if not head1 or not head2:
            return

        while p1 != p2:
            if not p1:
                p1.next = head2
            else:
                p1 = p1.next

            if not p2:
                p2.next = head1
            else:
                p2 = p2.next

        return
