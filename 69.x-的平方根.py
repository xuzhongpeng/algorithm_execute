#
# @lc app=leetcode.cn id=69 lang=python3
#
# [69] x 的平方根
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        def f(n, m):
            mid = (n+m)//2
            k = mid * mid
            if k <= x and (mid+1) * (mid+1) > x:
                return mid
            elif k < x:
                return f(mid+1, m)
            else:
                return f(0, mid)

        return f(0, x)
# @lc code=end


print(Solution().mySqrt(9))
