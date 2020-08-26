# Given two sorted arrays nums1 and nums2 of size m and n respectively.
# Return the median of the two sorted arrays.
# Follow up: The overall run time complexity should be O(log (m+n)).

# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.

#this problem uses binary search algorithm
#partition both nums1 & nums2 to 2 parts, left part is less than right part


def find_median_sorted_arrays(nums1, nums2)
    #make sure the nums2 is always the shorter one
    return find_median_sorted_arrays(nums2, nums1) if nums1.length < nums2.length
    n1 = nums1.length
    n2 = nums2.length

    low = 0
    high = n2 * 2

    while low <= high do 
        mid2 = (low + high) / 2
        mid1 = n1 + n2 - mid2

        l1 = (mid1 == 0) ? -(2 ** 32) : nums1[(mid1 - 1) / 2]
        l2 = (mid2 == 0) ? -(2 ** 32) : nums2[(mid2 - 1) / 2]
        r1 = (mid1 == n1 * 2) ? 2 ** 32 : nums1[mid1 / 2]
        r2 = (mid2 == n2 * 2) ? 2 ** 32 : nums2[mid2 / 2]

        if l1 > r2
            low = mid2 + 1
        elsif l2 > r1
            high = mid2 - 1
        else
            return ([l1, l2].max + [r1, r2].min).to_f / 2
        end
    end
end