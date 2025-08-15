# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author :
#    @Create Time   : 2024/6/27 10:41
#    @Description   : 103. 二叉树的锯齿形层序遍历
#
# ===============================================================

from collections import deque


class Solution:
    def zigzagLevelOrder(self, root):
        """
        双端队列 + flag方向控制
        :param root:
        :return:
        """
        if not root:
            return []

        q = deque()
        q.append(root)
        flag = True
        res = []

        while q:
            tmp_res = []
            if flag:  # 正序
                for i in range(len(q)):
                    cur = q.popleft()
                    tmp_res.append(cur.val)
                    if cur.left:
                        q.append(cur.left)
                    if cur.right:
                        q.append(cur.right)
                flag = False
                res.append(tmp_res)
            else:  # 倒序
                for i in range(len(q)):
                    cur = q.pop()
                    tmp_res.append(cur.val)
                    if cur.right:
                        q.appendleft(cur.right)
                    if cur.left:
                        q.appendleft(cur.left)
                flag = True
                res.append(tmp_res)
        return res
