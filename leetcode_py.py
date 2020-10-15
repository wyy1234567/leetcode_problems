import heapq
import math

def kClosest(points, K): 
    heap = []
    for (x, y) in points:
        dis = (x * x + y * y) * -1
        if len(heap) == K:
            heapq.heappushpop(heap, (dis, x, y))
        else:
            heapq.heappush(heap, (dis, x, y))
    return [(x, y) for (dis, x, y) in heap]

def winSum(nums, K):
    if not nums or K == 0: 
        return []
    
    initial_sum = 0
    for i in range(K):
        initial_sum += nums[i]
    
    start, last = 0, K
    res = [initial_sum]
    while last < len(nums): 
        initial_sum = initial_sum + nums[last] - nums[start]
        res.append(initial_sum)
        last += 1
        start += 1
    
    return res

def longestPalindrome(s):
    ss = set()

    for char in s: 
        if char in ss: 
            ss.remove(char)
        else:
            ss.add(char)
    
    if len(ss) == 0:
        return len(s)
    else: 
        return len(s) - len(ss) + 1

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
    
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None
        
        curr = head
        while curr: 
            new_node = Node(curr.val)
            next_node = curr.next
            curr.next = new_node
            new_node.next = next_node
            curr = next_node
        
        curr = head
        while curr:
            if not curr.random:
                curr.next.random = None
            else: 
                curr.next.random = curr.random.next
            
            curr = curr.next.next
        
        curr = head.next
        while curr: 
            curr.next = curr.next.next
            curr = curr.next

        return head.next

# Given a list of scores of different students, return the average score of each student's top five scores in the order of each student's id.
# Each entry items[i] has items[i][0] the student's id, and items[i][1] the student's score.  The average score is calculated using integer division.
# Example 1:
# Input: [[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]
# Output: [[1,87],[2,88]]
# Explanation: 
# The average of the student with id = 1 is 87.
# The average of the student with id = 2 is 88.6. But with integer division their average converts to 88.

def highFive(slist):
    shash = {}
    for (x, y) in slist:
        if x not in shash:
            shash[x] = [y] #value is a heap: [sum, avg]
        else:
            if len(shash[x]) == 5:
                heapq.heappushpop(shash[x], y)
            else:
                heapq.heappush(shash[x], y)

    print(shash)
    res = []
    for k in shash:
        avg = math.floor(sum(shash[k]) / len(shash[k]))
        res.append([k, avg])
    return res

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
    
    def findSubtree(self, root):
        self.max_sum = float('-inf')
        self.max_node = None

        def nodeSum(root): 
            if not root:
                return 0
            
            left_sum = nodeSum(root.left)
            right_sum = nodeSum(root.right)
            curr = root.val + left_sum + right_sum
            if curr > self.max_sum:
                self.max_sum = curr
                self.max_node = root
            return curr
        
        nodeSum(root)
        return self.max_node

def validWordAbbreviation(self, word, abbr):
        if not word or not abbr or abbr[0] == '0':
            return False
        
        i, j = 0, 0
        while i < len(word) and j < len(abbr):
            if abbr[j].isdigit():
                num = 0
                while j < len(abbr) and abbr[j].isdigit():
                    num = num * 10 + (ord(abbr[j]) - ord('0'))
                    j += 1 
                i += num 
            else:
                if abbr[j] == word[i]:
                    i += 1 
                    j += 1 
                else:
                    return False 
            
        if i == len(word) and j == len(abbr):
            return True
        else: 
            return False

class Solution:
    """
    @param: nums: a sorted integer array
    @param: lower: An integer
    @param: upper: An integer
    @return: a list of its missing ranges
    """
    def findMissingRanges(self, nums, lower, upper):
        # write your code here
        self.ans = []
        
        def addRange(low, high):
            if low > high:
                return
            if low == high:
                self.ans.append(str(low))
                return 
            string = str(low) + '->' + str(high)
            self.ans.append(string)
            
        if len(nums) == 0:
            addRange(lower, upper)
            return self.ans
        
        addRange(lower, nums[0] - 1)
        for i in range(1, len(nums)):
            addRange(nums[i - 1] + 1, nums[i] - 1)
        
        addRange(nums[len(nums) - 1] + 1, upper)
        return self.ans 

    
#valid num: 符号+浮点数+e+符号+整数，前后可以有空格
def isNumber(self, s: str) -> bool:
    i = 0
    s = s.strip() + ' '
    size = len(s) - 1

    if s[i] == '+' or s[i] == '-':
        i += 1
    
    point, num = 0, 0

    while s[i].isdigit() or s[i] == '.':
        if s[i].isdigit():
            num += 1
        if s[i] == '.':
            point += 1
        i += 1

    if point > 1 or num < 1:
        return False
    
    if s[i] == 'e':
        i += 1
        if s[i] == '+' or s[i] == '-':
            i += 1
        
        if i == size:
            return False 
        
        while i < size:
            if not s[i].isdigit():
                return False
            i += 1
    
    return i == size

