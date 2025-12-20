"""
给你一个链表，两两交换其中相邻的节点，并返回交换后链表的头节点。你必须在不修改节点内部的值的情况下完成本题（即，只能进行节点交换）。
"""


class Solution:
    def swapPairs(self, head):
        if not head or not head.next:
            return head

        nxt = head.next
        sub = nxt.next
        nxt.next = head
        head.next = self.swapPairs(sub)

        return nxt
