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