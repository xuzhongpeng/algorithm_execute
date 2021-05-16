#
# @lc app=leetcode.cn id=54 lang=python3
#
# [54] 螺旋矩阵
#

# @lc code=start
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        while len(matrix) != 0:
            # 第一步 取第一行
            if self.isEmpty(matrix):break
            one = matrix.pop(0)
            for x in one:
                result.append(x)
            # 第二步 遍历列 取每一列最后一行的数
            if self.isEmpty(matrix):break
            for l in matrix:
                result.append(l.pop())
            # 第三步 取最后一行
            if self.isEmpty(matrix):break
            last = matrix.pop()
            last.reverse()
            for x in last:
                result.append(x)
            # 第四步 遍历列 取第一行
            if self.isEmpty(matrix):break
            m = matrix.copy()
            m.reverse()
            for l in m:
                result.append(l.pop(0))
        return result
    def isEmpty(self,list:List):
        return len(list)==0 or len(list[0])==0
           
 # @lc code=end


s = Solution()
print(s.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]))
