# -*- coding: utf-8 -*-
# ===============================================================
#
#
# ===============================================================


def my_sqrt(x):
    """
    二分法
    :param x:
    :return:
    """
    if x < 0:
        return

    low, high = 1, x
    res = -1
    while low <= high:
        mid = low + (high - low) // 2
        if mid * mid == x:
            return mid
        elif mid * mid > x:
            high = mid - 1
        else:
            res = mid
            low = mid + 1
    return res

if __name__ == '__main__':
    print(my_sqrt(8))

