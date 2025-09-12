# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author : 
#    @Create Time   : 2025-09-05 10:55
#    @Description   : #662
#
# ===============================================================


"""
给你一棵二叉树的根节点 root ，返回树的 最大宽度 。

树的 最大宽度 是所有层中最大的 宽度 。

每一层的 宽度 被定义为该层最左和最右的非空节点（即，两个端点）之间的长度。将这个二叉树视作与满二叉树结构相同，两端点间会出现一些延伸到这一层的 null 节点，这些 null 节点也计入长度。
"""


from collections import deque


class Solution:
    def __init__(self):
        self.res = 0

    def widthOfBinaryTree(self, root):
        """
        层序遍历
        """
        if not root:
            return -1

        q = deque()
        q.append([root, 1])

        while q:
            sz = len(q)
            tmp = []
            for i in range(sz):
                node, idx = q.popleft()
                tmp.append(idx)

                if node.left:
                    q.append([node.left, idx * 2])
                if node.right:
                    q.append([node.right, idx * 2 + 1])
            self.res = max(self.res, tmp[-1] - tmp[0] + 1)

        return self.res





