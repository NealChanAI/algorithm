# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author :
#    @Create Time   : 2024/6/27 15:49
#    @Description   : 105. 从前序与中序遍历序列构造二叉树
#
# ===============================================================

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder, inorder):
        def construct(preorder, prestart, preend, inorder, instart, inend):
            root_val = preorder[prestart]
            root = TreeNode(root_val)

            root_idx = -1
            for i in range(instart, inend + 1):
                if inorder[i] == root_val:
                    root_idx = i
                    break

            root.left = construct(preorder, prestart+1, prestart+(root_idx-instart), inorder, instart, root_idx-1)
            root.right = construct(preorder, prestart+(root_idx-instart)+1, preend, inorder, root_idx+1, inend)

            return root

        return construct(preorder, 0, len(preorder)-1, inorder, 0, len(inorder)-1)
