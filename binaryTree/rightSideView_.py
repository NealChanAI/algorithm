# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author :
#    @Create Time   : 2024/7/1 15:23
#    @Description   : 
#
# ===============================================================


from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root):
        """
        层序遍历，取最后一个值
        :param root:
        :return:
        """

        if not root:
            return []

        q = deque()
        q.append(root)
        res = []

        while q:
            sz = len(q)
            for i in range(sz):
                node = q.popleft()
                if i == sz - 1:
                    res.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        return res




