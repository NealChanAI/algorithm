"""
给你一棵二叉树的根节点，返回该树的 直径 。

二叉树的 直径 是指树中任意两个节点之间最长路径的 长度 。这条路径可能经过也可能不经过根节点 root 。

两节点之间路径的 长度 由它们之间边数表示。
"""


class Solution:
    def __int__(self):
        self.res = 0

    def diameterOfBinaryTree(self, root):
        """左右子树木的深度之和"""
        self.res = 0 
        self.max_depth(root)
        return self.res

    def max_depth(self, root):
        if not root:
            return 0

        left = self.max_depth(root.left)
        right = self.max_depth(root.right)

        self.res = max(self.res, left + right)

        return 1 + max(left, right)
