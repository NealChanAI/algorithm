# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author : 
#    @Create Time   : 2025-09-05 10:39
#    @Description   : #103  todo
#
# ===============================================================


"""
给你二叉树的根节点 root ，返回其节点值的 锯齿形层序遍历 。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。
"""


from collections import deque

class Solution:
    def __init__(self):
        self.res = []

    def traverse(self, root, flag):
        if not root:
            return

        q = deque()
        q.append(root)

        while q:
            sz = len(q)
            tmp = []

            for i in range(sz):

                q.pop()
                if flag:
                    pass


    def zigzag_level_order(self, root):
        """
        层序遍历, 使用flag来控制方向
        """
