#!/usr/bin/env python
# coding=utf-8
"""
Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary representation and return them as an array.

Example:
    For num = 5 you should return [0,1,1,2,1,2].

    Follow up:

    It is very easy to come up with a solution with run time O(n*sizeof(integer)). But can you do it in linear time O(n) /possibly in a single pass?
    Space complexity should be O(n).
    Can you do it like a boss? Do it without using any builtin function like __builtin_popcount in c++ or in any other language.

"""

class Solution(object):
    def countBits(self, num):
    """
    :type num: int
    :rtype: List[int]
    """
    #http://blog.csdn.net/tstsugeg/article/details/50922112
        if not num:
            return [0]
        res = [0]
        while True:
            i = 0
            sz = len(res)
            while i < sz:
                if len(res) == num + 1:
                    return res
                res.append(res[i] + 1)
                i += 1                                                                                                                                                                                          return res

