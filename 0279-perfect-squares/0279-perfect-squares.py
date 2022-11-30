class Solution:
    
    def numSquares(self, n: int) -> int:
        dp = [n + 1] * (n + 1)
        dp[0] = 0
        for num in range(1, n + 1):
            num *= num
            for t in range(num, n + 1):
                dp[t] = min(dp[t], 1 + dp[t - num])

        return dp[n]
        
        
        
        
        
#         dp = [inf] * (n+1)
#         for i in range(1,n+1):
#             i_sq = pow(i,2)
#             if i_sq <= n:
#                 dp[i_sq] = 1
                
#             for j in range(i):
#                 dp[i] = min(dp[i],dp[i-j]+dp[j])

#         return dp[n]
        