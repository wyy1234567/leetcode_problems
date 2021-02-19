def minRemoveToMakeValid(s: str) -> str:
        s = list(s)
        stack = []
        
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            elif s[i] == ')':
                if stack:
                    stack.pop()
                else:
                    s[i] = ''
                    
        while stack:
            s[stack.pop()] = ''
        return ''.join(s)

def exist(board, word):
        if not board:
            return False
        
        m = len(board)
        n = len(board[0])
        
        def helper(board, i, j, m, n, word): #find word with start index [i][j]
            if len(word) == 0:
                return True
            
            if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != word[0]:
                return False
            
            temp = board[i][j]
            board[i][j] = '#'
            res = helper(board, i+1, j, m, n, word[1:]) or helper(board, i-1, j, m, n, word[1:]) or helper(board, i, j+1, m, n, word[1:]) or helper(board, i, j-1, m, n, word[1:])
            board[i][j] = temp
            return res
        
        for i in range(m):
            for j in range(n):
                if helper(board, i, j, m, n, word):
                    return True

        return False


def spiralOrder(matrix):
        if not matrix:
            return []
        rows = len(matrix)
        columns = len(matrix[0])
        x = [0, 1, 0, -1]
        y = [1, 0, -1, 0]
        i, j, d = 0, 0, 0
        seen = [[False] * columns for _ in range(rows)]
        ans = []
        for _ in range(rows * columns):
            ans.append(matrix[i][j])
            seen[i][j] = True
            ni = i + x[d]
            nj = j + y[d]
            
            if 0 <= ni < rows and 0 <= nj < columns and not seen[ni][nj]:
                i = ni
                j = nj
            else:
                d = (d + 1) % 4
                i = i + x[d]
                j = j + y[d]
        
        return ans


def convert(s, numRows):
    if numRows == 1 or len(s) < numRows:
        return s 

    lines = [''] * numRows
    step, index = 1, 0 

    for char in s:
        lines[index] += char 

        if index == 0:
            step = 1 
        elif index == numRows - 1:
            step = -1 
        
        index += step 
    
    return ''.join(lines)


def generateParenthesis(n):
    result = []

    def backtrack(s, left, right):
        if len(s) == 2 * n:
            result.append(s)
            return 

        if left < n:
            backtrack(s + '(', left + 1, right)
        if right < left:
            backtrack(s + ')', left, right + 1)

    backtrack('', 0, 0)
    return result


def strStr(haystack, needle):

    if not needle:
        return 0 


    for i in range(len(haystack) - len(needle) + 1):
        for j in range(len(needle)):
            if haystack[i + j] != needle[j]:
                break 
            if j == len(needle) - 1:
                return i 
    
    return -1


def minWindow(s, t):
    if not s or not t:
        return ""

    dict_t = {}
    for c in t:
        dict_t[c] = dict_t.get(c, 0) + 1
    required = len(dict_t)
    left, right, formed = 0, 0, 0
    window = {}
    ans = float('inf'), None, None 

    while right < len(s):
        char = s[right]

        window[char] = window.get(char, 0) + 1 

        if char in dict_t and window[char] == dict_t[char]:
            formed += 1 

        while left < right and formed == required:
            char = s[left]

            if right - left + 1 < ans[0]:
                ans = (right - left + 1, left, right)
            
            window[char] -= 1 

            if char in dict_t and window[char] < dict_t[char]:
                formed -= 1 
            
            left += 1 

        right += 1

    return "" if ans[0] == float('inf') else s[ans[1]:ans[2]+1]


def decodeWays(s):
    dp = [0] * (len(s) + 1)
    dp[0] = 1 #1 way to decode empty string
    dp[1] = 0 if s[0] == '0' else 1

    for i in range(2, len(dp)):
        char = int(s[i-1])
        chars = int(s[i-2:i])

        if 0 < char <= 9:
            dp[i] += dp[i-1]
        
        if 10 <= chars <= 26:
            dp[i] += dp[i-2]

    return dp[-1]


def myPow(x, n):
    def function(base = x, exponent = abs(n)):
        if exponent == 0:
            return 1
        elif exponent % 2 == 0:
            return function(base * base, exponent // 2)
        else:
            return base * function(base * base, (exponent - 1) // 2)

    f = function()
    
    return float(f) if n >= 0 else 1/f

def myAtoi(s):
    s = s.strip()
    size = len(s)
    s += ' '
    isNegative = False
    i = 0
    ans = 0
    
    if s[i] == '+' or s[i] == '-':
        if s[i] == '-':
            isNegative = True 
        i += 1 
    
    if i >= size or not s[i].isdigit():
        return 0 
    
    while i <= size and s[i] == '0':
        i += 1 
    while i <= size and s[i].isdigit():
        ans += ans * 10 + int(s[i])
        i += 1
        
    if isNegative:
        ans *= -1 
    
    if ans < -1 * 2 ** 31:
        return -1 * 2 ** 31

    if ans > 2 ** 31 - 1:
        return 2**31 - 1
    
    return ans

# Input: s = "(1+(2*3)+((8)/4))+1"
# Output: 3
# Explanation: Digit 8 is inside of 3 nested parentheses in the string.
def maxDepth(s):
    stack = []
    res = 0
    
    for i in range(len(s)):
        char = s[i]
        
        if char == '(':
            stack.append('(')
        
        if char == ')':
            res = max(res, len(stack))
            stack.pop()
            
    return res

def ladderLength(beginWord, endWord, wordList):
    result = 0
    words = set(wordList)
    queue = [beginWord]
    seen = set()
    
    def construct_dict(word_list):
        d = {}
        for word in word_list:
            for i in range(len(word)):
                s = word[:i] + "_" + word[i+1:]
                d[s] = d.get(s, []) + [word]
        return d
    
    word_dict = construct_dict(wordList)
    
    if endWord not in words:
        return 0 
    
    while queue:
        size = len(queue)
        result += 1 
        
        for _ in range(size):
            curr = queue.pop(0)
            seen.add(curr)
            if curr == endWord:
                return result 
            
            for i in range(len(curr)):
                path = curr[:i] + '_' + curr[i+1:]
                neighbors = word_dict.get(path, [])
                for w in neighbors:
                    if w not in seen:
                        queue.append(w)
    return 0

def maxLengthBetweenEqualCharacters(s):
    index = {}
    result = -1 
    
    for i, char in enumerate(s):
        if char not in index:
            index[char] = [i]
        else:
            index[char].append(i)
            result = max(result, index[char][-1] - index[char][0]-1)
    
    return result

# Input: S = "aab"
# Output: "aba"
def reorganizeString(S):
    N = len(S)
    A = []
    s = sorted((S.count(x), x) for x in set(S))
    print(s)
    for c, x in sorted((S.count(x), x) for x in set(S)):
        if c > (N+1)/2: return ""
        A.extend(c * x)
    print(A)
    ans = [None] * N
    ans[::2], ans[1::2] = A[N//2:], A[:N//2]
    return "".join(ans)

def partitionLabels(S):
    dic = {}
    merged = []
    for i, c in enumerate(S):
        if c not in dic:
            dic[c] = [i, i]
        else:
            dic[c][-1] = i 
            
    intervals = []
    for val in dic.values():
        intervals.append(val)
    
    intervals.sort()
    merged = []
    
    for i in intervals:
        if not merged or i[0] > merged[-1][1]:
            merged.append(i)
        else:
            merged[-1][1] = max(merged[-1][1], i[1])
            
        
    return [(j-i+1) for i, j in merged]