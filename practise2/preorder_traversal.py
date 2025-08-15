

class Solution:
    def __init__(self):
        self.res = []

    def preorderTraversal(self, root):
        self.traverse(root)
        return self.res
    
    def traverse(self, root):
        if not root:
            return

        self.res.append(root.val)
        self.traverse(root.left)
        self.traverse(root.right)