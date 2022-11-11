class Solution(object):
    """
    An integer x is a good if after rotating each digit individually by 180 degrees, we get
    a valid number that is different from x. Each digit must be rotated - we cannot choose to leave it alone.
    """

    def test_goodness(self, x):
        tmp_x = x
        idx = 0
        rotated_x = 0
        
        digit = tmp_x % 10
        if digit in [3,4,7]:
            return False
        if digit in [0,1,8]:
            rotated_x = digit
        if digit in [6]:
            rotated_x = 9
        if digit in [9]:
            rotated_x = 6
        if digit in [2]:
            rotated_x = 5
        if digit in [5]:
            rotated_x = 2

        tmp_x = int(tmp_x/10)

        while tmp_x >= 1:
            idx += 1
            digit = tmp_x % 10
            if digit in [3,4,7]:
                return False
            if digit in [0,1,8]:
                rotated_x += digit*(10**idx)
            if digit in [6]:
                rotated_x += 9*(10**idx)
            if digit in [9]:
                rotated_x += 6*(10**idx)
            if digit in [2]:
                rotated_x += 5*(10**idx)
            if digit in [5]:
                rotated_x += 2*(10**idx)
            
            tmp_x = int(tmp_x/10)
        
        return rotated_x != x
            
    def rotatedDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        for i in range(1,n+1):
            if self.test_goodness(i):
                count += 1
        return count
        