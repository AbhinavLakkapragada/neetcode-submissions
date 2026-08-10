class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Brute Force O(nlogn)

        # First Hashmap to count Frequency
        count = {}
        for num in nums:
            count[num] = 1+ count.get(num,0)

        # Array to sort them all
        arr = []
        for num, cnt in count.items():
            arr.append([cnt,num])
        arr.sort() # To sort for top k elements

        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res
        