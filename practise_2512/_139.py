# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author : 
#    @Create Time   : 2026/1/4 22:09
#    @Description   : 
#
# ===============================================================


"""
给你一个字符串 s 和一个字符串列表 wordDict 作为字典。如果可以利用字典中出现的一个或多个单词拼接出 s 则返回 true。

注意：不要求字典中出现的单词全部都使用，并且字典中的单词可以重复使用。



示例 1：

输入: s = "leetcode", wordDict = ["leet", "code"]
输出: true
解释: 返回 true 因为 "leetcode" 可以由 "leet" 和 "code" 拼接成。
示例 2：

输入: s = "applepenapple", wordDict = ["apple", "pen"]
输出: true
解释: 返回 true 因为 "applepenapple" 可以由 "apple" "pen" "apple" 拼接成。
     注意，你可以重复使用字典中的单词。
示例 3：

输入: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
输出: false
"""


class Solution:
    def __init__(self):
        self.found = False
        self.track = []

    def wordBreak(self, s, wordDict):
        """
        递归子结构：
            若词典中有一个单次是s的前缀，则再判断剔除掉这个前缀后的子串
        """
        self.backtrack(s, 0, wordDict)
        return self.found

    def backtrack(self,s, i, wordDict):
        # base case
        if self.found:
            return

        if i == len(s):
            self.found = True
            return

        for word in wordDict:
            _len = len(word)
            if i + _len <= len(s) and s[i: i+_len] == word:
                self.track.append(word)
                self.backtrack(s, i+_len, wordDict)
                self.track.pop()
