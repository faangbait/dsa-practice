from typing import List

class Solution(object):
    """
    You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

    Find two lines that together with the x-axis form a container, such that the container contains the most water.
    
    Return the maximum amount of water a container can store.

    """
    
    def maxArea(self, height: List[int]):
        """
        :type height: List[int]
        :rtype: int
        """
        
        if len(height) == 2:
            return min(height)
        
        class Boundary(object):
            index = 0
            height = 0
            
            def __init__(self, idx, h):
                self.index = idx
                self.height = h
       
        def compute_area(left: Boundary, right: Boundary) -> int:
            x = right.index - left.index
            y = min(right.height, left.height)
            
            return x*y
        
        
        left = Boundary(0, height[0])
        right = Boundary(len(height) - 1, height[-1])
        
        old_max = 0
        
        for h in height:
            old_max = max(old_max, compute_area(left, right))
            
            if right.height <= left.height:
                right = Boundary(right.index - 1, height[right.index - 1])
            else:
                left = Boundary(left.index + 1, height[left.index + 1])

        return old_max
    
s = Solution()

def test_cases():
    assert 1 == s.maxArea([1,1])
    assert 49 == s.maxArea([1,8,6,2,5,4,8,3,7])

def test_middle_ridge():
    assert 7 == s.maxArea([1,1,1,1,2,1,1,1])
    assert 24 == s.maxArea([1,3,2,5,25,24,5])
    assert 200 == s.maxArea([1,8,100,2,100,4,8,3,7])
    
def test_zero_height():
    assert 49 == s.maxArea([1,8,6,2,0,4,8,3,7])

