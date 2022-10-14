


# def countBits(self, num: int) -> List[int]:
#     counter = [0]
#     for i in range(1, num+1):
#         counter.append(counter[i >> 1] + i % 2)
#     return counter




class Solution:
    def countBits(self, num: int) -> List[int]:
        dp = [0]
        for i in range(1, num + 1):
            if i % 2 == 1:
                dp.append(dp[i - 1] + 1)
            else:
                dp.append(dp[i // 2])
        return dp