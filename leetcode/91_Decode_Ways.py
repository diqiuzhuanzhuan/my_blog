# -*- coding: utf-8 -*-
"""
comments
author: diqiuzhuanzhuan
email: diqiuzhuanzhuan@gmail.com

"""


class Solution:
    _map = {}

    def discriminate(self, n: str) -> int:
        if len(n) == 1:
            if int(n) == 0:
                return 0
            else:
                return 1
        if len(n) == 2:
            if int(n) < 10:
                return 0
            if int(n) <= 26:
                return 1
            return 0

    def count(self, n: str) -> int:
        if n in self._map:
            return self._map[n]
        if len(n) == 1:
            if int(n) == 0:
                return 0
            else:
                return 1
        if len(n) == 2:
            if int(n) < 10:
                return 0
            if int(n) <= 26 and int(n) % 10 == 0:
                return 1
            if int(n) <= 26:
                return 2
            if int(n) % 10 == 0:
                return 0
            return 1
        t1 = self.discriminate(n[0:1])
        t2 = self.discriminate(n[0:2])

        m = t1 * self.count(n[1:]) + t2 * self.count(n[2:])
        self._map[n] = m
        return m

    def numDecodings(self, s: str) -> int:
        return self.count(s)


if __name__ == "__main__":

    so = Solution()
    print(so.numDecodings("2001"))
    print(so.numDecodings("611111"))
