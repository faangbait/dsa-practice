class Solution(object):
    """
    You are given an array representing a row of seats where seats[i] = 1 represents
    a person sitting in the ith seat, and seats[i] = 0 represents that the ith seat is empty (0-indexed).

    There is at least one empty seat, and at least one person sitting.

    Alex wants to sit in the seat such that the distance between him and the closest person to him is maximized. 

    Return that maximum distance to the closest person.
    """
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """

        seat_chunks = []
        cur_chunk = 0
        for seat in seats:
            if seat == 1:
                seat_chunks.append(cur_chunk)
                cur_chunk = 0
            else:
                cur_chunk += 1
    
        seat_chunks.append(cur_chunk)

        for idx,i in enumerate(seat_chunks[1:-1]):
            seat_chunks[idx+1] = (i+1) // 2

        return max(seat_chunks)
            

