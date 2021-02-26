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


def pow_iteration(x, n):
    if n == 0 or x == 1:
        return 1 
    if n == 1:
        return x 
    result = 1 

    if n < 0:
        return 1 / (x * pow_iteration(x, -(n+1)))
    
    while n > 1:
        if n % 2 == 1:
            result = result * n 
        
        x = x * x 
        n //= 2
    result *=  x 

    return result