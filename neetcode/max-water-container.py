# You are given an integer array heights where heights[i] represents the height of the 
# i
# t
# h
# i 
# th
#   bar.

# You may choose any two bars to form a container. Return the maximum amount of water a container can store.

# Example 1:



# Input: height = [1,7,2,5,4,7,3,6]

# Output: 36
# Example 2:

# Input: height = [2,2,2]

# Output: 4

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        global_max = 0
        for idx, left in enumerate(heights):
            for jdx, right in enumerate(heights):
                res = abs(jdx-idx) * min(left,right)
                if res > global_max:
                    global_max = res
        return global_max
