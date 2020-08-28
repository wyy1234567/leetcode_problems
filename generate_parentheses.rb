# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

# For example, given n = 3, a solution set is:

# [
#   "((()))",
#   "(()())",
#   "(())()",
#   "()(())",
#   "()()()"
# ]


def generate_parenthesis(n)
    ans = []
    backtrack(ans, '', 0, 0, n)
    ans
end

def backtrack(ans, curr, open_num, close_num, n)
    if curr.size == n * 2
        ans << curr
        return ans
    end

    if open_num < n 
        backtrack(ans, curr + '(', open_num + 1, close_num, n)
    end
    
    if close_num < open_num
        backtrack(ans, curr + ')', open_num, close_num + 1, n)
    end
end

print generate_parenthesis(3)