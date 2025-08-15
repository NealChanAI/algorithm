# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Time   : 2024/8/18 11:53
#    @Description   : 
#
# ===============================================================


class Solution:
    def swapPairs(self, head):
        """
        递归子函数：
            返回已经交换好的子链表


        :param head:
        :return:
        """

        if not head or not head.next:
            return head

        new_head = head.next
        sub_head = new_head.next

        head.next = self.swapPairs(sub_head)
        new_head.next = head

        return new_head