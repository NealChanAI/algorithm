# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Time   : 2024/8/17 23:30
#    @Description   : 
#
# ===============================================================


from collections import deque

class Solution:
    def rightSideView(self, root):
        """右视图，层序遍历"""
        if not root:
            return []

        q = deque()
        q.append(root)
        res = []

        while q:
            tmp_size = len(q)
            for i in range(tmp_size):
                node = q.popleft()
                if i == tmp_size - 1:
                    res.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        return res



