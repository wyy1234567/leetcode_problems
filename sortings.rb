#selection sort
#start from index 0 of the array, find the minimum element in the remaining array(start from index 1), swap it with current element
def selection_sort(array)
    n = array.size - 1
    n.times do |i|
        min = i

        #find the min in the remaining array
        for j in (i + 1)..n do 
            min = j if array[j] < array[min]
        end

        #swap current with min
        if min != i
            temp = array[min]
            array[min] = array[i]
            array[i] = temp
        end
    end
    array
end

#merge sort
#sort the array in two halfs, then merge them together
def merge_sort(array)
    return array if array.size <= 1
    mid = (array.size / 2).floor
    left = merge_sort(array[0..mid - 1])
    right = merge_sort(array[mid..array.size])
    merge(left, right)
end

def merge(left, right)
    return right if left.empty?
    return left if right.empty?
    if left[0] < right[0]
        [left[0]] + merge(left[1..left.length], right)
    else
        [right[0]] + merge(left, right[1..right.length])
    end
end


#quick sort

#insertion sort




# print selection_sort([5, 4, 3, 2, 1])
print merge_sort([5, 4, 3, 2, 1])
