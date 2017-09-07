#!/usr/bin/env python
# coding=utf-8
"""
Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive.

For example, given the range [5, 7], you should return 4.
"""
class Solution(object):
    def rangeBitwiseAnd(self, m, n):
    """
    :type m: int
    :type n: int
    :rtype: int
    """
    #http://www.cnblogs.com/grandyang/p/4431646.html
    while m < n:
        n &= n - 1
    return n
