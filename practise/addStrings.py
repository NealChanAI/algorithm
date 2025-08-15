# -*- coding: utf-8 -*-
# ===============================================================
#
#    @Description   : 
#
# ===============================================================


class Solution:
    def addStrings(self, num1, num2):
        """
        算法流程： 设定 i，j 两指针分别指向 num1，num2 尾部，模拟人工加法；

        计算进位： 计算 carry = tmp // 10，代表当前位相加是否产生进位；
        添加当前位： 计算 tmp = n1 + n2 + carry，并将当前位 tmp % 10 添加至 res 头部；
        索引溢出处理： 当指针 i或j 走过数字首部后，给 n1，n2 赋值为 0，相当于给 num1，num2 中长度较短的数字前面填 0，以便后续计算。
        当遍历完 num1，num2 后跳出循环，并根据 carry 值决定是否在头部添加进位 1，最终返回 res 即可。

        :param num1:
        :param num2:
        :return:
        """

        i, j = len(num1) - 1, len(num2) - 1
        carry = 0
        res = ''

        while i >= 0 or j >= 0:
            n1 = int(num1[i]) if i >= 0 else 0
            n2 = int(num2[j]) if j >= 0 else 0
            tmp = n1 + n2 + carry
            carry = tmp // 10
            res = str(tmp % 10) + res
            i -= 1
            j -= 1
        return '1' + res if carry else res
