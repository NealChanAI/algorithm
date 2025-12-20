"""
给定两个整数数组 preorder 和 inorder ，其中 preorder 是二叉树的先序遍历，
inorder 是同一棵树的中序遍历，请构造二叉树并返回其根节点。

输入: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
输出: [3,9,20,null,null,15,7]
示例 2:

输入: preorder = [-1], inorder = [-1]
输出: [-1]

preorder 和 inorder 均 无重复 元素
"""


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder, inorder):
        """
        使用辅助函数，递归构造
        """
        return self._build_tree_helper(preorder, 0, len(preorder)-1, inorder, 0, len(inorder)-1)

    def _build_tree_helper(self, preorder, pre_start, pre_end, inorder, in_start, in_end):
        # 边界条件
        if pre_start > pre_end or in_start > in_end:
            return

        # preorder的pre_start是根节点
        root_val = preorder[pre_start]

        idx = -1
        for i in range(in_start, in_end+1):
            if root_val == inorder[i]:
                idx = i
                break

        root = TreeNode(root_val)
        root.left = self._build_tree_helper(preorder, pre_start+1, pre_start+idx-in_start, inorder, in_start, idx-1)
        root.right = self._build_tree_helper(preorder, pre_start+idx-in_start+1, pre_end, inorder, idx+1, in_end)

        return root


