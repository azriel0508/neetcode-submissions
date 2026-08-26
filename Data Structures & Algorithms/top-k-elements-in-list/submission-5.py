class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #First we count the frequencies of each number
        count = {}

        for num in nums:
            count[num] = 1 + count.get(num, 0)

        #Then we create an array with indexes as the frequency:
        freq = [[] for _ in range(len(nums) + 1)]

        #We populate the array with the frequencies from count using the value as the index on the freq list and the key as the value
        for key, value in count.items():
            freq[value].append(key)
        
        #Then we get the top k frequent elements by looping through the frequency array in a descending order until only the given k
        answer = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                answer.append(num)
                if len(answer) == k:
                    return answer