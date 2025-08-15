

class Solution:
    def __init__(self):
        self.maxDiameter = 0

    def diameterOfBinaryTree(self, root):
        self.max_depth(root)
        return self.maxDiameter

    def max_depth(self, root):
        if not root:
            return 0

        left_max = self.max_depth(root.left)
        right_max = self.max_depth(root.right)

        diameter = left_max + right_max
        self.maxDiameter = max(self.maxDiameter, diameter)

        return 1 + max(left_max, right_max)

