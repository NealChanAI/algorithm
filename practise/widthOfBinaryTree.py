# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Time   : 2024/8/18 11:33
#    @Description   : 
#
# ===============================================================


from collections import deque

class Solution:
    def widthOfBinaryTree(self, root):
        """pass"""
        if not root:
            return

        q = deque()
        q.append([root, 1])
        res = 0

        while q:
            q_size = len(q)
            tmp_res = []
            for i in range(q_size):
                node, idx = q.popleft()
                tmp_res.append(idx)
                if node.left:
                    q.append([node.left, idx * 2])
                if node.right:
                    q.append([node.right, idx * 2 + 1])

            res = max(res, tmp_res[-1] - tmp_res[0])

        return res
