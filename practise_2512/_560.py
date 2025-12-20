"""
给你一个整数数组 nums 和一个整数 k ，请你统计并返回 该数组中和为 k 的子数组的个数 。

子数组是数组中元素的连续非空序列。
"""

class Solution:
    def subarraySum(self, nums, k):
        """
        字典
        前缀和
        """
        cnt = 0
        d = {0: 1}

        pre_sum = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            pre_sum[i+1] = pre_sum[i] + nums[i]
            need = pre_sum[i+1] - k
            if need in d:
                cnt += d[need]

            if pre_sum[i+1] not in d:
                d[pre_sum[i+1]] = 0
            d[pre_sum[i+1]] += 1

        return cnt


if __name__ == '__main__':
    a = Solution()
    nums = [1, 2, 3]
    k = 3

    nums = [1, 1, 1]
    k = 2
    print(a.subarraySum(nums, k))
