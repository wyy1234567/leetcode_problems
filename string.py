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