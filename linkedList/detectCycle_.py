# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author :
#    @Create Time   : 2024/6/7 10:39
#    @Description   : 142. 环形链表
#
# ===============================================================

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def detect_cycle(head):
    """
    快慢指针
    思考：若有环，设head到环起点的距离为a, 环长为b，则f = 2s；f - s = nb; 环起点的位置为a + nb；
        故当双指针相遇是，慢指针走了nb步，只需要再走a步即可到环起点；
    代码逻辑：
    1. 非空判断
    2. 快慢指针
    3. 当两者相遇时，将快指针指向head，每次走一步，当两者再次相遇时，返回
    :param head:
    :return:
    """
    # 非空判断
    if not head:
        return

    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if fast == slow:
            break
    # 无环，返回结果
    if not fast or not fast.next:
        return

    fast = head
    while fast != slow:
        fast = fast.next
        slow = slow.next

    return slow