def coinChange(coins, amount):
    coins.sort()
    dp = [amount + 1] * (amount + 1)
    dp[0] = 0

    for i in range(1, len(dp)):
        for num in coins:
            if num <= i:
                dp[i] = min(dp[i], dp[i - num] + 1)
    
    if dp[amount] > amount:
        return -1
    else:
        return dp[amount]

def dfs(board, i, j, word):
    if len(word) == 0:
        return True
    
    if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[0]:
        return False
    
    temp = board[i][j]
    board[i][j] = '#'
    res = dfs(board, i+1, j, word[1:]) or dfs(board, i-1, j, word[1:]) or dfs(board, i, j + 1, word[1:]) or dfs(board, i, j-1, word[1:])
    board[i][j] = temp
    return res    

def exist(board, word) -> bool:
    if not board:
        return False
    
    for i in range(len(board)):
        for j in range(len(board[0])):
            return dfs(board, i, j, word)
     
def submerge(grid, i, j, m, n):
    x = [0, 1, -1, 0]
    y = [1, 0, 0 -1]
    queue = []
    queue.append([i, j])
    grid[i][j] = '0'

    while len(grid) > 0:
        curr = queue.pop(0)
        curr_x = curr[0]
        curr_y = curr[1]

        for i in range(4):
            adj_x = curr_x + x[i]
            adj_y = curr_y + y[i]

            if adj_x < 0 or adj_x > m or adj_y < 0 or adj_y > n:
                continue

            if grid[adj_x][adj_y] == '1':
                grid[adj_x][adj_y] = '0'
                queue.append([adj_x, adj_y])

def numIsland(grid):
    if not grid or len(grid) == 0 or len(grid[0]) == 0:
        return 0
    
    m = len(grid)
    n = len(grid[0])
    ans = 0

    for i in range(m):
        for j in range(n):
            if grid[i][j] == '1':
                ans += 1
                submerge(grid, i, j, m, n)
    return ans

def letterCombinations(digits):
    if not digits:
        return []

    phone = {'2': ['a', 'b', 'c'],
             '3': ['d', 'e', 'f'],
             '4': ['g', 'h', 'i'],
             '5': ['j', 'k', 'l'],
             '6': ['m', 'n', 'o'],
             '7': ['p', 'q', 'r', 's'],
             '8': ['t', 'u', 'v'],
             '9': ['w', 'x', 'y', 'z']}
    
    ans = []

    def backtrack(res, words):
        if len(words) == 0:
            ans.append(res)
        else:
            for letter in phone[words[0]]:
                backtrack(res+letter, words[1:])
    
    backtrack('', digits)
    return ans

#in-place modification, void-function
def nextPermutation(nums):
    if not nums or len(nums) == 0 or len(nums) == 1:
        return
    
    pointer = len(nums - 2)
    while pointer >= 0 and nums[pointer] >= nums[pointer + 1]:
        pointer -= 1
    
    if pointer < 0:
        nums.sort()
        return 
    
    min_gap = float('inf')
    index = 0
    
    for i in range(pointer + 1, len(nums)):
        if nums[i] > nums[pointer]:
            if nums[i] - nums[pointer] < min_gap:
                index = i
                min_gap = nums[i] - nums[pointer]
    
    temp = nums[pointer]
    nums[pointer] = nums[index]
    nums[index] = temp
    nums[(pointer + 1):] = sorted(nums[(pointer + 1):])

def spiralOrder(matrix):
    if not matrix:
        return []
    rows = len(matrix)
    columns = len(matrix[0])
    copy = [[False] * columns for _ in range(rows)]
    ans = []
    r, c, d = 0, 0, 0
    x = [1, 0, -1, 0]
    y = [0, 1, 0, -1]

    for _ in range(rows * columns):
        ans.append(matrix[r][c])
        copy[r][c] = True
        nc = c + x[d]
        nr = r + y[d]

        if 0<= nc < columns and 0 <= nr < rows and not copy[nr][nc]:
            r = nr 
            c = nc
        else:
            d = (d + 1) % 4
            r = r + y[d]
            c = c + x[d]
    
    return ans


