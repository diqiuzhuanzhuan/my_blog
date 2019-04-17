# -*- coding: utf-8 -*-
"""
comments
author: diqiuzhuanzhuan
email: diqiuzhuanzhuan@gmail.com

"""


class Solution:

    def min(self, a, b):
        if a > b:
            return b
        else:
            return a

    def coinChange(self, coins, amount):
        if amount == 0:
            return 0
        coins = sorted(coins)
        res = [-1] * (amount + 1)
        res[0] = 0
        for i in range(coins[0], amount+1, 1):
            for _, j in enumerate(coins):
                if j > i:
                    break;
                if res[i-j] == -1:
                    continue
                if res[i] > 0:
                    res[i] = self.min(res[i - j] + 1, res[i])
                else:
                    res[i] = res[i - j] + 1
        return res[amount] or -1


if __name__ == "__main__":
    s = Solution()
    data = [
        ([1, 2, 5], 11, 3),
        ([474, 83, 404, 3], 264, 8),
        ([2, 5, 10, 1], 27, 4),
        ([186, 419, 83, 408], 6249, 20)
    ]
    import time
    t1 = time.time()
    for ele in data:
        print("input is {}, {}, output is {}, expected is {}".format(ele[0], ele[1], s.coinChange(ele[0], ele[1]), ele[2]))
        assert(s.coinChange(ele[0], ele[1]) == ele[2])
    t2 = time.time()
    print("consume {}".format(t2-t1))
