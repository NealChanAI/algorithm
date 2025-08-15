# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author :
#    @Create Time   : 2024/7/1 14:50
#    @Description   : 
#
# ===============================================================


from collections import deque

class Solution:
    def levelOrder(self, root):
        q = deque()
        q.append(root)
        res = []

        while q:
            tmp_res = []
            sz = len(q)
            for i in range(sz):
                node = q.popleft()
                tmp_res.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(tmp_res)
        return res