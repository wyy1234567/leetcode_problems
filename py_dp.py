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

def combinationSum4(nums, target):
    dp = [1] + [0] * target

    for i in range(1, len(dp)):
        for num in nums:
            if i >= num:
                dp[i] += dp[i - num]
    
    return dp[target]

# You are given coins of different denominations and a total amount of money. Write a function to compute the number of combinations that make up that amount. You may assume that you have infinite number of each kind of coin.
def coinChange(amount, coins):
    dp = [1] + [0] * amount 

    for coin in coins:
        for i in range(1, amount + 1):
            if i >= coin:
                dp[i] += dp[i-coin]

    return dp[amount]

# Given a non-empty array nums containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.       
def canPartition(nums):
    numsSum = sum(nums)

    if numsSum % 2 == 1:
        return False 
    
    numsSum = numsSum // 2 

    dp = [True] + [False] * numsSum

    for num in nums:
        for i in range(numsSum, -1, -1):
            if i > num:
                dp[i] = dp[i] or dp[i-num]
    
    return dp[numsSum]


def findTargetSumWays(nums, S):
    totalSum = sum(nums)
    if(S not in range(-1 * totalSum, totalSum + 1) ): return 0
    dp = [ [ 0 for j in range( totalSum*2 + 1 ) ] for i in range(len(nums))]
        
    ## BASE CASE ## FIRST ROW ##
    dp[0][totalSum + nums[0]] += 1
    dp[0][totalSum - nums[0]] += 1
        
    for i in range(1, len(nums)):
        for j in range( totalSum*2 + 1 ):
                
            if( j - nums[i] >= 0 and dp[i-1][j-nums[i]] > 0 ):          # left side
                dp[i][j] += dp[i-1][j-nums[i]]
                
            if( j + nums[i] <= totalSum*2 and dp[i-1][j+nums[i]] > 0 ): # right side
                dp[i][j] += dp[i-1][j+nums[i]]
        
    return dp[-1][totalSum + S]

# Given a number n. You have to get exactly n 'A' on the notepad by performing the minimum number of steps permitted. Output the minimum number of steps to get n 'A'.
def minSteps(n):
    dp = [float('inf')] * (n+1)
    dp[1] = 0

    for i in range(2, n+1):
        for j in range(2, i+1):
            if i % j == 0:
                dp[i] = min(dp[i], dp[i//j] + j)
                break

    return dp[n]

def knapsack(values, weights, maxWeightConstraint):
    row, col = len(values)+1, maxWeightConstraint+1
    dp = [[0 for _ in range(col)] for _ in range(row)]

    for i in range(1, row):
        for j in range(1, col):
            if j >= weights[i-1]:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-weights[i-1]]+values[i-1])
    
    return dp[row-1][col-1]

        