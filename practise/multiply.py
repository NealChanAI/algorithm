# -*- coding: utf-8 -*-
# ===============================================================
#
#
# ===============================================================


class Solution:
    def multiply(self, num1, num2):
        """
        按照位数相乘
        :param num1:
        :param num2:
        :return:
        """
        m, n = len(num1) - 1, len(num2) - 1
        res = [0] * (m + n + 2)

        for i in range(m, -1, -1):
            for j in range(n, -1, -1):
                dot = int(num1[i]) * int(num2[j])
                tmp = res[i+j+1] + dot
                res[i+j+1] = tmp % 10
                res[i+j] = res[i+j] + tmp // 10

        # 前缀可能为0
        i = 0
        while i < len(res) and res[i] == 0:
            i += 1

        str_res = ''.join([str(x) for x in res[i:]])

        return '0' if not str_res else str_res


if __name__ == '__main__':
    print(Solution().multiply('2', '3'))
