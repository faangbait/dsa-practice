class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        differences = 0
        while x > 0 or y > 0:
            if y % 2 != x % 2:
                differences += 1
            x>>=1
            y>>=1
        return differences

