


class Solution:
    def __init__(self):
        self.res = []
        self.path = []
        self.sum = 0

    def combinationSum2(self, candidates, target):
        """
        nums sort
        """
        candidates.sort()
        # print(candidates)
        self._help(candidates, target, 0)
        return self.res

    def _help(self, candidates, target, start):

        if self.sum == target:
            self.res.append(self.path.copy())
            return

        if self.sum > target:
            return

        for i in range(start, len(candidates)):
            if i > start and candidates[i] == candidates[i-1]:
                continue
            self.sum += candidates[i]
            self.path.append(candidates[i])
            self._help(candidates, target, i+1)
            self.path.pop()
            self.sum -= candidates[i]


if __name__ == '__main__':
    a = Solution()
    c = [10,1,2,7,6,1,5]
    target = 8

    # c = [2,5,2,1,2]
    # target = 5

    print(a.combinationSum2(c, target))
