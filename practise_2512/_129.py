"""
给你一个二叉树的根节点 root ，树中每个节点都存放有一个 0 到 9 之间的数字。
每条从根节点到叶节点的路径都代表一个数字：

例如，从根节点到叶节点的路径 1 -> 2 -> 3 表示数字 123 。
计算从根节点到叶节点生成的 所有数字之和 。

叶节点 是指没有子节点的节点。
"""


class Solution:
    def __init__(self):
        self.res = 0
        self.path = ''

    def sumNumbers(self, root):
        """
        遍历
        """
        self._sum_numbers_helper(root)
        return self.res

    def _sum_numbers_helper(self, root):
        # base case
        if not root:
            return

        self.path += str(root.val)

        if not root.left and root.right:  # 叶子节点
            self.res += int(self.path)

        self._sum_numbers_helper(root.left)
        self._sum_numbers_helper(root.right)
        self.path = self.path[:-1]


