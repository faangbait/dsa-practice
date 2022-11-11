class Solution(object):
    """
    You are given two strings order and s. All the characters of order are unique
    and were sorted in some custom order previously.

    Permute the characters of s so that they match the order that order was sorted. 
    More specifically, if a character x occurs before a character y in order, then 
    x should occur before y in the permuted string.

    Return any permutation of s that satisfies this property.
    """
    def customSortString(self, order, s):
        """
        :type order: str
        :type s: str
        :rtype: str
        """
        def sort_func(order,x):
            try:
                return order.index(x)
            except ValueError:
                return 1000
            
        result = list(s)        
        result.sort(key=lambda x: sort_func(order,x))
        return "".join(result)
