# -*- coding: utf-8 -*-
"""
comments
author: diqiuzhuanzhuan
email: diqiuzhuanzhuan@gmail.com

"""


class Solution(object):

    def __init__(self):
        self.table = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        self.keys = {"(", "{", "["}
        self.values = {")", "}", "]"}

    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        queue = []
        for i in s:
            if i in self.keys:
                queue.append(i)
            elif i in self.values:
                valid = (len(queue) > 0 and self.table.get(i, -1) == queue.pop())
                if not valid:
                    return False
        return len(queue) == 0

