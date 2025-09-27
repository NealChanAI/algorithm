# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author : 
#    @Create Time   : 2025/9/25 19:22
#    @Description   : 
#
# ===============================================================


"""
给你二叉树的根结点 root ，请你将它展开为一个单链表：

展开后的单链表应该同样使用 TreeNode ，其中 right 子指针指向链表中下一个结点，而左子指针始终为 null 。
展开后的单链表应该与二叉树 先序遍历 顺序相同。
"""


class ListNode:
    def __init__(self, val):
        self.val = val


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    """
    1. 非空判断
    2. 递归遍历：将结果保存为列表
    3. 根据列表创建链表
    """
    def __init__(self):
        self.res_lst = []

    def traverse(self, root):
        # 非空判断
        if not root:
            return

        self.res_lst.append(root.val)
        # 遍历左子树
        self.traverse(root.left)
        # 遍历右子树
        self.traverse(root.right)

    def create_tree(self, lst):
        """根据列表构造树"""
        # 非空判断
        if not lst:
            return
        dummy = TreeNode(lst[0])
        root = dummy

        for i in range(1, len(lst)):
            root.left = None
            root.right = TreeNode(lst[i])
            root = root.right

        return dummy

    def extent_linked_list(self, root):
        # 按照前序遍历树，并将结果保存到列表中
        self.traverse(root)
        # 根据列表构造链表（树）
        res_linked_lst = self.create_tree(self.res)
        return res_linked_lst