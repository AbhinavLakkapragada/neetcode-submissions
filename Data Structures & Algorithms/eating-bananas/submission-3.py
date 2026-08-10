class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        import math
        l,r = 1,max(piles)
        res = r

        while l<=r:
            k = (l+r)//2
            H=0
            for p in piles:
                H += (p+k-1)//k
            if H<=h:
                res = k
                r = k-1
            else:
                l=k+1

        return res

        


        