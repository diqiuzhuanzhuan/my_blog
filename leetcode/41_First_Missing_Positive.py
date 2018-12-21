# -*- coding: utf-8 -*-
"""
comments
author: diqiuzhuanzhuan
email: diqiuzhuanzhuan@gmail.com

"""


class Solution(object):

    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0: return 1
        i = 0
        while i < n:
            if nums[i] <= 0 or nums[i] > n:
                i = i+1
                continue
            #bypass duplication
            if nums[nums[i]-1] == nums[i]:
                i = i+1
                continue

            if nums[i] != i+1:
                t = nums[i]
                nums[i] = nums[nums[i] - 1]
                nums[t-1] = t
            else:
                i = i+1

        for i, j in enumerate(nums):
            if j != i+1:
                return i+1

        return nums[n-1] + 1


if __name__ == "__main__":
    t = Solution()
    print(t.firstMissingPositive([1, 2, 0]))
    print(t.firstMissingPositive([3, 4, -1, 1]))
    print(t.firstMissingPositive([7, 9, 11, 3]))
    print(t.firstMissingPositive([0, 2, 2, 1, 1]))
    print(t.firstMissingPositive([1]))
