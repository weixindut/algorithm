#!/usr/bin/env python
# coding=utf-8
class Solution(object):
    def bubblesort(self, arr):
        for i in range(0, len(arr)):
            for k in range(0, len(arr) - i - 1):
                if arr[k] > arr[k + 1]:
                    arr[k], arr[k+1]= arr[k+1], arr[k]
    def insertsort(self, arr):
        for i in range(1, len(arr)):
            for j in range(i, 0, -1):
                if arr[j-1] > arr[j]:
                    arr[j], arr[j-1] = arr[j-1], arr[j]
    def selectionsort(self, arr):
        for i in range(len(arr)):
            min_i = i
            for j in range(i + 1, len(arr)):
                if arr[j] <arr[min_i]:
                    min_i = j
            arr[i], arr[min_i] = arr[min_i], arr[i]

    def mergesort_1(self, arr):
        self.aux = [0] * len(arr)
        self.msort(arr, 0, len(arr) - 1)
    def msort(self, arr, start, end):
        if start >= end:
            return
        mid = start + (end - start)/2
        self.msort(arr, start, mid)
        self.msort(arr, mid + 1, end)
        self.merge(arr, start, mid, end)

    def mergesort_2(self, arr):
        self.aux = [0] * len(arr)
        sz = 1
        while sz < len(arr):
            k = 0
            while k < len(arr) - sz:
                self.merge(arr, k , k + sz -1 , min(k + sz + sz - 1, len(arr) - 1))
                k += sz + sz
            sz = sz + sz
    def merge(self, arr, start, mid, end):
        for i in range(start, end + 1):
            self.aux[i] = arr[i]
        i = start
        j = mid + 1
        k = start
        while k <= end:
            if i > mid:
                arr[k] = self.aux[j]
                j += 1
            elif j > end:
                arr[k] = self.aux[i]
                i += 1
            elif self.aux[i] < self.aux[j]:
                arr[k] = self.aux[i]
                i += 1
            else:
                arr[k] = self.aux[j]
                j += 1
            k += 1
    
    def quicksort(self, arr):
        self.qsort(arr, 0 , len(arr) - 1)
    def qsort(self, arr, lo, hi):
        if hi <= lo :
            return
        j = self.partion(arr, lo, hi)
        self.qsort(arr, lo, j - 1)
        self.qsort(arr, j + 1, hi)
    def partion(self, arr, lo, hi):
        i = lo + 1
        j = hi
        while True:
            while arr[i] < arr[lo]:
                i += 1
                if i == hi:
                    break
            while arr[j] > arr[lo]:
                j -= 1
                if j == lo:
                    break
            if i >= j:
                break
            arr[i], arr[j] = arr[j], arr[i]

        arr[j], arr[lo] = arr[lo], arr[j]
        return j
            



if __name__ == "__main__":
    arr = [7,6,5,4,3,2,1,0]
    so = Solution()
    so.quicksort(arr)
    print arr
