# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author : 
#    @Create Time   : 2025-09-04 17:35
#    @Description   : #297
#
# ===============================================================


"""
序列化是将一个数据结构或者对象转换为连续的比特位的操作，进而可以将转换后的数据存储在一个文件或者内存中，同时也可以通过网络传输到另一个计算机环境，采取相反方式重构得到原数据。

请设计一个算法来实现二叉树的序列化与反序列化。这里不限定你的序列 / 反序列化算法执行逻辑，你只需要保证一个二叉树可以被序列化为一个字符串并且将这个字符串反序列化为原始的树结构。

提示: 输入输出格式与 LC 目前使用的方式一致，详情请参阅 LC 序列化二叉树的格式。你并非必须采取这种方式，你也可以采用其他的方法解决这个问题。
"""


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Codec:
    def __init__(self):
        self.res = []

    def _serialize(self, root):
        if not root:
            self.res.append('#')
            return

        self.res.append(root.val)
        self._serialize(root.left)
        self._serialize(root.right)

    def serialize(self, root):
        """
        前序遍历
        """
        self._serialize(root)

        return ','.join(self.res)

    def _deserialize(self, nodes):
        if not nodes:
            return

        root_val = nodes.popleft()
        if root_val == '#':
            return
        root = TreeNode(root_val)

        root.left = self._deserialize(nodes)
        root.right = self._deserialize(nodes)

        return root

    def deserialize(self, data):
        from collections import deque

        nodes = deque(data.split('#'))
        return self._deserialize(nodes)
