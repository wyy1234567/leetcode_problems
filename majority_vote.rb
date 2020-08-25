# You are given a list of integers nums containing n integers, where each number represents a vote to a candidate.

# Return the id of the candidate that has more than half of the votes. If there's not a majority vote, return -1.

#nums = [5, 5, 1, 1, 2, 2, 2, 2, 2] => 2
# nums = [3, 3, 4, 4] => -1

#Using Boyer Moore Algorith to do string searching
def majority_vote(nums)
    candidate = nil
    count = 0
    nums.each do |num|
        candidate = num if count == 0
        if candidate == num
            count += 1
        else
            count -= 1
        end
    end

    count = 0
    nums.each do |num|
        if num == candidate
            count += 1
        end
    end

    return candidate if count > nums.size / 2
    return -1
end


print majority_vote([3, 3, 4, 4])