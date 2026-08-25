class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        freq = [[] for _ in range(len(nums) + 1)]

        for num, c in count.items():
            freq[c].append(num)

        ans = []

        for j in range(len(freq) - 1, 0, -1):
            for n in freq[j]:
                ans.append(n)
                if len(ans) == k:
                    return ans