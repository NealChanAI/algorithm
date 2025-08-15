# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author :
#    @Create Time   : 2024/7/17 22:00
#    @Description   : 129. 回溯算法
#
# ===============================================================


class Solution:
    def __init__(self):
        self.res = 0
        self.path = []

    def sumNumbers(self, root):
        """
        回溯算法：
            1. 当到达叶子结点时，累加当前的值
        :param root:
        :return:
        """
        if not root:
            return

        def back_track(node):
            if not node:
                return

            self.path.append(str(node.val))
            # 判断是否为叶子结点
            if not node.left and not node.right:

                self.res += int("".join(self.path.copy()))

            back_track(node.left)
            back_track(node.right)

            self.path.pop()

        back_track(root)
        return self.res


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


if __name__ == '__main__':
    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(3)
    a.left = b
    b.left = c

    print(Solution().sumNumbers(a))
    # print("".join([1, 2, 3]))
