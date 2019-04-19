# -*- coding: utf-8 -*-
"""
comments
author: diqiuzhuanzhuan
email: diqiuzhuanzhuan@gmail.com

"""


class Solution:
    """
    def change(self, amount: int, coins: List[int]) -> int:
        if amount == 0:
            return 1
        if amount < 0 or len(coins) == 0:
            return 0
        return self.change(amount - coins[0], coins) + self.change(amount, coins[1:])
    """

    def change(self, amount: int, coins: list) -> int:
        if amount == 0:
            return 1
        t = [0] * (amount + 1)
        t[0] = 1
        for j in coins:
            for i in range(amount + 1):
                if i - j < 0:
                    continue
                t[i] += t[i - j]

        return t[amount]


if __name__ == "__main__":
    s = Solution()
    print(s.change(11, [1, 2]))
