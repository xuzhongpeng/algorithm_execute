#
# @lc app=leetcode.cn id=240 lang=python3
#
# [240] 搜索二维矩阵 II
#

# @lc code=start
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0:
            return False
        x = len(matrix[0])-1
        while x >= 0:
            if matrix[0][x] == target:
                return True
            elif matrix[0][x] < target:
                y = 0
                while y < len(matrix):
                    n = matrix[y][x]
                    if n == target:
                        return True
                    elif n < target:
                        y += 1
                    else:
                        break
            x -= 1
        return False


# @lc code=end
print(Solution().searchMatrix([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [
      11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]], 19))
