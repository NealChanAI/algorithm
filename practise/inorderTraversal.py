# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Time   : 2024/8/17 22:06
#    @Description   : 
#
# ===============================================================


class ListNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# # 写法一
# class Solution:
#     def __init__(self):
#         self.res = []
#
#     def inorderTraversal(self, root):
#         if not root:
#             return []
#
#         def _traversal_helper(node):
#             if not node:
#                 return
#             self.inorderTraversal(node.left)
#             self.res.append(node.val)
#             self.inorderTraversal(node.right)
#
#         _traversal_helper(root)
#
#         return self.res
#

# 写法二
def main():
    # res = []
    def inorderTraversal(root):
        if not root:
            return []

        # global res
        res = []

        def _traversal_helper(node):
            if not node:
                return
            # global res
            _traversal_helper(node.left)
            res.append(node.val)
            # print(node.val)
            _traversal_helper(node.right)

        _traversal_helper(root)

        return res

    # node1 = ListNode(1)
    # node2 = ListNode(2)
    # node3 = ListNode(3)
    # node4 = ListNode(4)
    # node5 = ListNode(5)
    # node1.left = node2
    # node1.right = node3
    # node2.right = node4
    # node3.left = node5

    # print(inorderTraversal(node1))


if __name__ == '__main__':
    main()
