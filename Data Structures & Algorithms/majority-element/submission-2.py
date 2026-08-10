class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = defaultdict(int)

        res = maxCount = 0

        for n in nums:
            count[n] += 1
            if maxCount < count[n]:
                maxCount = count[n]
                res = n
        
        return res
        