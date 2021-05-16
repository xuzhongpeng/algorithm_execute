#
# @lc app=leetcode.cn id=67 lang=python3
#
# [67] 二进制求和
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        x, y = int(a, 2), int(b, 2)
        while y:
            answer = x ^ y
            carry = (x & y) << 1
            x, y = answer, carry
        # 讲10进制转为二进制
        return bin(x)[2:]

# @lc code=end
print(Solution().addBinary('101','11'))

x=1110
y=1011
a=int(str(x),2)
b=int(str(y),2)
print(bin(a+b)[2:])
print(a)
print(bin(a)[2:])
