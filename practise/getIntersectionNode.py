# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Time   : 2024/8/17 21:33
#    @Description   : 
#
# ===============================================================


class Solution:
    def getIntersectionNode(self, head1, head2):
        """
        双指针

        :param head1:
        :param head2:
        :return:
        """
        # 非空判断
        if not head1 or not head2:
            return

        p1, p2 = head1, head2

        while p1 != p2:
            if not p1:
                p1 = head2
            else:
                p1 = p1.next

            if not p2:
                p2 = head1
            else:
                p2 = p2.next

        return p1

