class Solution:
    #Input: List of strings
    #Output: Encode function outputs an encoded string, decode brings back the input of the array of strings
    #Brute Force Method: We split the strings using one character and when decoding it we use a nested while loop
    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for word in strs:
            encoded += str(len(word)) + "#" + word
        
        return encoded
    def decode(self, s: str) -> List[str]:
        ans = []
        i, j = 0, 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            
            length = int(s[i:j])
            start = j + 1
            end = start + length
            ans.append(s[start:end])
            i = end
        return ans