def maxSubstr(s): 
    if len(s) < 2:
        return s 
    
    ans = ''

    def findStr(s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            subString = s[left:right+1]
            if len(subString) > len(ans):
                ans = subString 
            left -= 1
            right += 1
    
    for i in range(len(s)):
        findStr(s, i, i)
        findStr(s, i, i + 1)
    
    return ans

def maxSublist(nums):
    dp = [float('-inf')] * (len(nums) + 1)
    dp[0] = 0
    ans = float('-inf')
    for i in range(1, len(dp)):
        dp[i] = max(nums[i - 1], dp[i - 1] + nums[i - 1])
        if dp[i] > ans:
            ans = dp[i]
    
    return ans

def shortestPath(grid):   
    m = len(grid)
    n = len(grid[0])

    if grid[0][0] == 0 or grid[m-1][n-1] == 0:
        return -1
    
    helper = [[float('inf')*n for _ in range(m)]]
    helper[0][0] = 1

    queue = [[0,0]]
    x = [-1,1,0,0,-1,1,-1,1]
    y = [0,0,1,-1,1,1,-1,-1]
    while len(queue) > 0:
        curr = queue.pop(0)
        cx = curr[0]
        cy = curr[1]
        for i in range(8):
            adj_x = cx + x[i]
            adj_y = cy + y[i]

            if adj_x >= 0 and adj_x < n and adj_y >= 0 and adj_y < m and grid[adj_x][adj_y] == 0 and helper[adj_x][adj_y] > helper[cx][cy] + 1:
                helper[adj_x][adj_y] = min(helper[adj_x][adj_y], helper[cx][cy] + 1)
                queue.append([adj_x, adj_y])
    
    if helper[m-1][n-1] == float('inf'):
        return -1
    else:
        return helper[m-1][n-1]


from collections import OrderedDict 
class LRUCache:
    
    def __init__(self, capacity):
        self.od = OrderedDict()
        self.capacity = capacity
    
    def get(self, key):
        if key in self.od:
            val = self.od[key]
            del self.od[key]
            self.od[key] = val
            return val
        else:
            return -1 
    
    def put(self, key, value):
        if key in self.od:
            del self.od[key]
            self.od[key] = value 
        else:
            if len(self.od) < self.capacity:
                self.od[key] = value
            else:
                firstKey = next(iter(self.od.keys()))
                del self.od[firstKey]
                self.od[key] = value



#words list: ['a','b',':','d'], find a way to encode it, return a string
def encode(words):
    ans = ''
    for w in words:
        for char in w:
            if char == ':':
                ans += '::'
            else:
                ans += char
        ans += ':;'
    return ans

#give an encoded string, decode it into a list of words
def decode(string):
    ans = []
    item = ''
    i = 0
    while i < len(string):
        if string[i] == ':':
            if string[i + 1] == ';':
                ans.append(item)
                item = ''
                i += 2
            else:
                item += string[i]
                i += 2            
        else:
            item += string[i]
    return ans

#return the longest file path length
def filePath(string):
    ans = 0
    levelHash = {0:0}
    for line in string.split('\n'):
        name = line.lsplit('\t') #leading split string
        level = len(line) - len(name)
        if '.' in name:
            ans = max(ans, levelHash[level] + len(name))
        else:
            levelHash[level + 1] = levelHash[level] + len(name) + 1
    return ans



class ReadFile:
    def __init__(self):
        self.buffer = [None] * 4
        self.head, self.tail = 0, 0
    
    def read(self, buf, n):
        i = 0
        while i < n:
            if self.head == self.tail:
                self.head = 0
                # self.tail = Reader.read4(self.buffer) #api calls here
                if self.tail == 0:
                    break
            while i < n and self.head < self.tail:
                buf[i] = self.buffer[self.head]
                i += 1
                self.head += 1
        return i


#convert given string to integer
#vaild string: '+/-'+digits+'.'+digits
def atoi(s):
    s = s.strip()
    if len(s) == 0 or not s:
        return 0
    size = len(s)
    s += ' '
    ans = 0
    isNegative = False
    i = 0 
    if s[i] == '+' or s[i] == '-':
        if s[i] == '-':
            isNegative = True 
        i += 1
    
    if i >= size or not s[i].isdigit():
        return 0 
    
    while i < size and s[i] == '0':
        i +=  1
    
    while i < size and s[i].isdigit():
        ans = ans * 10 + int(s[i])
        i += 1

    if isNegative:
            ans *= -1 
        
    if ans < -1 * 2 ** 31:
        return -1 * 2 ** 31
    
    if ans > 2 ** 31 - 1:
        return 2**31 - 1
        
    return ans 
        

# [[1,3],[2,6],[8,10],[15,18]] => [[1,6],[8,10],[15,18]]
def mergeIntervals(intervals):
    intervals.sort(key = lambda l:l[0])
    ans = []
    for i in intervals:
        if not ans or i[0] > ans[-1][1]:
            ans.append(i)
        else:
            ans[-1][1] = max(ans[-1][1], i[1])
    return ans


def insertInterval(intervals, newInterval):
    left = newInterval[0]
    right = newInterval[1]
    small = []
    large = []

    for i in intervals:
        if i[1] < left:
            small.append(i)
        elif i[0] > right:
            large.append(i)
        else:
            left = min(left, i[0])
            right = max(right, i[1])
    
    return small + [[left, right]] + large

def shortenWord(s, prefix):
    if prefix >= len(s) - 2:
        return s 
    ans = ''
    ans = s[0:prefix] + str(len(s) - 1 - prefix) + s[len(s)-1:]
    return ans

def wordAbbreviation(words):
    count = {}
    size = len(words)
    prefix = [0] * size 
    ans = [''] * size

    for i in range(size):
        prefix[i] = 1
        ans[i] = shortenWord(words[i], 1)
        if ans[i] not in count:
            count[ans[i]] = 1
        else:
            count[ans[i]] += 1
    
    while True:
        allUnique = True
        for i in range(size):
            if count[ans[i]] > 1:
                prefix[i] += 1
                ans[i] = shortenWord(words[i], prefix[i])
                if ans[i] not in count:
                    count[ans[i]] = 1
                else:
                    count[ans[i]] += 1
                allUnique = False
        if allUnique:
            break
    
    return ans


import random
class LoadBalance:
    def __init__(self):
        self.sset = set()

    # @param {int} server_id add a new server to the cluster 
    # @return nothing
    def add(self, server_id):
        self.sset.add(server_id)

    # @param {int} server_id remove a bad server from the cluster
    # @return nothing
    def remove(self, server_id):
        if server_id in self.sset:
            self.sset.remove(server_id)
        else:
            return None

    # @return {int} pick a server in the cluster randomly with equal probability
    def pick(self):
        if self.sset:
            return random.sample(self.sset, 1)[0]
        else:
            return None


def longestSub(s):
    start = 0
    ans = 0
    curr = 0
    dic = {}

    for i in range(len(s)):
        if s[i] in dic and dic[s[i]] >= start:
            ans = max(curr, ans)
            curr = i - dic[s[i]]
            start = dic[s[i]] + 1
        else:
            curr += 1
        dic[s[i]] = i 

    return max(ans, curr)


def wordBreak(s, wordDict):
    dp = [False] * (len(s) + 1)
    dp[0] = True

    for i in range(len(s)):
        for j in range(i, len(s)):
            if dp[i] and s[i:j + 1] in wordDict:
                dp[j + 1] = True
    
    return dp[-1]

memo = {}
def wordBreakII(s, wordDict):
    return findWord(s, wordDict)

#functions will return an array of possible combinations
#meanwhile add {string:combination} to memo hash
def findWord(s, wordDict):
    if not s:
        return []

    if s in memo:
        return memo[s]
    
    partitions = []

    if s in wordDict:
        partitions.append(s)

    for i in range(1, len(s)):
        word = s[:i]
        if word not in wordDict:
            continue

        sub = findWord(s[i:], wordDict)   #if the word is in the dict, find the partitions of the remaining string
        for w in sub:
            partitions.append(word + ' ' + w)
    memo[s] = partitions
    return partitions


def findPeak(nums):
    left = 0 
    right = len(nums) - 1
        
    while left + 1 < right:
        mid = left + (right - left) // 2 
        if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
            return mid 
        elif nums[mid] > nums[mid - 1] and nums[mid] < nums[mid + 1]:
            left = mid 
        else:
            right = mid 
        
    if nums[left] > nums[right]:
        return left
    return right

def findFirstIndex(nums, target):

    left = 0 
    right = len(nums)

    while left + 1 < right:
        mid = left + (right - left) // 2
        if nums[mid] < target:
            left = mid 
        else:
            right = mid 
    
    if nums[left] >= target:
        return left 
    
    return right

def findRange(nums, target):
    if not nums:
        return [-1, -1]
    
    left = findFirstIndex(nums, target)
    right = findFirstIndex(nums, target + 1) - 1 
    if left >= len(nums) or nums[left] != target:
        return [-1, -1]
    return [left, max(left, right)]


def closestNumber(nums, target):
    
    if not nums:
        return -1 
    
    left = 0
    right = len(nums) - 1 

    while left + 1 < right:
        mid = left + (right - left) // 2

        if nums[mid] == target:
            return mid 
        elif nums[mid] < target:
            left = mid 
        else:
            right = mid 
    
    if abs(nums[left] - target) < abs(nums[right] - target):
        return left
    
    return right