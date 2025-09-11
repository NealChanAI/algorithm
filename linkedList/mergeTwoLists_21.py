# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author :
#    @Create Time   : 2025-08-27 14:22
#    @Description   : #21
#
# ===============================================================


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

def create_linked_list(arr):
    """
    create linked list from array
    """
    if not arr:
        return

    head = ListNode(arr[0])
    cur = head
    for i in range(1, len(arr)):
        cur.next = ListNode(arr[i])
        cur = cur.next
    return head

def print_linked_list(head):
    """
    print linked list
    """
    if not head:
        return
    lst = []
    while head:
        lst.append(str(head.val))
        head = head.next

    print('->'.join(lst))


class Solution:
    def mergeTwoLists(self, l1, l2):
        # define virtual head node
        dummy = ListNode(-1)
        p1, p2 = l1, l2
        p = dummy

        while p1 and p2:
            if p1.val < p2.val:
                p.next = p1
                p1 = p1.next
            else:
                p.next = p2
                p2 = p2.next

            p = p.next

        if p1:
            p.next = p1

        if p2:
            p.next = p2

        return dummy.next


if __name__ == '__main__':
    lst1 = [1, 4, 6, 8]
    lst2 = [0, 2, 4, 9, 10]

    l1 = create_linked_list(lst1)
    l2 = create_linked_list(lst2)

    # print_linked_list(l1)
    # print_linked_list(l2)

    res = Solution().merge_two_lists(l1, l2)
    print_linked_list(res)

