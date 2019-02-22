# -*- coding: utf-8 -*-
"""
comments
author: diqiuzhuanzhuan
email: diqiuzhuanzhuan@gmail.com

"""
import string


class MyDfa(object):

    def __init__(self):
        state_table = None

        # 定义字母表
        self.alphabet = set(string.ascii_letters)
        # 定义数字表
        self.digits = set(string.digits)
        # 定义状态转移矩阵

    def delta(self, state, char):
        """
        状态转移函数
        :param state:
        :param char:
        :return:
        """
        if state == "init":
            if char in self.alphabet:
                return 1
            else:
                return "error"
        if state == 1 or state == 2:
            if char in self.alphabet or char in self.digits:
                return 2
            else:
                return "error"
        return "error"

    def walk(self, str):
        final = "init"
        for i in str:
            final = self.delta(final, i)
            if final == "error":
                break
        print(final)


if __name__ == "__main__":
    machine = MyDfa()
    machine.walk("aaadaf")
    machine.walk("1aadaf")
    machine.walk("b1aadaf")
