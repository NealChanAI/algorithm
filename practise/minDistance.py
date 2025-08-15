# -*- coding: utf-8 -*-
# ===============================================================
#
# ===============================================================


class Solution:
    def minDistance(self, word1, word2):
        """
        动态规划
            base case:
        :param word1:
        :param word2:
        :return:
        """
        memo = [ [-1] * len(word2) for _ in range(len(word1))]

        def dp(i, j):
            if memo[i][j] != -1:
                return memo[i][j]

            # base case
            if i < 0:
                return j + 1
            if j < 0:
                return i + 1

            if word1[i] == word2[j]:
                memo[i][j] = dp(i - 1, j - 1)
            else:
                memo[i][j] = min(dp(i - 1, j),
                           dp(i - i, j - 1),
                           dp(i, j - 1)) + 1

            return memo[i][j]

        return dp(len(word1) - 1, len(word2) - 1)


if __name__ == '__main__':
    word1 = "horse"
    word2 = "ros"
    print(Solution().minDistance(word1, word2))
