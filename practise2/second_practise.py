# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Time   : 2025-08-05 10:44
#    @Description   : 
#
# ===============================================================


import heapq


class ListNode():
    def __init__(self, val):
        self.val = val
        self.next = None

class ListNode2():
    def __init__(self, val):
        self.val = val
        self.next = next

    def __lt__(self, other):
        return self.val < other.val


class Solution:
    def merge_two_lists(self, l1, l2):
        """
        double pointers
        :param l1:
        :param l2:
        :return:
        """

        dummy = ListNode(-1)
        p1, p2 = l1, l2
        p = dummy

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

    def merge_k_lists(self, lists):
        """
        use heapq to get the smallest node
        :param lists:
        :return:
        """
        if not lists:
            return None

        dummy = ListNode2(-1)
        p = dummy


        pq = []
        for node in lists:
            if node:
                heapq.heappush(pq, (node.val, node))

        while pq:
            # get the smallest val node
            val, node = heapq.heappop(pq)
            p.next = node

            if node.next:
                heapq.heappush(pq, (node.next.val, node.next))

            p = p.next

        return dummy.next

    def get_intersection_node(self, headA, headB):
        """
        get the intersection node
        :param headA:
        :param headB:
        :return:
        """
        if not headA or not headB:
            return

        p1, p2 = headA, headB
        while p1 != p2:
            if p1:
                p1 = p1.next
            else:
                p1 = headB

            if p2:
                p2 = p2.next
            else:
                p2 = headA

        return p1

    def has_cycle(self, head):
        """
        slow and fast points
        :param head:
        :return:
        """
        if not head:
            return

        s, f = head, head
        while f and f.next:
            f = f.next.next
            s = s.next

            if f == s:
                return True

        return False


    def detect_cycle(self, head):
        """
        slow and fast pointers
        :param head:
        :return:
        """
        if not head:
            return

        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                fast = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow

        return None

    def remove_nth_from_end(self, head, n):
        """
        double pointers
        :param head:
        :param n:
        :return:
        """
        if not head or n < 0:
            return

        left, right = head, head

        for _ in range(n):
            if not right:
                return
            right = right.next

        while right.next:
            left = left.next
            right = right.next

        left.next = left.next.next

        return head

    def delete_duplicates(self, head):
        """
        slow and fast
        :param head:
        :return:
        """
        if not head:
            return

        slow, fast = head, head
        while fast:
            if slow != fast:
                slow.next = fast
                slow = slow.next
            fast = fast.next
        slow.next = None
        return head

    def move_zeros(self, nums):
        if not nums:
            return

        slow, fast = 0, 0
        while fast < len(nums):
            if nums[fast] != 0:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1

        for i in range(slow, len(nums)):
            nums[i] = 0

    def remove_duplicates(self, nums):
        """
        slow and fast double pointers
        :param nums:
        :return:
        """
        if not nums:
            return

        slow, fast = 0, 0
        while fast < len(nums):
            if nums[slow] != nums[fast]:
                slow += 1
                nums[slow] = nums[fast]
            fast += 1

        return slow + 1

    def partition_86(self, head, x):
        """
        tow linked_list
        :param head:
        :param x:
        :return:
        """
        dummy1 = ListNode(-1)
        dummy2 = ListNode(-1)
        p, p1, p2 = head, dummy1, dummy2

        while p:
            if p.val <= x:
                p1.next = p
                p1 = p1.next
            else:
                p2.next = p
                p2 = p2.next

            tmp = p.next
            p.next = None
            p = tmp
        p1.next = dummy2.next

        return dummy1.next

    def min_window(self, s, t):
        """
        sliding window
        :param s:
        :param t:
        :return:
        """
        need, window = {}, {}
        left, right = 0, 0
        valid = 0
        length = float('inf')
        start = 0

        for c in t:
            if c not in need:
                need[c] = 0
            need[c] += 1

        while right < len(s):
            c = s[right]
            right += 1

            if c in need:
                if c not in window:
                    window[c] = 0
                window[c] += 1

                if window[c] == need[c]:
                    valid += 1

            while len(need) == valid:
                if right - left < length:
                    start = left
                    length = right - left

                d = s[left]
                left += 1

                if d in need:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1

            return '' if length == float('inf') else s[start: start+length]

    def length_of_longest_substring(self, s):
        """
        sliding window
        :param s:
        :return:
        """
        if not s:
            return

        window = {}
        res = 0
        left, right = 0, 0
        while right < len(s):
            c = s[right]
            right += 1

            if c not in window:
                window[c] = 0
            window[c] += 1

            while window[c] > 1:
                d = s[left]
                left += 1

                if d in window:
                    window[d] -= 1


            res = max(res, right - left)

        return res
