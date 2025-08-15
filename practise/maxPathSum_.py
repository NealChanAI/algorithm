# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author :
#    @Create Time   : 2024/8/17 22:48
#    @Description   : 
#
# ===============================================================


class ListNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def maxPathSum(root):
    if not root:
        return

    global res
    res = float('-inf')

    def max_gain(node):
        # base case
        if not node:
            return 0

        left = max(max_gain(node.left), 0)
        right = max(max_gain(node.right), 0)

        global res
        res = max(res, node.val + left + right)

        return node.val + max(left, right)

    max_gain(root)
    return res


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node1.left = node2
node1.right = node3
node2.right = node4
node3.left = node5

print(maxPathSum(node1))