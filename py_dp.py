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

def lengthOfLIS(nums):
    dp = [1] * len(nums)
    res = 0 
        
    for i in range(len(nums)):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
        res = max(res, dp[i])
        
    return res

# Given two lists, scores and ages, where each scores[i] and ages[i] represents the score and age of the ith player, respectively, return the highest overall score of all possible basketball teams.
def bestTeamScore(scores, ages):
    n = len(scores)
    players = [[a, s] for a, s in zip(ages, scores)]
    players.sort(reverse = True)

    ans = 0
    dp = [0]*n

    for i in range(n):
        score = players[i][1]
        dp[i] = score
        for j in range(i):
            if players[j][1] >= players[i][1]:
                dp[i] = max(dp[i], dp[j] + score)
        ans = max(ans, dp[i])

    return ans


def minCost(n, cuts):
    cuts = sorted(cuts + [0, n])
    k = len(cuts)
    dp = [[0] * k for _ in range(k)]
    for d in range(2, k):
        for i in range(k - d):
            dp[i][i + d] = min(dp[i][m] + dp[m][i + d] for m in range(i + 1, i + d)) + cuts[i + d] - cuts[i]

    return dp[0][k - 1]


def trapWater(height):
    size = len(height)
    left, right = [0] * size, [0]*size
    left[0] = height[0]
    right[-1] = height[-1]
    res = 0

    for i in range(1, size):
        left[i] = max(height[i], left[i-1])
    
    for i in range(size-2, -1, -1):
        right[i] = max(height[i], right[i+1])
    
    for i in range(1, size -1):
        res += min(left[i], right[i]) - height[i]
    
    return res


def findNumberOfLIS(nums):
    n = len(nums)
    if n <= 1:
        return n
    lengths = [1] * n #lengths[i] = longest ending in nums[i]
    counts = [1] * n #count[i] = number of longest ending in nums[i]
    
    longest = float('-inf')
    result = 0 
    for i, num in enumerate(nums):
        for j in range(i):
            if num > nums[j]:
                if lengths[j] >= lengths[i]:
                    lengths[i] = lengths[j] + 1 
                    counts[i] = counts[j]
                elif lengths[j] + 1 == lengths[i]:
                    counts[i] += counts[j]
        longest = max(longest, lengths[i])
    
    for i, c in enumerate(counts):
        if lengths[i] == longest:
            result += c

    return result
            

from math import sqrt, ceil
def numSquares(n):
    limit = ceil(sqrt(n)) + 1
    dp = [float('inf')] * (n+1)
    dp[0] = 0

    for num in range(1, limit):
        for i in range(num**2, n+1):
            dp[i] = min(dp[i], 1+dp[i-num**2])
    return dp[-1]

def minPathSum(grid):
    rows, cols = len(grid), len(grid[0])
    
    #initialize the first row 
    for i in range(1, cols):
        grid[0][i] += grid[0][i-1]
    
    #initialize the first column
    for i in range(1, rows):
        grid[i][0] += grid[i-1][0] 
        
    for i in range(1, rows):
        for j in range(1, cols):
            grid[i][j] += min(grid[i-1][j], grid[i][j-1])
    
    return grid[rows-1][cols-1]


def countSubstrings(s):
    dp = [[False for _ in range(len(s))] for _ in range(len(s))]
    count = 0 
    for i in range(len(s)-1, -1, -1):
        dp[i][i] = True 
        count += 1 
        for j in range(i+1, len(s)):
            if j == i+1 and s[i] == s[j]:
                dp[i][j] = True 
                count += 1 
            if j > i+1 and dp[i+1][j-1] and s[i] == s[j]:
                dp[i][j] = True
                count += 1
    return count


def longestCommonSubsequence(text1, text2):
    rows, cols = len(text1), len(text2)
    dp = [[0 for _ in range(cols + 1)] for _ in range(rows + 1)]
    
    for i in range(1, rows + 1):
        for j in range(1, cols + 1):
            if text1[i-1] == text2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1 
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                
    return dp[rows][cols]


def minDistance(word1: str, word2: str) -> int:
    rows, cols = len(word1), len(word2)
    dp = [[0 for _ in range(cols+1)] for _ in range(rows + 1)]
    
    for i in range(rows + 1):
        for j in range(cols + 1):
            if i == 0 or j == 0:
                dp[i][j] = i+j
            elif word1[i-1] == word2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + 1 
    
    return dp[rows][cols]


#number of unique bst with input integer n
def numTrees(n):
    dp = [0] * (n+1)
    dp[0] = dp[1] = 1 
    for i in range(2, n+1):
        for j in range(1, i+1):
            dp[i] += dp[j-1] * dp[i-j]
    return dp[n]
        
# Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.
# An interleaving of two strings s and t is a configuration where they are divided into non-empty substrings such that:
# Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac" Output: true
def isInterleave(s1, s2, s3):

    if len(s1) + len(s2) != len(s3):
        return False 
    
    dp = [[False for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]
    dp[0][0] = True 
    
    for i in range(len(s3)):
        for l1 in range(i+2):
            if l1 > len(s1):
                continue 
            l2 = i+1-l1 
            if l2 > len(s2):
                continue 
            
            if (l1 > 0 and dp[l1-1][l2] and s3[i] == s1[l1-1]) or (l2 > 0 and dp[l1][l2-1] and s2[l2 - 1] == s3[i]):
                dp[l1][l2] = True 
    
    return dp[len(s1)][-1]


def minimumTotal(triangle):
    rows = len(triangle)
    
    for r in range(rows - 2, -1, -1):
        for c in range(len(triangle[r])):
            triangle[r][c] += min(triangle[r+1][c], triangle[r+1][c+1])
    return triangle[0][0]


def uniquePaths(m, n):
    matrix = [[1 for _ in range(n)] for _ in range(m)]
    
    for i in range(1, m):
        for j in range(1, n):
            matrix[i][j] = matrix[i-1][j] + matrix[i][j-1]
            
    return matrix[m-1][n-1]

# Input: words = ["a","b","ba","bca","bda","bdca"]
# Output: 4
# Explanation: One of the longest word chain is "a","ba","bda","bdca".
def longestStrChain(words):

    dp = {}
    result = 1 

    for word in sorted(words, key=len):
        dp[word] = 1 

        for i in range(len(word)):
            prev = word[:i] + word[i+1:]
            
            if prev in dp:
                dp[word] = max(dp[prev]+1, dp[word])
                result = max(dp[word], result)
    
    return result