# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Create Author : 
#    @Create Time   : 2026-01-04 11:19
#    @Description   : 
#
# ===============================================================


"""
有效 IP 地址 正好由四个整数（每个整数位于 0 到 255 之间组成，且不能含有前导 0），整数之间用 '.' 分隔。

例如："0.1.2.201" 和 "192.168.1.1" 是 有效 IP 地址，但是 "0.011.255.245"、"192.168.1.312" 和 "192.168@1.1" 是 无效 IP 地址。
给定一个只包含数字的字符串 s ，用以表示一个 IP 地址，返回所有可能的有效 IP 地址，这些地址可以通过在 s 中插入 '.' 来形成。你 不能 重新排序或删除 s 中的任何数字。你可以按 任何 顺序返回答案。

示例 1：

输入：s = "25525511135"
输出：["255.255.11.135","255.255.111.35"]
示例 2：

输入：s = "0000"
输出：["0.0.0.0"]
示例 3：

输入：s = "101023"
输出：["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]
提示：

1 <= s.length <= 20
s 仅由数字组成
"""


class Solution:
    def __init__(self):
        self.res = []
        self.track = []

    def restoreIpAddresses(self, s):
        self.backtrack(s, 0)
        return self.res

    def backtrack(self, s, start):
        # 叶子节点
        if start == len(s) and len(self.track) == 4:
            self.res.append('.'.join(self.track))

        for i in range(start, len(s)):
            if not self._is_valid(s, start, i):
                continue

            if len(self.track) >= 4:
                break

            self.track.append(s[start: i+1])
            self.backtrack(s, i+1)
            self.track.pop()

    def _is_valid(self, s, start, end):
        length = end - start + 1
        if length == 0 or length > 3:
            return False
        if length == 1:
            return True
        if s[start] == '0':  # 长度不为1
            return False
        if int(s[start: end+1]) > 255:
            return False

        return True


if __name__ == '__main__':
    s = "25525511135"
    s = "101023"
    s = "0000"
    a = Solution()
    print(a.restoreIpAddresses(s))

