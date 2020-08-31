#find a target number in a sorted array
# Input: nums = [1,2,2,4,5,5], target = 2
# Output: 1 or 2
#return -1 if not found

def search_target(nums, target)
    return -1 if nums.empty? || !target
    start_ind = 0
    last_ind = nums.size - 1
    mid = (start_ind + last_ind) / 2

    #having condition as start_ind + 1 < last_ind will be helpful in find first/last position in function
    #also avoid infinite loop when the array only has two elements
    while start_ind + 1 < last_ind do 
        mid = start_ind + (last_ind - start_ind) / 2
        if (nums[mid] == target)
            last_ind = mid
        elsif nums[mid] > target
            last_ind = mid
        else
            start_ind = mid
        end
    end

    #find first position
    #if we wanna find the last position, check last_ind first
    if nums[start_ind] == target
        return start_ind
    end

    if nums[last_ind] == target
        return last_ind
    end

    return -1
end

# puts search_target([1,2,2,4,5,5], 2)
# puts search_target([1,2,2,4,5,5], 3)


#find target in a rotated array 
#input [10, 12, 14, 18, 1, 4], target = 1
#output = 4

def find_target(nums, target)
    return -1 if nums.empty? || !target
    start_ind = 0
    last_ind = nums.size - 1

    while (start_ind + 1 < last_ind) do
        mid = start_ind + (last_ind - start_ind) / 2

        if nums[mid] == target
            return mid
        end

        if nums[start_ind] < nums[mid]
            if nums[start_ind] <= target && target <= nums[mid]
                last_ind = mid
            else
                start_ind = mid
            end
        else
            if nums[mid] <= target && target <= nums[last_ind]
                start_ind = mid
            else
                last_ind = mid
            end
        end
    end

    return start_ind if nums[start_ind] == target
    return last_ind if nums[last_ind] == target
    return -1
end

puts find_target([10, 12, 14, 18, 1, 4], 4)
puts find_target([10, 12, 14, 18, 1, 4], 6)

#find top element in a mountain sequence 
# Input: nums = [1,2,6,4,5,2]
# Output: 6

def mountain_seq(nums)
    start_ind = 0
    last_ind = nums.size - 1
    while start_ind + 1 < last_ind do 
        mid = start_ind + (last_ind - start_ind) / 2
        if nums[mid] > nums[mid + 1]
            last_ind = mid
        else
            start_ind = mid
        end
    end

    [nums[start_ind], nums[last_ind]].max
end

puts mountain_seq([1,2,6,4,5,2])

#if we have multiple peaks, then randomly return one peak

def find_peak(nums)
    start_ind = 1
    last_ind = nums.size - 2
    while start_ind + 1 < last_ind do 
        mid = start_ind + (last_ind - start_ind) / 2
        if nums[mid] < nums[mid - 1]
            last_ind = mid
        elsif nums[mid] < nums[mid + 1]
            start_ind = mid
        else
            last_ind = mid
        end

        # if nums[mid] < nums[mid + 1]
        #     start_ind = mid
        # else
        #     last_ind = mid
        # end
    end
    nums[start_ind] < nums[last_ind] ? last_ind : start_ind
end


puts find_peak([1, 2, 1, 3, 4, 5, 7, 6])

