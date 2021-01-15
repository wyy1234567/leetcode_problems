# Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.
def maximalSquare(matrix):
    row, col = len(matrix), len(matrix[0])
    res = float('-inf')
    dp = [[0 for _ in range(col)] for _ in range(row)]
    
    for i in range(row):
        dp[i][0] = int(matrix[i][0])
        res = max(res, dp[i][0] ** 2)     
            
    for j in range(col):
        dp[0][j] = int(matrix[0][j])
        res = max(res, dp[0][j] ** 2)     
        
    for i in range(1, row):
        for j in range(1, col):
            if matrix[i][j] == '1':
                dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1 
            else:
                dp[i][j] = 0
            res = max(res, dp[i][j] ** 2)           
    return res

def countSquares(matrix):
    row, col = len(matrix), len(matrix[0])
    dp = [[0 for _ in range(col + 1)] for _ in range(row + 1)]
    res = 0 
        
    for i in range(1, row + 1):
        for j in range(1, col + 1):
            if matrix[i-1][j-1] == 1:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                res += dp[i][j]
            else:
                dp[i][j] = 0
                    
    return res
        