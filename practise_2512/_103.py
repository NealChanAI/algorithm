# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author : 
#    @Create Time   : 2025-12-15 17:55
#    @Description   : 
#
# ===============================================================


"""
给你二叉树的根节点 root ，返回其节点值的 锯齿形层序遍历 。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。
"""


class Solution:
    def zigzagLevelOrder(self, root):
        """
        双端队列
        flag来判断方向
        """
        res = []
        if not root:
            return res

        flag = True
        from collections import deque

        q = deque()
        q.append(root)

        while q:
            sz = len(q)
            tmp = []

            if flag:
                for i in range(sz):
                    node = q.popleft()
                    tmp.append(node.val)

                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
            else:
                for i in range(sz-1, -1, -1):
                    node = q.pop()
                    tmp.append(node.val)

                    if node.right:
                        q.appendleft(node.right)

                    if node.left:
                        q.appendleft(node.left)

            flag = not flag
            res.append(tmp)

        return res

