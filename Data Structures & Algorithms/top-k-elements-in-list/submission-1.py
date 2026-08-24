class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #Input: int array, int k
        #Output: int array
        #brute force: The brute force solution would be having a counter and going through the whole array with a nested for loop checking each element to find the frequency of it in the array
        #Optimised Solution: First count the frequency of each unique element, then we create a list of the range of the allowed frequency and then we check the value of each element and map it to the right frequency number, then with k  we go through the frequency list from highest to lowest returning all until we reach our limit k

        count = {}

        for num in nums:
            count[num] = 1 + count.get(num, 0)

        freq = [[] for _ in range(len(nums) + 1)]

        for num, i in count.items():
            freq[i].append(num)

        result = []

        for i in range(len(freq) - 1, 0, - 1):
            for num in freq[i]:
                result.append(num)

                if len(result) == k:
                    return result

