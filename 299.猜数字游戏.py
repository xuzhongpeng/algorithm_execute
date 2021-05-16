#
# @lc app=leetcode.cn id=299 lang=python3
#
# [299] 猜数字游戏
#

# @lc code=start
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        cows = 0
        array = [0]*10
        i = 0
        while i < len(secret):
            if secret[i] == guess[i]:
                bulls+=1
            else:
                a =  int(secret[i])
                b = int(guess[i])
                if array[a] < 0:
                    cows += 1
                if array[b] > 0:
                    cows += 1
                array[a]+=1
                array[b]-=1
            i += 1
        return str(bulls)+'A'+str(cows)+'B'


# @lc code=end
print(Solution().getHint('1122', '2211'))
