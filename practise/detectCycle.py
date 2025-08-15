# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Time   : 2024/8/17 21:59
#    @Description   : 
#
# ===============================================================


class Solution:
    def detectCycle(self, head):
        """
        环形链表：快慢指针
        :param head:
        :return:
        """
        # 非空判断
        if not head:
            return

        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            # 有环且相遇
            if slow == fast:
                fast = head
                while fast != slow:
                    fast = fast.next
                    slow = slow.next
                return slow
        # 无环
        return
