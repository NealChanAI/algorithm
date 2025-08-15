# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Time   : 2025-08-01 15:10
#    @Description   : 
#
# ===============================================================


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class ListNode2:
    def __init__(self, val):
        self.val = val
        self.next = None

    def __lt__(self, other):
        return self.val < other.val


class Solution():
    def merge_two_lists(self, l1, l2):
        # define a dummy head
        dummy = ListNode(-1)
        p, p1, p2 = dummy, l1, l2

        while p1 and p2:
            if p1.val <= p2.val:
                p.next = p1
                p1 = p1.next
            else:
                p.next = p2
                p2 = p2.next

            # go ahead
            p = p.next

        if p1:
            p.next = p2

        if p2:
            p.next = p1

        return dummy.next

    def partition_86(self, head, x):
        dummy1, dummy2 = ListNode(-1), ListNode(-1)
        p1, p2 = dummy1, dummy2
        p = head

        while p:
            if p.val < x:
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

    def merge_k_lists(self, lists):
        """
        merge k sorted list
        :param lists:
        :return:
        """
        if not lists:
            return
        import heapq

        dummy = ListNode2(-1)
        p = dummy

        # 优先级队列, 最小堆
        pq = []
        # 将K个链表的头节点放入最小堆
        for i, head in enumerate(lists):
            if head:
                heapq.heappush(pq, (head.val, i, head))

        while pq:
            # 获取最小节点
            val, i, node = heapq.heappop(pq)
            p.next = node

            if node.next:
                heapq.heappush(pq, (node.next.val, i, node.next))

            p = p.next

        return dummy.next

    def remove_nth_from_end(self, head, n):
        dummy = ListNode(-1)
        dummy.next = head

        p1, p2 = dummy, dummy
        for _ in range(n):
            if p2.next:
                p2 = p2.next
            else:
                raise Exception("Something Wrong")

        while p2.next:
            p1 = p1.next
            p2 = p2.next

        p1.next = p1.next.next

        return head


    def middle_node(self, head):
        dummy = ListNode(-1)
        dummy.next = head

        slow, fast = dummy, dummy

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.ne
        return slow

    def hasCycle(self, head):
        if not head:
            return

        dummy = ListNode(-1)
        dummy.next = head

        slow, fast = dummy, dummy

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False


    def detectCycle(self, head):
        if not head:
            return

        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                # encouter
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow

        return None

    def get_intersection_node(self, headA, headB):
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

    def remove_duplicates(self, nums):
        if not nums:
            return 0
        slow, fast = 0, 0
        while fast < len(nums):
            if nums[slow] != nums[fast]:
                slow += 1
                nums[slow] = nums[fast]
            fast += 1
        return slow + 1

    def delete_duplicates(self, head):
        if not head:
            return

        slow, fast = head, head
        while fast:
            if slow.val != fast.val:
                slow.next = fast
                slow = slow.next
            fast = fast.next
        slow.next = None
        return head

    def move_zeros(self, nums, val):
        if not nums:
            return
        slow, fast = 0, 0
        while fast < len(nums):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        for i in range(slow, len(nums)):
            nums[i] = 0

    def min_window(self, s, t):
        """
        sliding window
        :param s:
        :param t:
        :return:
        """
        need, window = {}, {}
        for c in t:
            if c not in need:
                need[c] = 0
            need[c] += 1

        left, right = 0, 0
        valid = 0

        # 记录最小覆盖子串的起始索引及长度
        start = 0
        length = float('inf')

        while right < len(s):
            # c是将移入窗口的字符
            c = s[right]
            # 扩大窗口
            right += 1
            # 进行窗口内数据的一系列更新
            if c in need:
                if c not in window:
                    window[c] = 0
                window[c] += 1

                if window[c] == need[c]:
                    valid += 1

            # 判断左侧窗口是否要收缩
            while valid == len(need):
                # 更新最小覆盖子串
                if right - left < length:
                    start = left
                    length = right - left
                # 缩小窗口
                d = s[left]
                left += 1
                if d in need:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1

        return '' if length == float('inf') else s[start: start+length]

    def check_inclusion(self, t, s):
        """
        sliding window
        :param t:
        :param s:
        :return:
        """
        need, window = {}, {}
        left, right = 0, 0
        valid = 0

        # 将t的字符串存入need中
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

            # 判断左侧窗口是否要收缩
            while right - left >= len(t):
                # 判断是否找到了合法的子串
                if valid == len(need):
                    return True
                d = s[left]
                left += 1
                # 进行窗口内数据的一系列更新
                if d in need:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1

        return False

    def find_anagrams(self, s, t):
        """
        sliding windows
        :param s:
        :param t:
        :return:
        """
        need, window = {}, {}
        left, right = 0, 0
        valid = 0
        res = []

        for c in t:
            if c not in need:
                need[c] = 0
            need[c] += 1

        while right < len(s):
            c = s[right]
            right += 1

            if c in need:
                window[c] += 1
                if window[c] == need[c]:
                    valid += 1

            while right - left >= len(t):
                # 判断是否满足条件
                if valid == len(need):
                    res.append(left)

                d = s[left]
                left += 1

                if d in need:
                    if window[d] == need[d]:
                        valid -=1
                    window[d] -= 1

        return res


    def length_of_longest_substring(self, s):
        """
        sliding window
        :param s:
        :return:
        """
        if not s:
            return

        window = {}
        res = -1
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

    def two_sum(self, numbers, target):
        """
        double pointers
        :param numbers:
        :param target:
        :return:
        """
        left, right = 0, len(target) - 1
        while left < right:
            sum = numbers[left] + numbers[right]
            if sum == target:
                return [left + 1, right + 1]
            elif sum > target:
                right -= 1
            else:
                left += 1

        return [-1, -1]

    def two_sum_v2(self, nums, target):
        """
        unorder arraylist
        :param nums:
        :param target:
        :return:
        """
        nums.sort()
        left, right = 0, len(nums) - 1
        while left < right:
            sum = nums[left] + nums[right]
            if sum == target:
                return [nums[left], nums[right]]
            elif sum > target:
                right -= 1
            else:
                left += 1
        return []

    def _two_sum_target(self, nums, start, target):
        """
        two sum
        :param nums:
        :param start:
        :param target:
        :return:
        """
        left, right = start, len(nums) - 1
        res = []
        while left < right:
            sum = nums[left] + nums[right]
            if sum > target:
                right -= 1
            elif sum < target:
                left += 1
            else:
                low = nums[left]
                high = nums[right]
                res.append([low, high])
                while left < right and nums[left] == low:
                    left += 1
                while left < right and nums[right] == high:
                    right -= 1
        return res


    def three_sum(self, nums):
        """
        implements two sum target firstly
        then iterates
        :param nums:
        :return:
        """
        if not nums:
            return

        nums.sort()
        res = []

        for i in range(len(nums)-2):
            if i != 0 and nums[i] == nums[i-1]:
                continue
            two_sum_res = self._two_sum_target(nums, i+1, -nums[i])
            if two_sum_res:
                res.append([nums[i], two_sum_res[0], two_sum_res[1]])

        return res

    def palindrome(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l += 1
            r -= 1
        return s[l+1: r]

    def longest_palindrome(self, s):
        res = ''
        for i in range(len(s)):
            s1 = self.palindrome(s, i, i)
            s2 = self.palindrome(s, i, i+1)

            res = res if len(res) > len(s1) else s1
            res = res if len(res) > len(s2) else s2

        return res