#
# @lc app=leetcode.cn id=1249 lang=python3
#
# [1249] 移除无效的括号
#
import re
from typing import List
# @lc code=start
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        leftParentheses: List[int] = []
        result = []
        n = 0
        for i,v in enumerate(s):
            if v == '(':
                leftParentheses.append(i-n)
                result.append(v)
            elif v == ')':
                if len(leftParentheses) != 0:
                    result.append(v)
                    leftParentheses.pop()
                else:
                    n += 1
            else:
                result.append(v)
        # 删除多余括号
        leftParentheses.reverse()
        for i,v in enumerate(leftParentheses):
            result.pop(v)
        return ''.join(result)




# @lc code=end

s = Solution()
print(s.minRemoveToMakeValid('s(f)))(d)d)d('))