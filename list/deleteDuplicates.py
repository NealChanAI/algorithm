
"""
给定一个已排序的链表的头 head ， 删除所有重复的元素，使每个元素只出现一次 。返回 已排序的链表 。
"""


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def delete_duplicates(head):
    """
    原地删除链表中的重复元素，使用快慢指针
    :param head:
    :return:
    """
    # 非空判断
    if not head:
        return

    # 初始化两个指针
    slow, fast = head, head

    # 遍历链表
    while fast:
        # 比较两者大小，若两者不相等，slow指针往前移动，将fast指针的值赋值给slow指针
        if slow.val != fast.val:
            slow.next = fast
            slow = slow.next
        fast = fast.next
    slow.next = None # 断开与后面重复元素的连接

    return head


