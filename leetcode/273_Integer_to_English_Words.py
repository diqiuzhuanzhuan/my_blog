# -*- coding: utf-8 -*-
"""
comments
author: diqiuzhuanzhuan
email: diqiuzhuanzhuan@gmail.com

"""


class Solution(object):
    _base = {
        "1": "One",
        "2": "Two",
        "3": "Three",
        "4": "Four",
        "5": "Five",
        "6": "Six",
        "7": "Seven",
        "8": "Eight",
        "9": "Nine",
        "10": "Ten",
        "11": "Eleven",
        "12": "Twelve",
        "13": "Thirteen",
        "14": "Fourteen",
        "15": "Fifteen",
        "16": "Sixteen",
        "17": "Seventeen",
        "18": "Eighteen",
        "19": "Nineteen"
    }

    _advance = {
        "2": "Twenty",
        "3": "Thirty",
        "4": "Forty",
        "5": "Fifty",
        "6": "Sixty",
        "7": "Seventy",
        "8": "Eighty",
        "9": "Ninety"
    }

    def fragment(self, num):
        if num == "0":
            return ["Zero"]
        s = []
        if len(num) == 3:
            query = self._base.get(num[0], None)
            if query:
                s.append(query)
                s.append("Hundred")
            num = num[1:]

        if len(num) == 2:
            query = self._base.get(num, None)
            if query:
                s.append(query)
                num = ""
            else:
                query = self._advance.get(num[0], None)
                if query:
                    s.append(query)
                num = num[1:]

        if len(num) == 1:
            query = self._base.get(num[0], None)
            if query:
                s.append(query)

        return s

    def metrics(self, index):
        if index == 1:
            return ["Thousand"]
        if index == 2:
            return ["Million"]
        if index == 3:
            return ["Billion"]
        return []

    def numberToWords(self, num):
        """

        :type num: int
        :rtype: str
        """
        s_num = str(num)
        length = len(s_num)
        index = 0
        s = []
        while s_num:

            cut = s_num[-3:]
            unit = self.fragment(cut)
            if unit:
                s = unit + self.metrics(index) + s

            s_num = s_num[:-3]
            index += 1

        return " ".join(s)


if __name__ == "__main__":
    solution = Solution()
    print(solution.fragment("318"))
    print(solution.fragment("300"))
    print(solution.fragment("309"))
    print(solution.fragment("9"))
    print(solution.fragment("29"))
    print(solution.fragment("209"))
    print(solution.fragment("009"))
    print(solution.numberToWords(318))
    print(solution.numberToWords(1318))
    print(solution.numberToWords(13181))
    print(solution.numberToWords(103181))
    print(solution.numberToWords(1234567891))
    print(solution.numberToWords(1000000))
    print(solution.numberToWords(0))
