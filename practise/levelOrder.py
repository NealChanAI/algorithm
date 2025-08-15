# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Time   : 2024/8/17 16:29
#    @Description   : 
#
# ===============================================================


from collections import deque

class Solution:
    def levelOrder(self, root):
        """
        使用双端队列处理
        :param root:
        :return:
        """
        if not root:
            return

        q = deque()
        q.append(root)
        res = []

        while q:
            tmp_res = []
            tmp_size = len(q)
            for i in range(tmp_size):
                node = q.popleft()
                tmp_res.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(tmp_res)

        return res




