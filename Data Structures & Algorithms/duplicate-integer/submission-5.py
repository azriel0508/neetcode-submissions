class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #We use hashsets here:
        #Input = array called nums
        #Output = boolean true or false
        #Brute Force = Check each element against the next element against all of the elements in the array except itself
        #Optimised Solution: Use a hashset to store all the values, when we create a set in python it automatically gets rid of all duplicates so we can compare this to the length of the array
        #Since we are using hashset the space complexity is O(n) and time complexity is O(n)
        return len(nums) != len(set(nums))