# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author :
#    @Create Time   : 2023/11/15 17:21
#    @Description   : 获取两个链表的交点
#
# ===============================================================

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def create_linked_list(arr):
    if not arr:  # 如果列表为空，返回None
        return None

    # 初始化链表头节点
    head = ListNode(arr[0])
    current = head

    # 遍历列表并创建链表
    for value in arr[1:]:
        current.next = ListNode(value)
        current = current.next

    return head


# 打印链表的辅助函数
def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> " if current.next else "")
        current = current.next
    print()


def get_intersection_node(head1, head2):
    p1, p2 = head1, head2

    while p1 != p2:
        # 若p1指向空指针，则将其指向head2
        if p1 is None:
            p1 = head2
        else:
            p1 = p1.next

        # 若p2指向空指针，则将其指向head1
        if p2 is None:
            p2 = head1
        else:
            p2 = p2.next

    return p1


if __name__ == '__main__':
    head_lst_1 = [2, 6, 4]
    head_lst_2 = [1, 5]
    linked_list_head1 = create_linked_list(head_lst_1)
    linked_list_head2 = create_linked_list(head_lst_2)
    get_intersection_node(linked_list_head1, linked_list_head2)
