# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        m = len(array)
        if m == 0 :
            return 0
        n = len(array[0])
        if n == 0 :
            return 0
        
        if target < array[0][0] or target > array[m-1][n-1] :
            return 0
        # 右上角开始
        i = 0
        j = n - 1
        while i < m and j >= 0 :
            if target == array[i][j]:
                return 1
            elif target > array[i][j] :    # 往下
                i += 1
            else :    # 往左
                j -= 1
        return 0