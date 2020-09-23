
# Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.
# For example, given the following triangle
# [
#      [2],
#     [3,4],
#    [6,5,7],
#   [4,1,8,3]
# ]

#find min path from bottom to top
def minimum_total(triangle)
    return 0 if !triangle || triangle.empty? || triangle[0].empty?
    return triangle[0][0] if triangle.size < 2

    i = triangle.size - 2
    while i >= 0 do 
        for j in 0...triangle[i].size do 
            triangle[i][j] += [triangle[i + 1][j], triangle[i + 1][j + 1]].min
        end
    end

    triangle[0][0]
end