
const square = (x) => {
    x = parseInt(x)
    return (x * x) 
}

// const cap = (string) => {
//     var splitStr = string.toLowerCase().split(' ');
//     for (var i = 0; i < splitStr.length; i++) {
//         splitStr[i] = splitStr[i].charAt(0).toUpperCase() + splitStr[i].substring(1);
//     }
//     return splitStr.join(' ');
// }

var cap = (string) => {
    var arr = string.split(' ')
    for (var i = 0; i < arr.length; i++) {
        arr[i] = arr[i].charAt(0).toUpperCase() + arr[i].substring(1);
    }

    return arr.join(' ')
}

var numDecodings = function(s) {
    if (!s || s.length === 0) {
        return 0
    }

    var dp = new Array(s.length + 1).fill(0)

    dp[0] = 1
    dp[1] = s.charAt(0) === '0' ? 0 : 1

    for (var i = 2; i < dp.length; i++) {
        var char = parseInt(s.slice(i - 1, i));
        var chars = parseInt(s.slice(i - 2, i));

        if (char >= 1 && char <= 9) {
            dp[i] += dp[i - 1]
        }

        if (chars >= 10 && chars <= 26) {
            dp[i] += dp[i - 2]
        }
    }

    return dp[dp.length - 1]
}

// var numDecodings = (s) => {
//     if (!s || s.length == 0) {
//         return 0
//     }

//     var dp = new Array(s.length + 1).fill(0)
//     dp[0] = 1
//     dp[1] = s.charAt(0) === '0' ? 0 : 1

//     for (var i = 2; i < s.length; i++) {
//         var char = parseInt(s.charAt(i - 1, i));
//         var chars = parseInt(s.slice(i - 2, i));

//     }
// }

var isHappy = function(n) {
    var hash = {}
    while (!hash[n]) {
        hash[n] = true
        var sum = 0
        while (n != 0) {
            sum += Math.pow(n % 10, 2)
            n = parseInt(n / 10)
        }

        if (sum === 1) {
            return true
        } else {
            n = sum
        }
    }

    return false
}

var isValid = function(s) {
    var stack = []
    var hash = {')':'(', '}':'{', ']':'['}

    for (var i = 0; i < s.length; i++) {
        if (stack[stack.length - 1] && stack[stack.length - 1] === hash[s[i]]) {
            stack.pop()
        } else {
            stack.push(s[i])
        }
    }

    if (stack.length === 0) {
        return true
    } else {
        return false
    }
}

var helper = function(nums, subset, ans, start) {
    ans.push([...subset])
    for (var i = start; i < nums.length; i++) {
        if (i != start && nums[i] == nums[i - 1]) {
            continue;
        }
        subset.push(nums[i])
        helper(nums, subset, ans, i + 1)
        subset.pop()
    }
}

var subsetsWithDup = function(nums) {
    if (!nums) {
        return [];
    }
    
    if (nums.length === 0) {
       return [[]] 
    }
    
    var ans = []
    var subset = []
    nums = nums.sort((a, b) => a - b)

    helper(nums, subset, ans, 0)
    return ans
};

