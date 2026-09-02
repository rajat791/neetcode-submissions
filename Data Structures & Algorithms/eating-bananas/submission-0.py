class Solution:
    import math
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        left, right = 1, max(piles)
        result = right

        while left <= right:
            midpoint = (left + right) // 2
            totalHours = [math.ceil(pile / midpoint) for pile in piles]
            totalHours = sum(totalHours)

            if totalHours <= h:
                right = midpoint - 1
            else:
                left = midpoint + 1
            
            result = midpoint
        
        return left
        