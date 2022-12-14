"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):
"""

class Solution(object):
    def findSolution(self, customfunction, z):
        """
        :type num: int
        :type z: int
        :rtype: List[List[int]]
        """
        x = 1
        y = 1
        results = []
        
        # get x bounds
        max_x = 1
        while True:
            ret = customfunction.f(max_x,1)
            if ret < z:
                max_x += 1
            else:
                break
        
        # get y bounds
        max_y = 1
        while True:
            ret = customfunction.f(1,max_y)
            if ret < z:
                max_y += 1
            else:
                break

        for i in range(1, max_x+1):
            for j in range(1, max_y+1):
                if customfunction.f(i,j) == z:
                    results.append([i,j])
        
        return results
    