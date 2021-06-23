#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        i=2
        f1=1
        f2=2
        now = f1 if n==1 else f2 if n==2 else  0
        while i<n:
            now = f1 + f2
            f1,f2 = f2,now
            i += 1
        return now
# @lc code=end

print(Solution().climbStairs(2))