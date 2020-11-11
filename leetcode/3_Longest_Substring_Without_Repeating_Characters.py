# -*- coding: utf-8 -*-
# author: Feynman
# email: diqiuzhuanzhuan@gmail.com

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # abcabc ---> abc
        # pkwwke ---> pkw
        # pkwwke ---> pkw
        """
        解决问题的思路如下：
        abcdefadb
        需要用一个hash_map来记录之前出现过的每个字符的位置
        记录下每次没有重复字符的子串的起始偏移，它的初始值为0
        每遇到与当前子串内字符有重复的token后，开始更新起始偏移, 并保留最大无重复子串的长度
        0 1 2 3 4 5 6 7
        a b c d a f d m
        | | | | |  ----> a重复，此时offset由0更新到1
        | | | | | | | ----> d重复，此时offset由1更新到4
        ......
        """
        hash_map = {}
        max_len = 0
        offset_start = 0
        for i, ele in enumerate(s):
            # 判断当前token是否是在当前子串内有重复
            if ele in hash_map and hash_map[ele] >= offset_start:
                max_len = max(max_len, i - offset_start)
                offset_start = hash_map[ele] + 1
            else:
                max_len = max(max_len, i - offset_start + 1)
            hash_map[ele] = i
        return max_len



if __name__ == "__main__":
    s = Solution()
    print(s.lengthOfLongestSubstring("au"))
    print(s.lengthOfLongestSubstring(" "))
    print(s.lengthOfLongestSubstring(""))
    print(s.lengthOfLongestSubstring("aaba"))
    print(s.lengthOfLongestSubstring("abcabcbb"))
    print(s.lengthOfLongestSubstring("tmmzuxt"))




