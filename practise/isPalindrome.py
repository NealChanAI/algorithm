# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Time   : 2024/8/18 11:25
#    @Description   : 
#
# ===============================================================


class Solution:
    def isPalindrome(self, head):
        """转换成list再处理"""

        # 非空判断
        if not head:
            return

        lst = []
        while head:
            lst.append(head.val)
            head = head.next

        l, r = 0, len(lst) - 1
        while l < r:
            if lst[l] != lst[r]:
                return False
            l += 1
            r -= 1

        return True


