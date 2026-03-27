# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author : 
#    @Create Time   : 2026-03-27 12:47
#    @Description   : 
#
# ===============================================================


"""
给你二叉树的根节点 root ，返回其节点值的 层序遍历 。 （即逐层地，从左到右访问所有节点）。
"""


from collections import deque

class Solution:
    def levelOrder(self, root):

        q = deque()
        q.append(root)
        res = []

        while q:
            sz = len(q)
            tmp = []
            for i in range(sz):
                node = q.popleft()
                tmp.append(node.val)

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)
            res.append(tmp)

        return res

