# -*- coding: utf-8 -*-
"""
comments
author: diqiuzhuanzhuan
email: diqiuzhuanzhuan@gmail.com

"""

class Solution:

    def longestPalindrome(self, s: str) -> str:

        length = len(s)
        flag = [[0 for _ in range(length)] for _ in range(length)]
        # init the matrix
        if s == "":
            res = ""
        else:
            res = s[0]
        for i in range(length):
            flag[i][i] = 1
            if i+1 < len(s) and s[i] == s[i+1]:
                flag[i][i+1] = 1
                res = s[i:i+1+1]

        for i in range(length-1, -1, -1):
            for j in range(length):
                if i-1 < 0 or j+1 >= length:
                    continue
                if s[i-1] == s[j+1] and flag[i][j] == 1:
                    flag[i-1][j+1] = 1
                    if (j+1) - (i-1) + 1 > len(res):
                        res = s[i-1:j+1+1]

        return res


if __name__ == "__main__":
    s = Solution()
    print(s.longestPalindrome("helllllllo"))
