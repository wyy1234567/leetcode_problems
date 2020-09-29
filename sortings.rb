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
            array[i], array[min] = array[min], array[i]
            # temp = array[min]
            # array[min] = array[i]
            # array[i] = temp
        end
    end
    array
end

#selection sort on matrix with input: [[1, 2], [4, 8], [2, 8], [1, 100]]
def selection_sort(matrix)
    n = matrix.size - 1
    for i in 0..n do
        min = i
        for j in (i + 1)..n do 
            min = j if matrix[j][0] < matrix[min][0]
        end
        if min != i
            temp = matrix[min]
            matrix[min] = matrix[i]
            matrix[i] = temp
        end
    end
    matrix  
end

print selection_sort([[1,100],[11,22],[1,11],[2,12]])

# merge sort
# sort the array in two halfs, then merge them together
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

#insertion sort
#gradually find & remove the minimum element in the given array, then push it to a new arr
def insertion_sort(array)

    ans = []
    while !array.empty? do 
        min = remove_min(array)
        ans << min
    end
    ans
end

def remove_min(array)
    min = array[0]
    array.each do |num|
        if num < min
            min = num
        end
    end
    array.delete(min)
    min
end


#quick sort
#Find an element(pivot) which divides the array to two parts, left is smaller ones, right is larger ones
#step1: bring pivot to apropiate position; step2: quick sort the left; step3: quick sort the right
#pivot is always selected as the last element in the array

def quick_sort(arr, low, high)
    if low < high
        position = partition(arr, low, high)
        quick_sort(arr, 0, position - 1)
        quick_sort(arr, position + 1, high)
    end
    arr
end

def partition(arr, low, high)
    pivot = arr[high]
    i = low - 1 
    for j in low..high - 1 do 
        if arr[j] <= pivot
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
        end
    end
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    i + 1
end


print selection_sort([5, 4, 3, 2, 1])
# # print merge_sort([5, 4, 3, 2, 1])
# # print insertion_sort([5, 4, 3, 2, 1])
# print quick_sort([5, 4, 3, 2, 1], 0, 4)
# print quick_sort([10, 80, 30, 90, 40, 50, 70], 0, 6)



