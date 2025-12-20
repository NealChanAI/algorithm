"""
给你二叉树的根节点 root 和一个整数目标和 targetSum ，找出所有 从根节点到叶子节点 路径总和等于给定目标和的路径。

叶子节点 是指没有子节点的节点。
"""


class Solution:
    def __init__(self):
        self.sum = 0
        self.path = []
        self.res = []

    def pathSum(self, root, targetSum):
        """backTrack"""
        self._path_sum_helper(root, targetSum)
        return self.res

    def _path_sum_helper(self, root, target):
        # base case
        if not root:
            return

        self.sum += root.val
        self.path.append(root.val)

        if not root.left and not root.right:
            if self.sum == target:
                self.res.append(self.path.copy())

        self._path_sum_helper(root.left, target)
        self._path_sum_helper(root.right, target)

        self.sum -= root.val
        self.path.pop()

