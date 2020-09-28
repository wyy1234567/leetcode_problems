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

# 1513. Number of Substrings With Only 1s
# Given a binary string s (a string consisting only of '0' and '1's).Return the number of substrings with all characters 1's.Since the answer may be too large, return it modulo 10^9 + 7.

def num_sub(s)
    curr = 0
    ans = 0
    for i in 0...s.size do 
        if s[i] == '1' 
            curr += 1
            ans += curr
        else
            curr = 0
        end
    end
    ans % (10 ** 9 + 7)
end