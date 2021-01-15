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