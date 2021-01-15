#combinatin sum
def combinationSum(candidates, target):
    candidates.sort()
    res = []

    def backtrack(candidates, path, res, target):
        if target < 0:
            return 
        if target == 0:
            res.append(res)
            return 
        for i in range(len(candidates)):
            backtrack(candidates[i:], path + [candidates[i]], res, target - candidates[i])
    
    backtrack(candidates, [], res, target)

    return res

#subset
def subset(nums):
    res = []

    def backtrack(nums, path, res):
        res.append(path)
        for i in range(len(nums)):
            backtrack(nums[i+1:], path+[nums[i]], res)

    backtrack(nums, [], res)
    return res

#permutation
def permutation(nums):
    res = []

    def backtrack(nums, path, res):
        if not nums:
            res.append(path)
            return 

        for i in range(len(nums)):
            backtrack(nums[:i]+nums[i+1:], path+[nums[i]], res)
    
    backtrack(nums, [], res)
    return res 