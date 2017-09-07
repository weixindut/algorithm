#!/usr/bin/env python
# coding=utf-8
"""
A binary watch has 4 LEDs on the top which represent the hours (0-11), and the 6 LEDs on the bottom represent the minutes (0-59).

Each LED represents a zero or one, with the least significant bit on the right.
For example, the above binary watch reads "3:25".

Given a non-negative integer n which represents the number of LEDs that are currently on, return all possible times the watch could represent.

Example:

    Input: n = 1
    Return: ["1:00", "2:00", "4:00", "8:00", "0:01", "0:02", "0:04", "0:08", "0:16", "0:32"]
Note:
    The order of output does not matter.
    The hour must not contain a leading zero, for example "01:00" is not valid, it should be "1:00".
    The minute must be consist of two digits and may contain a leading zero, for example "10:2" is not valid, it should be "10:02".
"""
class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        if not num:
            return ["0:00"]
        res = []
        self.bc(res, list(), 0, num)
        print res
        return self.transform(res)

    def bc(self, res, tmp, start, num):
        if len(tmp) == num:
            import copy
            res.append(copy.copy(tmp))
            return
        if start == 10:
            return
        for i in range(start, 10):
            tmp.append(i)
            self.bc(res, tmp, i + 1, num)
            tmp.pop(-1)

    def transform(self, res):
        if not res:
            return []
        ret = []
        for l in res:
            h = 0
            m = 0
            for t in l:
                if 0 <= t <= 3:
                    h += pow(2, t)
                else:
                    m += pow(2, t - 4)
            if h > 11 or m > 59:
                continue
            else:
                h_s = str(h)
                m_s = str(m)
                m_s = m_s if len(m_s) == 2 else "0" + m_s
                ret.append(h_s + ":" + m_s)
        return ret
