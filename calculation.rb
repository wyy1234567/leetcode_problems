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