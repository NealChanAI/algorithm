# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author :
#    @Create Time   : 2024/6/27 10:24
#    @Description   : 102. 二叉树的层序遍历
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
            return []

        q = deque()
        q.append(root)
        res = []

        while q:
            tmp_res = []
            for i in range(len(q)):
                cur = q.popleft()
                tmp_res.append(cur.val)
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            res.append(tmp_res)
        return res
