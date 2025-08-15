# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Time   : 2024/8/17 16:35
#    @Description   : 
#
# ===============================================================


from collections import deque

class Solution:
    def zigzagLevelOrder(self, root):
        """双端队列 结合 flag"""
        if not root:
            return []

        q = deque()
        res = []
        q.append(root)
        flag = True

        while q:
            tmp_res = []
            tmp_size = len(q)

            if flag:  # 正序
                for i in range(tmp_size):
                    node = q.popleft()
                    tmp_res.append(node.val)
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
                    flag = False
            else:  # 倒序
                for i in range(tmp_size):
                    node = q.pop()
                    tmp_res.append(node.val)
                    if node.right:
                        q.appendleft(node.right)
                    if node.left:
                        q.appendleft(node.left)
                    flag = True
            res.append(tmp_res)
        return res



