#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        def p(f):
            if f==1: return 1
            elif f == 2: return 2
            return p(f-1)+2
        return p(n)
# @lc code=end

print(Solution().climbStairs(5))