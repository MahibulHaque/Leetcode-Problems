class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        l, r = 1, max(piles)
        k = 0
        
        while l <= r:
            mid = (l + r) // 2
            
            totalTime = 0
            for p in piles:
                totalTime += ((p-1)//mid) + 1
            if totalTime <= h:
                k = mid
                r = mid - 1
            else:
                l = mid + 1
        return k