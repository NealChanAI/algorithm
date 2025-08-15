# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author :
#    @Create Time   : 2024/7/1 16:36
#    @Description   : 
#
# ===============================================================


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def buildTree(self, preorder, inorder):
        """
        1. 先找到根结点
        2. 再拆分左右子树
        3. 最后分别找左右子树的根节点
        :param preorder:
        :param inorder:
        :return:
        """
        if not preorder or not inorder:
            return

        def build(pre_order, pre_start, pre_end, in_order, in_start, in_end):
            """

            :param pre_order:
            :param pre_start:
            :param pre_end:
            :param in_order:
            :param in_start:
            :param in_end:
            :return:
            """
            # base case
            if pre_start > pre_end:
                return

            # 找到根结点
            node_val = pre_order[pre_start]

            # 在中序列表中查找根结点
            index = 0
            for i in range(len(in_order)):
                if in_order[i] == node_val:
                    index = i
                    break

            left_node = build(pre_order, pre_start + 1, pre_start + (index - in_start), in_order, in_start, index - 1)
            right_node = build(pre_order, pre_start + (index - in_start) + 1, pre_end, in_order, index + 1, in_end)

            node = ListNode(node_val)
            node.left = left_node
            node.right = right_node

            return node

        return build(preorder, 0, len(preorder) - 1, inorder, 0, len(inorder) - 1)
