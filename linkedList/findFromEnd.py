# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author :
#    @Create Time   : 2023/11/15 16:16
#    @Description   : 倒数第K个节点
#
# ===============================================================

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

def find_from_end(head, k):
    """
    使用双指针，A指针先走K步，然后B指针开始走，待到A指针走到尾节点时，B指针所指即为所求
    :param head:
    :param k:
    :return:
    """
    # 合理性判断
    if not head:
        return

    a = head
    b = head

    for i in range(k):
        a = a.next

    while a:
        b = b.next
        a = a.next

    return b.val


