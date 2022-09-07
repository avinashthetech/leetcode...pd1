class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        dp = [[-1 for _ in range(len(obstacleGrid[0]))] for _ in range(len(obstacleGrid))] 
        
        if obstacleGrid[0][0] == 1:
            return 0
        
        def topDown(i, j):
            if i == 0 and j == 0:
                return 1
            if i < 0 or j < 0:
                return 0
            if i >= 0 and j >= 0 and obstacleGrid[i][j] == 1:
                return 0
            if dp[i][j] != -1:
                return dp[i][j]
            top = topDown(i-1, j)
            left = topDown(i, j - 1)
            dp[i][j] = top + left
            return dp[i][j]
        
        return topDown(len(obstacleGrid) - 1, len(obstacleGrid[0]) - 1)
            
        
        