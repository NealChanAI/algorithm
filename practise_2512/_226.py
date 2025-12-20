"""
给你一棵二叉树的根节点 root ，翻转这棵二叉树，并返回其根节点。
"""


class Solution:
    def invertTree(self, root):
        if not root:
            return

        left = self.invertTree(root.left)
        right = self.invertTree(root.right)

        root.left = right
        root.right = left

        return root