class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #Input: array = nums, integer = target
        #Output: array = answers
        #Brute force: Add all possible combinations in the array and return true if we find the combination that equals to target thats going to be Space Complexity: O(n) because we are using another array to return, time complexity of O(n^2) because we are using a for loop
        #Optimised: Use a hashmap to store the value as the index and the key as the num[i] we use diff = target - num to find which number will sum up to target when added to our current num[i]
        count = {}

        for i, num in enumerate(nums):
            diff = target - num

            if diff in count:
                return [count[diff], i]
            
            count[num] = i