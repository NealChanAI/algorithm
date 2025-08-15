# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author :
#    @Create Time   : 2024/7/1 17:36
#    @Description   : 
#
# ===============================================================


from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Codec:
    def __init__(self):
        self.res = []

    def serialize(self, root):

        def traverse(root):
            if not root:
                self.res.append("#")
                return

            # 前序遍历
            self.res.append(str(root.val))

            traverse(root.left)
            traverse(root.right)

        traverse(root)
        return ",".join(self.res)

    def deserialize(self, data):
        nodes = deque(data.split(","))

        def build(nodes):
            if not nodes:
                return

            node = nodes.popleft()
            if node.val == "#":
                return

            root = TreeNode()
            root.left = build(node)
            root.right = build(node)

            return root

        return build(nodes)


