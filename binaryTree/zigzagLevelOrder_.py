# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author :
#    @Create Time   : 2024/7/1 14:59
#    @Description   : 
#
# ===============================================================


from collections import deque

class Solution:
    def zigzagLevelOrder(self, root):
        """
        层次遍历，加一个flag控制方向
        :param root:
        :return:
        """
        # 合理性判断
        if not root:
            return []

        res = []
        q = deque()
        flag = True
        q.append(root)

        while q:
            sz = len(q)
            tmp_res = []
            if flag:
                for i in range(sz):
                    node = q.popleft()
                    tmp_res.append(node.val)
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
                res.append(tmp_res)
                flag = False
            else:
                for i in range(sz):
                    node = q.pop()
                    tmp_res.append(node.val)
                    if node.right:
                        q.appendleft(node.right)
                    if node.left:
                        q.appendleft(node.left)
                res.append(tmp_res)
                flag = True
        return res

