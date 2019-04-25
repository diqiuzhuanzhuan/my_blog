# -*- coding: utf-8 -*-
"""
comments
author: diqiuzhuanzhuan
email: diqiuzhuanzhuan@gmail.com

"""
import numpy


class Solution(object):

    def profitableSchemes(self, G: int, P: int, group: list, profit: list) -> int:
        group_len = len(group) + 1
        value = [[[0 for _ in range(P+1)] for _ in range(G+1)] for _ in range(group_len)]

        value[0][0][0] = 1
        mod = 10**9 + 7
        for k in range(1, group_len):
            """
            for i in range(P+1):
                for j in range(G+1):
                    if j - group[k-1] < 0:
                        value[k][i][j] = value[k-1][i][j]
                    else:
                        value[k][i][j] = value[k-1][i][j] + value[k-1][max(0, i-profit[k-1])][j-group[k-1]]
            """
            g = group[k-1]
            p = profit[k-1]
            for i in range(G+1):
                for j in range(P+1):
                    if i - g < 0:
                        value[k][i][j] = value[k-1][i][j] % mod
                    else:
                        value[k][i][j] = (value[k-1][i][j] + value[k-1][i-g][max(j-p, 0)]) % mod

        res = sum([line[-1] for line in value[-1][:]]) % mod
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.profitableSchemes(5, 3, [2, 2], [2, 3]))
    print(s.profitableSchemes(10, 5, [2, 3, 5], [6, 7, 8]))
