"""
给你二叉树的根节点 root 和一个表示目标和的整数 targetSum 。判断该树中是否存在 根节点到叶子节点 的路径，这条路径上所有节点值相加等于目标和 targetSum 。如果存在，返回 true ；否则，返回 false 。

叶子节点 是指没有子节点的节点。
"""


class Solution:
    def __init__(self):
        self.sum = 0
        self.res = False

    def hasPathSum(self, root, targetSum):
        """1"""
        self.traverse(root, targetSum)
        return self.res

    def traverse(self, root, targetSum):
        if not root:
            return

        self.sum += root.val

        if not root.left and not root.right:
            if self.sum == targetSum:
                self.res = True
                return

        self.traverse(root.left, targetSum)
        self.traverse(root.right, targetSum)

        self.sum -= root.val

