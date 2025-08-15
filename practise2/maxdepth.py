

class Solution:
    def __init__(self):
        self.depth = 0
        self.res = 0

    def maxDepth(self, root):
        self.traverse(root)
        return self.res

    def traverse(self, root):
        if not root:
            return

        # 前序遍历位置
        self.depth += 1

        # 遍历到叶子节点时记录最大深度
        if root.left is None and root.right is None:
            self.res = max(self.res, self.depth)

        self.traverse(root.left)
        self.traverse(root.right)

        self.depth -= 1


class Solution2:
    def maxDepth(self, root):
        if root is None:
            return 0
        left_max = self.maxDepth(root.left)
        right_max = self.maxDepth(root.right)

        return 1 + max(left_max, right_max)

