#
# @lc app=leetcode.cn id=387 lang=python3
#
# [387] 字符串中的第一个唯一字符
#

# @lc code=start
class Solution:
    def firstUniqChar(self, s: str) -> int:
        m = {}
        for (i,v) in enumerate(s):
            # print(i)
            if v in m:
                m[v].append(i)
            else:
                m[v] = [i]
        result = len(s)
        for x in m.values():
            if len(x) == 1 and x[0] < result:
                result = x[0]
        return -1 if result == len(s) else result
# @lc code=end

print(Solution().firstUniqChar('leetcode'))