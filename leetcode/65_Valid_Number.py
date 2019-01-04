# -*- coding: utf-8 -*-
"""
comments
author: diqiuzhuanzhuan
email: diqiuzhuanzhuan@gmail.com

"""


class Solution(object):

    condition = [
        {"+", "-"},
        {"e"},
        {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"},
        {"."},
        {" "}
    ]

    condition_category = {
        "+": 0,
        "-": 1,
        "0": 2,
        "1": 2,
        "2": 2,
        "3": 2,
        "4": 2,
        "5": 2,
        "6": 2,
        "7": 2,
        "8": 2,
        "9": 2,
        ".": 3,
        "e": 4,
        " ": 5
    }

    station_table = {
        ("s0", 0): "s1",
        ("s0", 1): "s1",
        ("s0", 3): "s8",
        ("s0", 2): "s2",
        ("s1", 2): "s2",
        ("s1", 3): "s8",
        ("s2", 2): "s2",
        ("s2", 4): "s3",
        ("s2", 3): "s4",
        ("s3", 1): "s6",
        ("s3", 2): "s7",
        ("s3", 0): "s6",
        ("s4", 2): "s5",
        ("s4", 4): "s3",
        ("s5", 2): "s5",
        ("s5", 4): "s3",
        ("s6", 2): "s9",
        ("s7", 2): "s7",
        ("s8", 2): "s4",
        ("s9", 2): "s9",
        ("s0", 5): "s0",
        ("s2", 5): "s_end",
        ("s4", 5): "s_end",
        ("s5", 5): "s_end",
        ("s7", 5): "s_end",
        ("s9", 5): "s_end",
        ("s_end", 5): "s_end"
    }

    end_states = {
        "s2", "s4", "s5", "s7", "s9", "s_end"
    }

    def go(self, current_state, condition):
        category = self.condition_category.get(condition, -1)
        if category == -1:
            return "Failed"
        next_state = self.station_table.get((current_state, category), -1)
        if next_state == -1:
            return "Failed"
        return next_state

    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool

        """
        current_state = "s0"
        for idx, char in enumerate(s):
            current_state = self.go(current_state, char)
            if current_state == "Failed":
                return False

        if current_state in self.end_states:
            return True
        else:
            return False


if __name__ == "__main__":
    so = Solution()
    examples = [
        ("0", True),
        (" 0.1 ", True),
        ("abc", False),
        ("1 a", False),
        ("2e10", True),
        (" -90e3   ", True),
        (" 1e", False),
        ("e3", False),
        (" 6e-1", True),
        (" 99e2.5 ", False),
        ("53.5e93", True),
        (" --6 ", False),
        ("-+3", False),
        ("95a54e53", False),
        ("-1.", True),
        ("+0e-", False),
        ("+.8", True),
        ("46.e3", True),
        (" 005047e+6", True),
        (" 005 047e+6 ", False)
    ]
    for ele in examples:
        print(ele[0])
        assert(so.isNumber(ele[0]) == ele[1])
