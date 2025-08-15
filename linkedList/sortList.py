# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author :
#    @Create Time   : 2024/7/1 08:48
#    @Description   : 148. 排序链表 未完成
#
# ===============================================================


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    # def sortList(self, head):
    #     """
    #     递归子函数：
    #         1. 返回已经排好序的链表，然后将头节点插入到已排好序的链表中
    #         2. base case：null或只有一个节点，就不需要排序了
    #     :param head:
    #     :return:
    #     """
    #     def sort_list_helper(head):
    #         # base case
    #         if not head:
    #             return
    #
    #         if not head.next:
    #             return head
    #
    #         # 返回已经排好序的子链表的头结点
    #         new_head = sort_list_helper(head.next)
    #
    #         # 将head结点插入到子链表中，使整个链表依然是有序的
    #         dummy1 = ListNode(-1)
    #         dummy1.next = new_head
    #         pre, cur = dummy1, new_head
    #         while cur and cur.val <= head.val:
    #             next = cur.next
    #             pre = cur
    #             cur = next
    #         pre.next = head
    #         head.next = cur
    #         # print("===" * 10)
    #         # # self.print_listnode(dummy1.next)
    #         # print("===" * 10)
    #
    #         return dummy1.next
    #
    #     return sort_list_helper(head)


    def sortList(self, head):
        """
        1. 找到链表的中点, 拆分成两个子链表
        2. 合并两个有序链表
        :param head:
        :return:
        """
        def find_middle(head):
            if not head or not head.next:
                return head, None

            slow, fast = head, head
            while fast and fast.next:
                fast = fast.next
                slow = slow.next

            next_head = slow.next
            slow.next = None
            return slow, next_head

        def merge_two_linklists(head1, head2):
            if not head1 and not head2:
                return
            if not head2:
                return head1

            dummy = ListNode(-1)
            p = dummy
            p1, p2 = head1, head2
            while p1 and p2:
                if p1.val >= p2.val:
                    p.next = p1
                    p1 = p1.next
                else:
                    p.next = p2
                    p2 = p2.next

                tmp = p.next
                p.next = None
                p = tmp

            if p1:
                p.next = p1
            if p2:
                p.next = p2
            return dummy.next

        if not head:
            return

        head1, head2 = find_middle(head)
        merge_two_linklists(head1, head2)















    def create_listnode(self, nums):
        if not nums:
            return
        dummy = ListNode(-1)
        p = dummy

        for num in nums:
            p.next = ListNode(num)
            p = p.next

        return dummy.next

    def print_listnode(self, head):
        if not head:
            return
        print(head.val)
        self.print_listnode(head.next)

if __name__ == '__main__':
    a = Solution()
    nums = [4, 2, 3, 1]
    head = a.create_listnode(nums)
    # print(a.print_listnode(head))
    a.print_listnode(a.sortList(head))

