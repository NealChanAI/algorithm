"""
给你链表的头结点 head ，请将其按 升序 排列并返回 排序后的链表 。
"""


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def sortList(self, head):
        """
        归并排序
        """
        if not head or not head.next:
            return head

        mid = self.find_middle(head)
        sec = mid.next
        mid.next = None

        left = self.sortList(head)
        right = self.sortList(sec)

        return self.merge_two_sorted_lists(left, right)

    def find_middle(self, head):
        """找到链表的中点"""
        if not head:
            return

        s, f = head, head.next
        while f and f.next:
            s = s.next
            f = f.next.next

        return s

    def merge_two_sorted_lists(self, list1, list2):
        """合并两个lst"""
        if not list1 and not list2:
            return

        dummy = ListNode(-1)
        p, p1, p2 = dummy, list1, list2

        while p1 and p2:
            if p1.val <= p2.val:
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


def create_from_lst(lst):
    dummy = ListNode(-1)
    p = dummy

    for l in lst:
        p.next = ListNode(l)
        p = p.next

    return dummy.next


def print_linked_list(head):
    while head:
        print(head.val)
        head = head.next


if __name__ == '__main__':
    lst = [4, 2, 1, 3]
    llst = create_from_lst(lst)
    print_linked_list(llst)
    print('=' * 10)

    a = Solution()
    res = a.sortList(llst)
    print_linked_list(res)



