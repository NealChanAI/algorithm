# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author :
#    @Create Time   : 2024/6/27 16:56
#    @Description   : 297. 二叉树的序列化与反序列化
#
# ===============================================================


from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def serialize(self, root):
        """
        前序遍历
        :param root:
        :return:
        """
        res = []
        def traverse(root):
            if not root:
                res.append("#")
                return

            res.append(str(root.val))
            traverse(root.left)
            traverse(root.right)
        traverse(root)
        return ",".join(res)

    def deserialize(self, data):
        """
        反序列化，递归函数
        :param data:
        :return:
        """
        nodes = deque(data.split(","))

        def build(nodes):
            if not nodes:
                return

            node = nodes.popleft()
            if node == "#":
                return

            root = TreeNode(int(node))
            root.left = build(nodes)
            root.right = build(nodes)

            return root
        return build(nodes)



