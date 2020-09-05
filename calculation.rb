# Given two binary strings, return their sum (also a binary string).
# The input strings are both non-empty and contains only characters 1 or 0.

# Example 1:
# Input: a = "11", b = "1"
# Output: "100"

def add_binary(a, b)
    ca = a.size - 1
    cb = b.size - 1
    carry = 0
    ans = ''
    while ca >= 0 && cb >= 0 do 
        diga = a[ca].to_i
        digb = b[cb].to_i
        sum = diga + digb + carry
        ans.prepend((sum % 2).to_s)
        carry = sum / 2
        ca -= 1
        cb -= 1
    end
    
     while ca >= 0
        diga = a[ca].to_i
        sum = diga + carry
        ans.prepend((sum % 2).to_s)
        carry = sum / 2
        ca -= 1
    end    

    while cb >= 0
        digb = b[cb].to_i
        sum = digb + carry
        ans.prepend((sum % 2).to_s)
        carry = sum / 2
        cb -= 1
    end

    carry > 0 ? ans.prepend(carry.to_s) : ans
    ans
end


# You are climbing a stair case. It takes n steps to reach to the top.
#Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
    
#Example 1:
#Input: 2
#Output: 2
#Explanation: There are two ways to climb to the top.
#1. 1 step + 1 step
#2. 2 steps

#Fibonacci number
def climb_stairs(n)
    return 1 if n == 1
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2
    for i in 3..n do 
        dp[i] = dp[i - 1] + dp[i - 2]
    end
    dp[n]
end