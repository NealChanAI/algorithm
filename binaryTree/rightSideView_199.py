# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author : 
#    @Create Time   : 2025-09-04 20:55
#    @Description   : #199
#
# ===============================================================


"""
给定一个二叉树的 根节点 root，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。
"""


from collections import deque

class Solution:
    def rightSideView(self, root):
        """
        层序遍历
        """
        if not root:
            return []

        res = []
        q = deque()
        q.append(root)

        while q:
            sz = len(q)

            for i in range(sz):
                node = q.popleft()
                if i == sz-1:
                    res.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        return res