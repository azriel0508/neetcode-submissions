class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #Input: two strings = s and t
        #Output: boolean = true or false
        #Brute Force: Go through each character compare it to all the characters in the other string, if it matches with one remove that character from both strings repeat with the next character, if both strings are empty then it is an anagram. 
        #Optimised Solution: We can go from sorting which has complexity of O(log n) because of the sorting algorithm to the more optimised solution which is frequency counting using a hashmap or two, which will bring us to O(n) time complexity with the sorting the space complexity is O(1) because we are not using a data structure
        if len(s) != len(t):
            return False
        
        count = {}

        for i in range(len(s)):
            count[s[i]] = 1 + count.get(s[i], 0)
            count[t[i]] = count.get(t[i], 0) - 1

        for j in count:
            if count[j] != 0:
                return False
        
        return True