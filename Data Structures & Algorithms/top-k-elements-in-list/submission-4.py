class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #Counting the freq of each number
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        #Assign each frequency value to the index of freq array and store in that index the numbers that have that frequency
        freq = [[] for _ in range(len(nums) + 1)]
        for key, value in count.items():
            freq[value].append(key)
        
        #then add all of the numbers with highest frequency top k
        ans = []
        for i in range(len(freq) - 1, 0, -1):
            for c in freq[i]:
                ans.append(c)
                if len(ans) == k:
                    return ans