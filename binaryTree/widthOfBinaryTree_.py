# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author :
#    @Create Time   : 2024/7/1 17:16
#    @Description   : 
#
# ===============================================================


from collections import deque

class Solution:
    def widthOfBinaryTree(self, root):
        """
        1. 层序遍历
        2. 给每个结点编号，root从1开始，左结点 1 * 2， 右结点为1 * 2 + 1
        :param root:
        :return:
        """
        if not root:
            return -1
        q = deque()
        q.append([root, 1])

        res = 0

        while q:
            tmp = []
            sz = len(q)
            for i in range(sz):
                node, idx = q.popleft()
                tmp.append([node, idx])

                if node.left:
                    q.append([node.left, idx * 2])
                if node .right:
                    q.append([node.right, idx * 2 + 1])

            global res
            res = max(res, tmp[-1][1] - tmp[0][1] + 1)

        return res








