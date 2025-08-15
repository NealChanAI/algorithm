# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Time   : 2024/8/18 15:37
#    @Description   : 
#
# ===============================================================


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.res = 0
        self.track = []

    def sumNumbers(self, root):
        """回溯算法"""
        if not root:
            return 0

        def _back_track(node):
            # 结点为None，直接返回
            if not node:
                return
            # 将当前结点的值添加到track中
            self.track.append(str(node.val))

            # 当到达叶子结点时，累加值
            if not node.left and not node.right:
                self.res += int(''.join(self.track.copy()))
                # return

            _back_track(node.left)
            _back_track(node.right)

            self.track.pop()

        _back_track(root)

        return self.res


if __name__ == '__main__':
    root = TreeNode(1)
    left = TreeNode(2)
    right = TreeNode(3)

    root.left = left
    root.right = right

    print(Solution().sumNumbers(root))


