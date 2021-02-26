# https://leetcode.com/problems/powx-n/
def pow_recursion(x, n):
    if n == 0:
        return 1 
    
    if n < 0:
        return 1.0 / pow_recursion(x, -n)
    
    if n % 2 == 0:
        return pow_recursion(x, n // 2) * pow_recursion(x, n // 2)
    else:
        return pow_recursion(x, n // 2) * pow_recursion(x, n // 2) * x