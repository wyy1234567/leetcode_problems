# Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

def longest_palindrome(s)
    @max = 0
    @low = nil

    return s if s.length < 2

    def expand(s, i, j)
        while (i >=0 && j < s.length && s[i] == s[j]) do
            i -= 1
            j += 1 
        end

        if @max < j - i - 1
            @low = i + 1
            @max = j - i - 1
        end
    end

    # i = 0

    for i in 0..s.length do 
        expand(s, i, i)
        expand(s, i, i + 1) 
        i += 1
    end

    s[@low..(@low + @max - 1)]
end

print longest_palindrome('abbd')