# Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.
# Note:
# The length of both num1 and num2 is < 5100.
# Both num1 and num2 contains only digits 0-9.
# Both num1 and num2 does not contain any leading zero.
# You must not use any built-in BigInteger library or convert the inputs to integer directly.

def add_strings(num1, num2)
    i = num1.size - 1
    j = num2.size - 1
    carry = 0
    ans = ''
    while i >= 0  && j >= 0 do 
        sum = (num1[i].ord) - ("0".ord) + num2[j].ord - ("0".ord) + carry
        ans = (sum % 10).to_s + ans
        carry = sum / 10
        i -= 1
        j -= 1
    end
    
    while i >= 0 do 
        sum = num1[i].ord - '0'.ord + carry
        ans = (sum % 10).to_s + ans
        carry = sum / 10
        i -= 1
    end
    
    while j >= 0 do 
        sum = num2[j].ord - '0'.ord + carry
        ans = (sum % 10).to_s + ans
        carry = sum / 10
        j -= 1
    end
    
    if carry > 0 
        ans = carry.to_s + ans
    end
    ans
end