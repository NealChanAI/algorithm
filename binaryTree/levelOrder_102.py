# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author : 
#    @Create Time   : 2025-09-05 10:33
#    @Description   : #102
#
# ===============================================================


"""
给你二叉树的根节点 root ，返回其节点值的 层序遍历 。 （即逐层地，从左到右访问所有节点）。
"""


from collections import deque


class Solution:
    def levelOrder(self, root):
        """层序遍历"""
        if not root:
            return []

        res = []
        q = deque()
        q.append(root)

        while q:
            sz = len(q)
            tmp = []
            for i in len(sz):
                node = q.popleft()
                tmp.append(node)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(tmp)
        return res





